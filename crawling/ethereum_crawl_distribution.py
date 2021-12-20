from os import write
import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

# 4 years block data (13135926 ~ Dec-07-2021) 
END_BLOCK_NUM = 13362645
START_BLOCK_NUM = 4842893

file = open("./ethereum.csv", "a")
writer = csv.writer(file)

options = webdriver.ChromeOptions()
options.add_argument('headless')

# browser = webdriver.Chrome("./chromedriver")
# browser.implicitly_wait(5)

for block_num in reversed(range(START_BLOCK_NUM, END_BLOCK_NUM)):
    # browser.get(f"https://etherscan.io/block/{block_num}")
    # miner = browser.find_element_by_xpath("//*[@id=\"ContentPlaceHolder1_maintable\"]/div[4]/div[2]/a")
    try:
        r = requests.get(f"https://www.blockchain.com/eth/block/{block_num}")

        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        idx = text.find("Miner")
        idx_end = text.find("Number of Transactions")

        addr = soup.get_text()[idx + 5:idx_end]
        addr = "".join(addr.split())
        writer.writerow([addr[2:]])
        print(f"Parse block {block_num}")
    except:
        pass
    