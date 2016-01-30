# -*- coding: utf-8 -*-
"""
Created on 2016/1/28 10:34  

@author: A.Y

本模块目的：
"""
# from quantdigger import *
# import quantdigger
# import quantdigger.kernel.engine


import quantdigger
from quantdigger import Strategy

class DemoStrategy(Strategy):
    """ 策略A1 """

    def on_init(self, ctx):
        """初始化数据"""
        ctx.ma10 = quantdigger.MA(ctx.close, 10, 'ma10', 'y', 2)
        ctx.ma20 = quantdigger.MA(ctx.close, 20, 'ma20', 'b', 2)
        ctx.ma2 = quantdigger.NumberSeries()

    def on_symbol(self, ctx):
        return

    def on_bar(self, ctx):
        if ctx.curbar > 1:
            ctx.ma2.update((ctx.close[1]+ctx.close)/2)
        if ctx.curbar > 20:
            if ctx.ma10[2] < ctx.ma20[2] and ctx.ma10[1] > ctx.ma20[1]:
                ctx.buy(ctx.close, 1)
            elif ctx.position() > 0 and ctx.ma10[2] > ctx.ma20[2] and ctx.ma10[1] < ctx.ma20[1]:
                ctx.sell(ctx.close, ctx.position())

    def on_exit(self, ctx):
        return

if __name__ == '__main__':
    # quantdigger.set_config({
    #     'source': 'sqlite',
    #     'data_path': "D:\Tmp\data"
    # })
    quantdigger.set_config({
        'data_path': "D:\Tmp\data"
    })
    # quantdigger.set_symbols(['AA.SHFE-1.Minute', 'BB.SHFE-1.Minute'])
    quantdigger.set_symbols(['AA.SHFE-1.Minute'])
    profile = quantdigger.add_strategy([DemoStrategy('A1')])
    # print "step"
    quantdigger.run()