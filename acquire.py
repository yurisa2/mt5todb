from datetime import datetime
import MetaTrader5 as mt5
import numpy as np

class AcquireData:

    def __init__(self):
        self.mt5 = mt5
        # self.dal = dal.Dal()

        self.symbol_list = None
        self.y_start = None
        self.y_end = None

        self.market = 'B3'
        self.provider = 'Rico MT5'

        if not self.mt5.initialize():
            print("initialize() failed, error code =",self.mt5.last_error())
            quit()

    def get_period_ticks(self, queue_ticks):
        for symbol in self.symbol_list:
            for year in range(self.y_start, self.y_end+1):
                for month in range(2, 13):
                    utc_from = datetime(year, month-1, 1)
                    utc_to = datetime(year, month, 1)
                    ticks = mt5.copy_ticks_range(symbol,
                                                 utc_from,
                                                 utc_to,
                                                 mt5.COPY_TICKS_TRADE)
                    queue_ticks.put(ticks)

    def get_period_rates(self, timeframe, queue_rates):
        for symbol in self.symbol_list:
            for year in range(self.y_start, self.y_end+1):
                for month in range(2, 13):
                    utc_from = datetime(year, month-1, 1)
                    utc_to = datetime(year, month, 1)
                    ticks = mt5.copy_rates_range(symbol,
                                                 timeframe,
                                                 utc_from,
                                                 utc_to)
                    queue_rates.put(ticks)
