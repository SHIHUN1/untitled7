#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/9/19 21:07


import logging
from logging.handlers import RotatingFileHandler
import os
import time
from Common import read_path

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

handler_2 = RotatingFileHandler(read_path.logs_path+"/Api_BaoJun_{0}.log".format(curTime),backupCount=20,encoding='utf-8')

#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])
