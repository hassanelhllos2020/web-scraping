import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
movie = browser.find_elements(By.CLASS_NAME,"sc-b0691f29-0.jbYPfh.cli-children")


name =[]
year = []
length = []
rate = []
views = []
links = []
budget = []
gross = []

#movie[122].text.split("\n")[0][movie[122].text.split("\n")[0].index(".")+2:]


for i in movie[:10]:
    name.append(i.text.split("\n")[0][i.text.split("\n")[0].index(".")+2:])
    year.append(i.text.split("\n")[1].strip())
    length.append(i.text.split("\n")[2].strip())
    rate.append(i.text.split("\n")[4].strip())
    views.append(i.text.split("\n")[5].strip())
    links.append(i.find_element(By.TAG_NAME,"a").get_attribute("href"))

#name.append(i.text.split("\n")[0].strip()[i.text.strip().index(".")+2:].strip())

browser.close()

#print(*name,sep="\n")
#movie[0].find_element(By.TAG_NAME,"a").get_attribute("href")

browser2 = webdriver.Chrome()
for ls in links[:10]:
    browser2.get(ls)
    time.sleep(1)
    budget.append(browser2.find_element(By.XPATH,"//li[@data-testid='title-boxoffice-budget']/div//span").text)
    gross.append(browser2.find_element(By.XPATH,"//li[@data-testid='title-boxoffice-cumulativeworldwidegross']/div//span").text)

import csv
with open("movies.csv","w") as file:
    header = ["name","year","length","rate","views","budget","gross"]
    writer = csv.DictWriter(file,header)
    writer.writeheader()
    for m in range(len(name)):
        writer.writerow({
        'name':name[m],
        'year':year[m],
        'length':length[m],
        'rate':rate[m],
        'views':views[m],
        'budget':budget[m],
        'gross':gross[m]})

browser2.close()
print("Done")



#//a[@data-testid="title-cast-item__actor"]