from binance.client import Client
import json

client = Client("BzGJcEwvM3nDYKJFdABx6zttrAS75qPbUNTvC9zXuoLuZZ7XIZabRrsMWjkDgHFJ","clZDNDdWS0hx6dLKgTD00cugFg3g9Iz7fuoTtoYZIrBeOWuha1fRrvKjCNHycS3V")
print(client.ping())
# print(json.dumps(client.futures_account_balance(), sort_keys=False, indent=4, ensure_ascii=False,separators=(',',': ')))
# print(client.futures_recent_trades("USDT"))
# print(, sort_keys=False, indent=4, ensure_ascii=False,separators=(',',': ')))
