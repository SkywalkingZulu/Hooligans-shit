from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BROWSERSTACK_URL = 'https://jasonwiiliams1:px7LhzNny2P8Nz1vyNxy@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
          
  'os' : 'Windows',
  'os_version' : '10',
  'browser' : 'Chrome',
  'browser_version' : '80',
  'name' : "jasonwiiliams1's First Test"

}

driver = webdriver.Remote(
    command_executor=BROWSERSTACK_URL,
    desired_capabilities=desired_cap
  )

driver.get("https://www.youtube.com/watch?v=qOtsn2HsQcs&list=PLfPyAFKY-OgxFYv8W-8JqGUub-9NP8JDo")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys(":space")
elem.submit()
print(driver.title)
