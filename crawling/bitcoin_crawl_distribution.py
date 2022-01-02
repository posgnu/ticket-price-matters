from os import write
import requests
import csv

# 4 years blocks data (2021.09.04 ~ 2021.12.04) 712550 - 699008
END_BLOCK_NUM = 642610
START_BLOCK_NUM = 502288

file = open("./bitcoin.csv", "a")
writer = csv.writer(file)


for block_num in reversed(range(START_BLOCK_NUM, END_BLOCK_NUM)):
    try:
        r = requests.get(f"https://blockchain.info/block-height/{block_num}?format=json")
        data = r.json()

        blocks = data["blocks"][0]
        tx = blocks["tx"][0]
        out = tx["out"][0]
        addr = out["addr"]

        writer.writerow([str(addr)])
        print(f"Parse block {block_num}")
    except:
        pass
    