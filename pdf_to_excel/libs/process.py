"""
- read config
- logging
"""

import os
import sys
import configparser
import logging
import datetime

class Base:
    def __init__(self):
        self.config = configparser.ConfigParser()
        if not self.config.read(r'C:\PlayGround\LANCERS\config\config.ini', 'UTF-8'):
            raise Exception('failed reading config.ini')

        now = datetime.datetime.now()
        logPathYear = os.path.join(self.config.get('DIR', 'logDir'), now.strftime('%Y'))
        logPathMonth = os.path.join(logPathYear, now.strftime('%m'))
        logFilePath = os.path.join(logPathMonth, now.strftime('%m%d') + '.log')

        if not os.path.exists(logPathYear):
            os.mkdir(logPathYear)
        if not os.path.exists(logPathMonth):
            os.mkdir(logPathMonth)
        if not os.path.isfile(logFilePath):
            with open(logFilePath, 'w', encoding='UTF-8') as f:
                print('created log file')

        # log name
        self.logger = logging.getLogger('debug log')

        # log level
        self.logger.setLevel(10)

        # console out put
        sh = logging.StreamHandler()
        self.logger.addHandler(sh)

        # out put to
        fh = logging.FileHandler(logFilePath)
        self.logger.addHandler(fh)

        # out put format
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)
        # out put
        # self.log(0, 'success')
        # self.log(1, 'failure')

    def log(self, flg, msg):
        if flg == 0:
            self.logger.info('----- ' + msg)
        else:
            self.logger.error('----- ' + msg)

    def getRiskRec(self):
        f = open(self.config.get('PATHs', 'recordPath'), 'r')
        records = f.readlines()
        first = records[0]
        last = records[1].replace('/n', '')
        f.close()
        self.log(0, first)
        self.log(0, last)
        return int(first), int(last)

    def saveRiskRec(self, first, last):
        f = open(self.config.get('PATHs', 'recordPath'), 'w')
        f.write(str(first) + "\n" + str(last))
        f.close()