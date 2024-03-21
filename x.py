#https://www.scrapingdog.com/blog/scrape-twitter/
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv



target = input("enter handel:@")
browser = webdriver.Chrome()

browser.get(f"https://twitter.com/{target}")
time.sleep(7)
content = browser.page_source
browser.close()
name = []
handel =  []
description = []
followers = []
following = []

#soup = BeautifulSoup(content,'html.parser')
try:
    soup = BeautifulSoup(content,'html.parser')
    name.append(soup.find("div",{"class":"r-1vr29t4"}).find("span").text)
    handel.append(soup.find("div",{"class":"r-1wvb978"}).text)
    description.append(soup.find("div",{"data-testid":"UserDescription"}).text)
    followers.append(soup.find_all("a",{"class":"r-rjixqe"})[0].text)
    following.append(soup.find_all("a",{"class":"r-rjixqe"})[1].text)
    print(name[0])
    print(handel)
    print(description)
    print(followers)
    print(following)
    with open("x.csv",'w') as x:
        header = ['name','handel','description','followers','following']
        writer = csv.DictWriter(x,header)
        writer.writeheader()
        writer.writerow({
            'name':name[0],
            'handel':handel[0],
            'description':"abc", #description[0]
            'followers':followers[0],
            'following':following[0]
        })
        print("Done!")
except Exception as erorr:
    print("try again")
    print(erorr)

    