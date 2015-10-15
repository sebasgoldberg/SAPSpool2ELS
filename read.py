#!/usr/bin/python
#encoding=utf8
__author__ = 'JSGold'

import psycopg2
import sys
import datetime

TIPO_CONDICION = 0
TIENDA = 1
MATERIAL = 2
MATERIAL_PADRE = 3
UNIDAD_MEDIDA = 4
VALIDO_HASTA = 5
VALIDO_DESDE = 6
PRECIO = 7
MONEDA = 9
DESCRIPCION = 10

class NoDataRecordException(Exception):
    pass

def parse(line):
    register = line.split('|')
    if len(register) <= 3:
        raise NoDataRecordException(u'Registro de datos no encontrado')
    register = register[1:-1]
    for i in range(len(register)):
        register[i] = register[i].strip()
    if register[0] == "TpC.":
        raise NoDataRecordException(u"El registro de cabecera no es un registro de datos")
    if register[0] == "*":
        raise NoDataRecordException(u"El registro de totales no es un registro de datos")
    if register[PRECIO] == "":
        register[PRECIO] = "0"
    return ({"material": register[MATERIAL],
        "descripcion": register[DESCRIPCION],},
        {"tipoCondicion":register[TIPO_CONDICION],
            "material": register[MATERIAL],
            "materialPadre": register[MATERIAL_PADRE],
            "validoDesde": datetime.datetime.strptime(register[VALIDO_DESDE],"%d.%m.%Y"),
            "validoHasta": datetime.datetime.strptime(register[VALIDO_HASTA],"%d.%m.%Y"),
            "unidadMedida": register[UNIDAD_MEDIDA],
            "tienda": register[TIENDA],
            "precio": float(register[PRECIO].replace('.','').replace(',','.')),
            "moneda": "BRL",})

def read(filename):
    conn = psycopg2.connect("dbname='precios'")

    cur = conn.cursor()

    cur.execute("SET DateStyle='ISO'")

    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.decode("utf8","replace")
            try:
                material, condicion= parse(line)
                
                #print(material)
                cur.execute("select * from materiales where material = %(material)s", material)
                rows = cur.fetchall()
                if len(rows) == 0:
                    cur.execute("insert into materiales (material, descripcion) values (%(material)s, %(descripcion)s)", material)

                #print(condicion)
                cur.execute(
                        """select * 
                        from condicionesMateriales 
                        where 
                            tienda = %(tienda)s and
                            tipoCondicion = %(tipoCondicion)s and 
                            material = %(material)s and
                            unidadMedida = %(unidadMedida)s and
                            validoDesde = %(validoDesde)s""", condicion)
                rows = cur.fetchall()
                if len(rows) == 0:
                    cur.execute(
                        """insert into condicionesMateriales (
                            tienda,
                            tipoCondicion,
                            material,
                            unidadMedida,
                            validoDesde,
                            materialPadre,
                            validoHasta,
                            precio,
                            moneda)
                        values(
                            %(tienda)s,
                            %(tipoCondicion)s,
                            %(material)s,
                            %(unidadMedida)s,
                            %(validoDesde)s,
                            %(materialPadre)s,
                            %(validoHasta)s,
                            %(precio)s,
                            %(moneda)s ) """, condicion)

                #print ("OK")
            except NoDataRecordException:
                pass
            except Exception:
                print("ERROR en linea: %s" % line)

    conn.commit()

for f in sys.argv:
    read(f)
