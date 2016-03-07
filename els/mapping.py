#!/usr/bin/python
#encoding=utf8

from els.utils import MappingFileGenerator
from els.lang import Lang

L = Lang.get_instance()

wdecide = MappingFileGenerator()
wdecide.add(L.option)
wdecide.add(L.criteria)
wdecide.save('./wdecide/mapping.json')

ldap = MappingFileGenerator()
ldap.add(L.mail)
ldap.add(L.msExchRecipientTypeDetails)
ldap.add(L.cn)
ldap.add(L.sAMAccountName)
ldap.save('./ldap/mapping.json')

venda = MappingFileGenerator()
venda.add(L.loja)
venda.add(L.secao)
venda.add(L.material)
venda.add(L.matid)
venda.add(L.descricao_material)
venda.add(L.descricao_secao)

venda.add(L.venda_bruta)
venda.add(L.quantidade)
venda.add(L.custo)
venda.add(L.venda_liquida)

venda.save('./venda/mapping.json')


ruptura = MappingFileGenerator()
ruptura.add(L.loja)
ruptura.add(L.secao)
ruptura.add(L.material)
ruptura.add(L.matid)
ruptura.add(L.descricao_material)
ruptura.add(L.descricao_secao)
ruptura.add(L.data)
ruptura.add(L.ruptura)
ruptura.add(L.perda)

ruptura.save('./ruptura/mapping.json')


precios = MappingFileGenerator()
precios.add(L.loja)
precios.add(L.secao)
precios.add(L.material)
precios.add(L.matid)
precios.add(L.matid_com_um)
precios.add(L.descricao_material)
precios.add(L.descricao_secao)
precios.add(L.data)
precios.add(L.matid)
precios.add(L.rankvarabs)
precios.add(L.rankvartot)
precios.add(L.media)
precios.add(L.desvio)
precios.add(L.indice_variacion)

precios.save('./precios/mapping.json')

quebra = MappingFileGenerator()
quebra.add(L.matid)
quebra.add(L.loja)
quebra.add(L.secao)
quebra.add(L.descricao_secao)
quebra.add(L.material)
quebra.add(L.descricao_material)
quebra.add(L.unidade_medida)
quebra.add(L.tipo_movimento)
quebra.add(L.quantidade)
quebra.add(L.data)
quebra.add(L.importe)

quebra.save('./quebra/mapping.json')



windows_clients = MappingFileGenerator()
windows_clients.add(L.estado_antivirus)
windows_clients.add(L.nome_maquina)
windows_clients.add(L.auto_gestao_senha)
windows_clients.add(L.lync)
windows_clients.add(L.data)
windows_clients.add(L.altiris)
windows_clients.add(L.osArch)
windows_clients.add(L.osVersion)
windows_clients.add(L.status)
windows_clients.add(L.ip)
windows_clients.add(L.local)
windows_clients.add(L.pcA)
windows_clients.add(L.bandeira)
windows_clients.add(L.regional)
windows_clients.add(L.loja_critica)
windows_clients.add(L.tipo_loja)
windows_clients.add(L.lat_lon)
windows_clients.save('./mac/mapping.json')


nfe = MappingFileGenerator()
nfe.add(L.nota)
nfe.add(L.serie)
nfe.add(L.cnpj)
nfe.add(L.pedido)
nfe.add(L.fornecedor)
nfe.add(L.data_emissao)
nfe.add(L.data_criacao)
nfe.add(L.total_produto)
nfe.add(L.total_nota)
nfe.add(L.enviada_sap)
nfe.add(L.centro)
nfe.add(L.tipo_centro)
nfe.add(L.org_venda)
nfe.add(L.erro_remessa)
nfe.add(L.erro_cadastro)
nfe.add(L.erro_comercial)
nfe.add(L.erro_custo_real)
nfe.add(L.erro_embalagem)
nfe.add(L.erro_fiscal)
nfe.add(L.erro_material)
nfe.add(L.erro_quantidade)
nfe.add(L.erro_operacional)
nfe.add(L.erro_custo)
nfe.add(L.nome_fantasia)
nfe.add(L.dia)
nfe.add(L.mes)
nfe.add(L.semana)
nfe.add(L.check_nfs)
nfe.add(L.check_pedido)
nfe.add(L.consolidado_supply)
nfe.add(L.horti)
nfe.add(L.tipo_erro)
nfe.add(L.quan_erros)
nfe.save('./nfe/mapping.json')

clima = MappingFileGenerator()
nfe.add(L.quan_erros)
clima.add(L.pais)
clima.add(L.visao)
clima.add(L.conceito)
clima.add(L.item)
clima.add(L.evaluacao)
clima.add(L.benchmark)
clima.add(L.ano)
clima.save('./clima/mapping.json')

from retail.mapping import RetailMapping
retail = RetailMapping()
retail.save('./retail/mapping.json')

