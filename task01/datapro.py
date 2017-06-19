#!/usr/bin/env python
# coding=utf-8

import os
import linecache
import optparse
import pandas as pd
import logbook
from logbook.more import ColorizedStderrHandler

class DataProcessing(object):
    """This is the data processing class"""
    def __init__(self):
        self.log = getLogger('datapro', logFile=True)

    def getFileName(self, fileDir):
        """Desc: get File names from data dir"""
        try:
            self.log.info(fileDir)
            fileList = []
            for root,dirs,files in os.walk(fileDir):
                for file in files:
                    if os.path.splitext(file)[1] == '.dat':
                        fileList.append(os.path.join(root, file))
            return fileList

        except Exception as err:
            self.log.error("{}".format(err))

    def getFileDataLines(self, fileName, lineNo):
        """Desc: get data from file"""
        try:
            lines = linecache.getlines(fileName, lineNo)
            return lines[lineNo-1:]

        except Exception as err:
            self.log.error("{}".format(err))

    def getFileDataOneLine(self, fileName, lineNo):
        """Desc: get one line from data"""
        try:
            line = linecache.getline(fileName, lineNo)
            return line

        except Exception as err:
            self.log.error("{}".format(err))


    def readDataToPandas(self, fileName):
        """Desc: read data use pandas"""
        try:
            data=pd.read_table(fileName, header=None, delim_whitespace=True)
            return(data)

        except Exception as err:
            self.log.error("{}".format(err))

    def preCheck(self, dataDir):
        try:
            if os.path.exists(dataDir) is True:
                self.log.info("The dir '{}' is ok.".format(dataDir))
                return True

        except (TypeError) as err:
            self.log.error("Ths dir '{}' is not exists err: {}".format(dataDir, err))

    def writeResultToFile(self, data, resultFileName, type):
        try:
            self.log.info(type)
            if type == 'excel':
                ret=data.to_excel(resultFileName+'.xls', header=None)
                return ret
            elif type == 'csv':
                ret=data.to_csv(resultFileName+'.csv', header=None)
                return ret
            elif type == 'json':
                ret=data.to_json(resultFileName+'.json')
                return ret
            elif type == 'html':
                ret=data.to_html(resultFileName+'.html', header=None)
                return ret
            else:
                self.log.error('This type is not support')
                return 1

        except Exception as err:
            self.log.error("{}".format(err))


def getLogger(name, logFile=False):
    """Get Logger"""
    LOG_DIR = os.path.join('log')
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False).push_application()
    if logFile:
        logbook.FileHandler(os.path.join(LOG_DIR,'%s.log'%name),bubble=True).push_application()
    return logbook.Logger(name)

def getParse():
    """Desc: get Options parse."""
    usage='''\
Desc:

    This is dataprocessing Tool FOR Beverly.
    # python datapro.py --dir ./dir/data'''
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-d","--dir",dest="dataDir",help="This is the data dir path")
    parser.add_option("-f","--file",dest="retFile",help="This is the result file")
    parser.add_option("-t","--type",dest="type",help="you can choice csv|excel|html|json")
    return(parser)

if __name__ == '__main__':
    """
    Desc:
            This is dataprocessing Tool FOR Beverly.
    """
    parser = getParse()
    (options, args) = parser.parse_args()
    log= getLogger('datapro', logFile=True)
    datapro = DataProcessing()

    if options.dataDir is not None\
        and datapro.preCheck(options.dataDir) is True:

        fileList=datapro.getFileName(options.dataDir)
        data=pd.DataFrame()
        finalRet=pd.DataFrame()
        retList=[]
        for file in fileList:
            data=datapro.readDataToPandas(file)
            retList.append(data[1])

        finalRet=pd.DataFrame({"A": data[0], "B":reduce(lambda x, y: x + y, retList)})

        if options.retFile is not None\
                and options.type is not None:
            RESULT_DIR = os.path.join('result')
            if not os.path.exists(RESULT_DIR):
                os.makedirs(RESULT_DIR)
            fileName=RESULT_DIR+'/'+options.retFile
            datapro.writeResultToFile(finalRet, fileName,
                                                options.type)
        else:
            log.info(finalRet)

    else:
        parser.print_help()
        exit(1)

