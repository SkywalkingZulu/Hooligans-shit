#Selenium Webdriver must be installed for this to work

import time;
from selenium import webdriver;

#time to refresh page (seconds)
Timer = 4320

#youtube link
link = 'https://youtube.com/playlist?list=PLfPyAFKY-OgxFYv8W-8JqGUub-9NP8JDo'

#number of views
views = 200

driver = webdriver.Chrome()
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
    print(i)