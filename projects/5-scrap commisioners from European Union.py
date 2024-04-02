from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

browser = webdriver.Chrome()
browser.get("https://op.europa.eu/en/web/who-is-who/organization/-/organization/COM/COM")
time.sleep(1)

plus = browser.find_elements(By.XPATH,"//span[contains(@class,'op-icon-more')]")

while plus:
    for i in plus:
        i.click()
    time.sleep(3)
    try:
        plus = browser.find_elements(By.XPATH,"//span[contains(@class,'op-icon-more')]")
    except:
        plus = 0

all = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]")
labels = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]/a")
rows = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]/span")

links_all = browser.find_elements(By.XPATH,"//span[@class='wiw-sublevel-person-name']/a")
links = []
for ll in links_all:
    links.append(ll.get_attribute("href"))

print(len(links))
#print(len(rows))

emails = []
for l in links:
    browser.get(l)
    time.sleep(1)
    try:
        ad = browser.find_element(By.CLASS_NAME,"address-email")
        ad.click()
        time.sleep(0.5)
        ad = browser.find_element(By.CLASS_NAME,"address-email")
        emails.append(ad.text)
    except:
        emails.append("-")


browser.get("https://op.europa.eu/en/web/who-is-who/organization/-/organization/COM/COM")
time.sleep(3)

plus = browser.find_elements(By.XPATH,"//span[contains(@class,'op-icon-more')]")
pluses = list(plus)

while plus:
    for i in plus:
        i.click()
    time.sleep(3)
    try:
        plus = browser.find_elements(By.XPATH,"//span[contains(@class,'op-icon-more')]")
    except:
        plus = 0

print(emails)

with open("Commission.csv","w",newline="",encoding="utf-8") as file:
    header = ['name','role','phone','email']
    writer = csv.DictWriter(file,header)
    writer.writeheader()

all = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]")
labels = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]/a")
rows = browser.find_elements(By.XPATH,"//span[contains(@class,'tree-label')]/span")

label = " "
name = " "
role = " "
phone = " "
labels_counter = 0
rows_counter = 0
for a in range(len(all)):
    if all[a].text.strip() == labels[labels_counter].text.strip():
        label = all[a].find_element(By.XPATH,"./a").text
        with open("Commission.csv","a",newline="",encoding="utf-8") as file:
            header = ['name','role','phone','email']
            writer = csv.DictWriter(file,header)
            writer.writerow({
            'name':label,
            "role":"...",
            "phone":"..."})
        labels_counter += 1
    elif all[a].text.strip() == rows[rows_counter].text.strip():
        try:
            name = all[a].find_element(By.XPATH,".//span[@class='wiw-sublevel-person-name']").text
        except:
            name = "-"
        try:
            role = all[a].find_element(By.XPATH,".//span[@class='wiw-sublevel-person-field'][text()]").text
        except:
            role = "-"
        try:
            phone = all[a].find_element(By.XPATH,".//span[@class='wiw-sublevel-person-field']/a").text
        except:
            phone="-"
        try:
            email = emails[rows_counter]
        except:
            email = "-"
        with open("Commission.csv","a",newline="",encoding="utf-8") as file:
            header = ['name','role','phone','email']
            writer = csv.DictWriter(file,header)
            writer.writerow({
            'name':name,
            "role":role,
            "phone":phone,
            "email":email})
        rows_counter += 1
    else:
        print("erorr")

print("DONE")
print("total: "+ all)
print("labels: " + len(labels))
print("rows: " + len(rows))
print(len(emails))