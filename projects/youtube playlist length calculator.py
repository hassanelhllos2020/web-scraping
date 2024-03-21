from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup
import time
print("Find the length of any YouTube playlist")
print("*------------------------*")
link = input("enter link:")
browser = webdriver.Chrome()

browser.get(link)
all = browser.page_source
time.sleep(5)
soup = BeautifulSoup(all, 'html.parser')


titles = soup.find_all("a",{"id":"video-title"})
times = soup.find_all("span",{"class":"style-scope ytd-thumbnail-overlay-time-status-renderer"})
hours = 0
minutes = 0
seconds = 0 

print("-----------------------")
for i in range(len(titles)):
    min = times[i].text.strip().split(":")
    if len(min) >= 3:
        hours += int(min[0])
        minutes += int(min[1])
        seconds += int(min[2])
    else:
        minutes += int(min[0])
        seconds += int(min[1])
total = seconds + (minutes*60) + (hours * 3600)
totalhours = total // 3600
totalmin =(total // 60) -  (totalhours *60)
totalsec = total - (totalmin*60) - (totalhours*3600)

print(f"Number of videso: {len(titles)}")
print(f"Total length: {totalhours} hours, {totalmin} minutes, {totalsec} seconds.")