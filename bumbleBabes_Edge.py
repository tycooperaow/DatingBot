from selenium import webdriver
from selenium.webdriver.common.keys import Keys #
from selenium.common import exceptions
import time, datetime, os, random, sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class BumbleBot:
    def __init__(self):
        self.driver = webdriver.Edge("C:/Users/Ty Cooper/Desktop/Coding/Apps/instagram_auto/edgedriver.exe")

    def closeBrowser(self):
           self.driver.close()

    def login(self):
           driver = self.driver
           driver.get("https://www.facebook.com/")
           time.sleep(3)
           driver.get('https://bumble.com/app')

    def testing_luck(self):
         driver = self.driver
         feelings = random.randint(0,1)
         read_profile = random.uniform(0.5, 3)
         presentation = driver.find_element_by_xpath("//div[contains(@class, 'encounters-action encounters-action--like')]")
         conceded = driver.find_element_by_xpath("//div[contains(@class, 'encounters-action encounters-action--dislike')]")
         if feelings == 1:
             time.sleep(read_profile)
             presentation.click()
         elif feelings == 0:
             time.sleep(read_profile)
             conceded.click()


myPassword = os.environ.get('facee_pass')
bumbleBabes = BumbleBot()
bumbleBabes.login()
time.sleep(20)

while True:
        bumbleBabes.testing_luck()
