#--$ pip install lxml
#--$ pip install requests
#--$ pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
import csv
#initalize the main site
page_num = 0
links = []
job_title = []
job_company = []
job_location = []
job_salary = []

job_input = job_input ="%20".join(input("enter job title: ").split(" "))
page_input = int(input("how many pages:"))
while True:
    results = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q={job_input}&start={page_num}")
    page_num += 1

    src = results.content

    soup = BeautifulSoup(src,'lxml')

#get main job list
    titles = soup.find_all("h2",{"class":"css-m604qf"})
    companys = soup.find_all("a", {"class":"css-17s97q8"})
    locations = soup.find_all("span",{"class":"css-5wys0k"})
    page_limit1 = soup.find('strong').text
    page_limit = int(page_limit1.replace(",",""))




# git main list vlaues and append it to lists
    for i in range(len(titles)):
        job_title.append(titles[i].text)
        job_company.append(companys[i].text)
        job_location.append(locations[i].text)
        links.append( titles[i].find("a").attrs["href"])

    print(f"page number: {page_num} added out of: {page_limit // 15}")
    if page_num >=  page_input:
        print("pages ended DONE!")
        break
    
#git page values
# for a in links :
#     linking = requests.get(a)
#     srclinks = linking.content
#     souplinks = BeautifulSoup(srclinks,'lxml')
#     salary = souplinks.find('span','css-4xky9y')
#     #job_salary.append(salary.text)
# print(salary)

with open("jobs.csv",'w',newline="") as jobs:
     header = ["title","company","location","link"]
     writer = csv.DictWriter(jobs,header)
     writer.writeheader()
     try:
         for l in range(len(job_title)):
             writer.writerow({
                 "title":job_title[l],
                 "company":job_company[l],
                 "location":job_location[l],
                 "link":links[l]
             })
     except:
         print(job_salary)
         print(len(job_salary))


print(f"total jobs: {len(job_title)}")

#for l in range(len(job_title)):
#print(job_title[l],job_company[l],job_location[l],sep=" | ")
