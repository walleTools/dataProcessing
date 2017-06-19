### task01
### dataProcessing
### Usage:
```
# python datapro.py --help

    This is dataprocessing Tool FOR Beverly's Task01.

Desc:
    python datapro.py --dir ./dir/data

Options:
    -h, --help                  show this help message and exit
    -d DATADIR, --dir=DATADIR   This is the data dir path
    -f RETFILE, --file=RETFILE  This is the result file
    -t TYPE, --type=TYPE        you can choice csv|excel|html|json
```
### How To Use:
#### First, execute the getDataSet.sh to get valid Data from result data
```
# sh getDataSet.sh centerResults
Please go to the next step.
if you just look the result , you can execute the following command
# python datapro.py --dir centerResults/data

if you want output the result file , you can execute the following command
if you want file format as excel:
# python datapro.py --dir centerResults/data --file FileName --type excel
if you want file formmat as csv:
# python datapro.py --dir centerResults/data --file FileName --type csv
if you want file formmat as html:
# python datapro.py --dir centerResults/data --file FileName --type html
if you want file format as json:
# python datapro.py --dir centerResults/data --file FileName --type json

You will find the result file in the './result' dir
# ls ./result
```
