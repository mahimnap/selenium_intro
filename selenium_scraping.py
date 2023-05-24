from selenium import webdriver
from selenium.webdriver.chrome.options import Options #browser options
from selenium.webdriver.chrome.service import Service #service (used to execute drivermanager) 
from selenium.webdriver.common.by import By #selectors 
from webdriver_manager.chrome import ChromeDriverManager #automatic chromedriver updater/downloader
from selenium.webdriver.common.keys import Keys #keyboard keys used for text entries (e.g. search bar) 
#import time

#setting headless option
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions") #disables chrome extensions to avoid conflicts
chrome_options.add_argument("--disable-gpu") #forces selenium to only rely on CPU as extra layer of assurance in avoiding browser (on top of headless option)
chrome_options.add_argument("--no-sandbox") #disables security measures to avoid conflicts

#automatically install chromedriver if not already done (via Service)
#and passes in options set above to the selenium webdriver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) 

#scraping
start_url = "https://hellomeal.com/"
driver.get(start_url)
a = driver.find_element(By.CLASS_NAME, "site-description")
print ("this text: " + "'" + a.text + "'")

#print(driver.page_source.encode("utf-8"))
# driver.maximize_window() - logic if you remove headless option and want to see scraping process in the browser itself