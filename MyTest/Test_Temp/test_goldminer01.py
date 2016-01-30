# -*- coding: utf-8 -*-
"""
Created on 2016/1/7 9:37  

@author: A.Y

本模块目的：
1.测试掘金的数据模块，DailyBar/Bar/Tick数据
2.将Bar数据存储到Panda的DataFrame，供绘制图形

"""

# import gmsdk.api

import gmsdk as gs
from gmsdk import md
from Util.Var import GMusername,GMpassword

dailybar=gs.DailyBar()
intrabar=gs.Bar()
tick=gs.Tick()

ret=md.init(GMusername, GMpassword)
print ret

if ret==0:

    # bars=md.get_dailybars("SZSE.000001",
    #             "2016-01-04 00:00:00",
    #             "2016-01-09 00:00:00")
    #
    #
    # for eachbar in bars:
    #     dailybar=eachbar
    #     print dailybar.strtime, dailybar.close

    # =========================================Intrabar 日内数据，但貌似还不支持2016年的数据===========
    # 必须写成XXXX-XX-XX的形式，不能是XXXX-X-X
    # ==========================get_bars
    intrabars=md.get_bars('SHSE.600000',
                60,
                '2016-01-08 09:30:00',
                '2016-01-08 10:30:00')
    # intrabars=md.get_bars(
    #     'CFFEX.IF1512',
    #     60,
    #     '2015-05-01 09:30:00',
    #     '2015-05-10 09:31:00',
    #     )
    for eachintrabar in intrabars:
        intrabar=eachintrabar
        print intrabar.strtime, ':intrabar.close:', intrabar.close # eachintrabar.close

    # print intrabar.sec_id
    # bardict=dailybar_to_dict(bar[0])
    #
    # print bardict

# =========================================get_last_ticks
    ticks=md.get_last_ticks('SZSE.000001')
    for eachtick in ticks:
        tick=eachtick
        print "Last Tick Asks:", tick.asks,"; Last Tick Open:", tick.open
# tick.open

    # =========================================Get_Ticks
    ticks=md.get_ticks('SZSE.000001','2016-01-08 9:30:00','2016-01-08 15:00:00')
    for eachtick in ticks:
        tick=eachtick
        print "Tick Time:",tick.strtime ,"; Tick Asks:", tick.asks,"; Tick Bid:", tick.bids

# ========================================= Last Bars
    intrabars=md.get_last_bars('SHSE.600000',60)
    for eachintrabar in intrabars:
        intrabar=eachintrabar
        print intrabar.strtime, "last bar:", intrabar.close

    md.close()