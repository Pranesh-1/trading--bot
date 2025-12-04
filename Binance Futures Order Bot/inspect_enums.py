import binance.enums
for item in dir(binance.enums):
    if 'ORDER' in item:
        print(f"{item}: {getattr(binance.enums, item)}")
