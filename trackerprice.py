# main
import time
import gmwhale
import pricetrack
import fn
import setup_var as sv
import test
import fn_stock

def main():
    while True:
        if fn.time_next_day():
            gmwhale.gmwhale()
            fn.get_report()
            fn_stock.get_exchangerate()
            fn_stock.get_stock_price()
        if fn.bar_time(sv.interval_candle,fn.time_server()):
            pricetrack.pricetrack()
        time.sleep(1)

if __name__ == "__main__":
    main()