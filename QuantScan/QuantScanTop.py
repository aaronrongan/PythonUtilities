# -*- coding: utf-8 -*-
"""
Created on 2016/1/5 19:28  

@author: A.Y

本模块目的：扫描所有股票中的Top 10，如x日内涨幅最大，x日内...

模仿学习TuShare的Toplist函数
"""
import pandas as pd
from pandas.compat import StringIO
from tushare.stock import cons as ct
import numpy as np
import time
import re
import lxml.html
from lxml import etree
from tushare.util import dateu as du
from tushare.stock import ref_vars as rv

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

# def ScanTopVariation(daterange):
