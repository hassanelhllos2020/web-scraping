from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import shutil

browser = webdriver.Chrome()
browser.get("https://books.toscrape.com/")

covers = browser.find_elements(By.TAG_NAME,value="img")

#print(covers[0].get_attribute("alt"))
#print(covers[0].get_attribute("src"))

for i in range(len(covers[:3])):
    response = requests.get(covers[i].get_attribute("src"),stream="True")
    with open(f"images/img{i+1}.jpg","wb") as file:
        shutil.copyfileobj(response.raw, file)
    del response

browser.close()