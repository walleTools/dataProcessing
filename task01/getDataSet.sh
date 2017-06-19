#!/bin/bash

DIR="${1:-'test23333'}"

function mkdirDataDir(){
    if [ $? == 0 ] ; then
        /bin/mkdir -p ${DIR}/data
    else
        exit 1
    fi
}

function getDataFromFile(){
    for i in `ls ${DIR}/*.dat`
    do

        BASENAME=`basename $i`
        sed '1,14d' $i > $DIR/data/$BASENAME
    done
}

function returnDataDir(){
    echo "\033[32m Please go to the next step. \033[0m"
    echo "\033[31m if you just look the result , you can execute the following command \033[0m"
    echo " # python datapro.py --dir ${DIR}/data"
    echo
    echo "\033[31m if you want output the result file , you can execute the following command \033[0m"
    echo "\033[32m if you want file format as excel: \033[0m"
    echo " # python datapro.py --dir ${DIR}/data --file FileName --type excel"
    echo "\033[32m if you want file formmat as csv: \033[0m"
    echo " # python datapro.py --dir ${DIR}/data --file FileName --type csv"
    echo "\033[32m if you want file formmat as html: \033[0m"
    echo " # python datapro.py --dir ${DIR}/data --file FileName --type html"
    echo "\033[32m if you want file format as json: \033[0m"
    echo " # python datapro.py --dir ${DIR}/data --file FileName --type json"
    echo 
    echo "\033[32m You will find the result file in the './result' dir \033[0m"
    echo " # ls ./result"
    echo 
}

### main
if [[ -d "$DIR" ]] && [[ "t$DIR" != 'ttest23333' ]] ; then
    DIR=$1
else
    echo "[error]: No such file or directory" 
    exit 1
fi
mkdirDataDir
getDataFromFile
returnDataDir
