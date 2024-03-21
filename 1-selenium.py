#https://www.selenium.dev/documentation/webdriver/elements/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome()

browser.get("https://elzero.org/")
#browser.find_element(By.ID,"search").send_keys("test")
browser.find_element(By.CSS_SELECTOR,"#search").send_keys("dark")
browser.implicitly_wait(5)
browser.find_element(By.CSS_SELECTOR,'.search-submit').submit()
browser.find_element(By.LINK_TEXT, "Selenium Official Page") #fin link element by inner text

#email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})

#browser.current_window_handle
#browser.current_url
#browser.get_screenshot_as_file("test.jpg")
#browser.back()
#browser.forward()
#browser.maximize_window()
#browser.minimize_window()

#It is used to track (or) find DOM element which has the focus in the current browsing context.
#  attr = browser.switch_to.active_element
#.get_attribute("title")
