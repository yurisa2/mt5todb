import acquire
import queue
from dotenv import load_dotenv

load_dotenv()

inst = acquire.AcquireData()

inst.symbol_list = ['WIN@D', 'WDO@D']

inst.y_start = 2020
inst.y_end = 2021


fila = queue.Queue()

inst.get_period_rates(inst.mt5.TIMEFRAME_D1)
