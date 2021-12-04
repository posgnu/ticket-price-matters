from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import code
import csv

class LeaderBoard:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://beaconcha.in/validators/eth1leaderboard")
    
    def setting(self):
        select = Select(self.browser.find_element_by_name("deposits_length"))
        select.select_by_visible_text("100")

if __name__ == "__main__":
    browser = webdriver.Chrome("./chromedriver")
    browser.implicitly_wait(5)
    leader_board = LeaderBoard(browser)
    browser.implicitly_wait(5)
    leader_board.setting()
    sleep(5)

    # opening the csv file in 'w+' mode
    file = open('eth2.csv', 'a+', newline ='')
    write = csv.writer(file)

    rotate = 0
    while True:
        try:
            print(rotate)
            try:
                for i in range(100):
                    parsed = int(browser.find_element_by_xpath(f"//*[@id=\"deposits\"]/tbody/tr[{i + 1}]/td[2]").text[:-4].replace(',', ''))
                    write.writerows([[parsed]])
            except:
                print("parse fail")


            button = browser.find_element_by_xpath("//*[@id=\"deposits_next\"]")
            if "disabled" in button.get_attribute("class"):
                break
            
            button.click()
            sleep(5)
            rotate += 1
        except:
            print("Page load fail")
            sleep(5)


    code.interact(local=locals())

    sleep(10)
    browser.close()