#!/bin/bash

A_PROCESAR="a-procesar"
VENDA="venda"
RUPTURA="ruptura"
QUEBRA="quebra"
PROCESADOS="procesados"

log(){
    echo "[$(date --rfc-3339=seconds)]" "[$@]" >> ./evodashd.log
}

verify_exists_or_create_path(){

    PATH="$1"

    if [ ! -d "$PATH" ]; then
        /bin/mkdir -p "$PATH"

        if [ $? -ne 0 ]; then
            log "ERROR: " /bin/mkdir -p "$PATH"
            exit 1
        fi
    fi

}

procesar_modelo(){

    A_PROCESAR_PATH="$1"
    EXEC_PATH="$2"
    PROCESADOS_PATH="$3"

    verify_exists_or_create_path "$A_PROCESAR_PATH"
    verify_exists_or_create_path "$PROCESADOS_PATH"

    for i in $(/usr/bin/find "$A_PROCESAR_PATH/" -type f)
    do
        "$EXEC_PATH/prepare-files.sh" "$i"

        if [ $? -ne 0 ]; then
            log "ERROR: " "$EXEC_PATH/prepare-files.sh" "$i"
            exit 1
        fi
    done

    for i in $(/usr/bin/find "$A_PROCESAR_PATH/" -type f)
    do

        "$EXEC_PATH/read.py" "$i"

        if [ $? -ne 0 ]; then
            log "ERROR: " "$EXEC_PATH/read.py" "$i"
            exit 1
        fi

        /bin/mv "$i" "$PROCESADOS_PATH/"

        if [ $? -ne 0 ]; then
            log "ERROR: " /bin/mv "$i" "$PROCESADOS_PATH/"
            exit 1
        fi

    done
}

procesar(){

    procesar_modelo "./$A_PROCESAR/$VENDA" "./$VENDA" "./$PROCESADOS/$VENDA"
    procesar_modelo "./$A_PROCESAR/$QUEBRA" "./$QUEBRA" "./$PROCESADOS/$QUEBRA"
    procesar_modelo "./$A_PROCESAR/$RUPTURA" "./$RUPTURA" "./$PROCESADOS/$RUPTURA"

    for i in $(/usr/bin/find . -maxdepth 1 -name "*.json"); do

        ./els/upload.sh "$i"

        if [ $? -ne 0 ]; then
            log "ERROR: " ./els/upload.sh "$i"
            exit 1
        fi

    done

    for i in $(/usr/bin/find . -maxdepth 1 -name "*.json"); do
        /bin/rm "$i"

        if [ $? -ne 0 ]; then
            log "ERROR: " /bin/rm "$i"
            exit 1
        fi
    done

}

verify_exists_or_create_path "./$PROCESADOS"

while true
do
    procesar
    /bin/sleep 10
done