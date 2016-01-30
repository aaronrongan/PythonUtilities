#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gmsdk import md

md.init('demo@myquant.cn', '123456')
# 提取tick数据
r = md.get_ticks(
    'CFFEX.IF1512,CFFEX.IF1512',
    '2015-03-19 11:29:00',
    '2015-03-19 12:00:00',
)
print('get_ticks: ', len(r))
#提取tick快照
r = md.get_last_ticks('CFFEX.IF1512,')
print('get_last_ticks: ', len(r))
#提取最新N笔tick数据
r = md.get_last_n_ticks(
    'CFFEX.IF1512', 10)
print('get_last_n_ticks(10): ', len(r))
#提起一分钟分时数据(freq=60 seconds)
r = md.get_bars(
    'CFFEX.IF1512',
    60,
    '2015-05-01 09:30:00',
    '2015-05-10 09:31:00',
)
print('get_bars: ', len(r))
#提取bar快照
r = md.get_last_bars('CFFEX.IF1512,', 60)
print('get_last_bars: ', len(r))
#提取最新N笔bar数据
r = md.get_last_n_bars(
    'CFFEX.IF1512',
    60,
    10)
print('get_last_n_bars(10): ', len(r))
#提取日频数据
r = md.get_dailybars(
    'CFFEX.IF1512',
    '2015-05-01 00:00:00',
    '2015-05-20 23:59:59')
print('get_dailybars: ', len(r))
#提取dailybar快照
r = md.get_last_dailybars('CFFEX.IF1512,')
print('get_last_dailybars: ', len(r))
#提取最新N笔dailybar数据
r = md.get_last_n_dailybars('CFFEX.IF1512', 10)
print('get_last_n_dailybars(10): ', len(r))

input()
