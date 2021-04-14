from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request
import csv

name_yearly = '2018'

driver = webdriver.Chrome()
driver.get("http://www.google.com")
time.sleep(1)

element = driver.find_element_by_name("q")
element.send_keys("box office mojo")
#element.send_keys(Keys.ENTER)
button = driver.find_element_by_class_name("gNO89b").click()
time.sleep(1)

box_office_mojo = driver.find_element_by_class_name("LC20lb.DKV0Md").click()
time.sleep(1)
movie_yearly = driver.find_element_by_partial_link_text("Yearly").click()
time.sleep(1)
movie_2018 = driver.find_element_by_xpath('//*[@id="table"]/div/table[2]/tbody/tr[5]/td[1]/a').click()
time.sleep(3)
csv_file = open(name_yearly+'title.csv','a+',newline='',encoding="utf-8")
writer = csv.writer(csv_file)

url = driver.current_url
page = urllib.request.urlopen(url)
bs = BeautifulSoup(page, 'html.parser')
table = bs.find('table')
trs=table.find_all('tr',recursive=False)
for tr in trs:
    tds=tr.find_all('td')
    if len(tds) == 11:
        movie_title=tds[1].text
        print("movie_title=%s" % (movie_title))
        writer.writerow([movie_title])
csv_file.close()

f1 = open(name_yearly+'title.csv','r')
f2 = open(name_yearly+'mojo_title.csv','w')
for line in f1:
    f2.write(line.replace('"',''))
f1.close()

f2.close()
#driver.close()

