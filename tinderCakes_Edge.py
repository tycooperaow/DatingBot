from selenium import webdriver
from selenium.webdriver.common.keys import Keys #
from selenium.common import exceptions
import time, datetime, os, random, sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Edge("C:/Users/Ty Cooper/Desktop/Coding/Apps/instagram_auto/edgedriver.exe")

    def closeBrowser(self):
           self.driver.close()

    def login(self):
           driver = self.driver
           driver.get("https://www.facebook.com/")
           time.sleep(3)
           driver.get('https://tinder.com/app/recs')
 
    def testing_luck(self):
         driver = self.driver
         presentation = driver.find_element_by_xpath("//button[contains(@class, 'button Lts($ls-s) Z(0) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) recsGamepad__button D(b) Bgc(#fff) Wc($transform) recsGamepad__button--like Scale(1.1):h')]")
         presentation.click()
         presentation.send_keys(Keys.ARROW_RIGHT)
         time.sleep(1)

myPassword = os.environ.get('facee_pass')
tinderCake = TinderBot()
tinderCake.login()
time.sleep(20)

while True:
        tinderCake.testing_luck()
