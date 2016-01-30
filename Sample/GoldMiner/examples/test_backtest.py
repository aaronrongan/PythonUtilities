# !/usr/bin/env python
# -*- coding: utf-8 -*-
from gmsdk.api import StrategyBase


class MyStrategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        super(MyStrategy, self).__init__(*args, **kwargs)
        self.oc = True

    def on_bar(self, bar):
        if self.oc:
            self.open_long(bar.exchange, bar.sec_id, 0, 100)
        else:
            self.close_long(bar.exchange, bar.sec_id, 0, 100)
        self.oc = not self.oc


if __name__ == '__main__':
    mystrategy = MyStrategy(
        username='demo@myquant.cn',
        password='123456',
        strategy_id='strategy_2',
        subscribe_symbols='SHSE.600000.bar.daily',
        mode=4,
        td_addr='localhost:8001')
    ret = mystrategy.backtest_config(
        start_time='2015-04-15 9:00:00',
        end_time='2015-05-15 15:00:00',
        initial_cash=1000000,
        transaction_ratio=1,
        commission_ratio=0,
        slippage_ratio=0,
        price_type=1)
    print('config status: ', ret)
    ret = mystrategy.run()
    print('exit code: ', ret)
