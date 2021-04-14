from bs4 import BeautifulSoup
import urllib.request
import requests as rq
import re
import csv
import pandas as pd
import time

name_yearly = '2018'
#cop = re.compile("[^0-9]")

a = open(name_yearly+'budget.csv','w',newline='',encoding="utf-8")
a1 = csv.writer(a)
a1.writerow(['number']+['budget'])
a.close()

mojo_url = pd.read_csv(name_yearly+'imdb_url.csv')

for i in range(len(mojo_url)):
    number = mojo_url.number[i]
    url = mojo_url.url[i]
    page = urllib.request.urlopen(url)
    bs = BeautifulSoup(page, 'lxml')
    f1 = bs.find_all('div',class_='article',id='titleDetails')
    for f2 in f1:
        f3 = f2.find_all('div',class_='txt-block',recursive=False)
        for f4 in f3:
            budget = f4.text
            if 'Budget' in budget:
                movie_budget = budget[8:]
                movie_budget = movie_budget.replace('(estimated)','').strip()
                print('number:'+str(number))
                print('budget:'+movie_budget)
                a = open(name_yearly+'budget.csv','a',newline='',encoding="utf-8")
                a1 = csv.writer(a)
                a1.writerow([number]+[movie_budget])
                a.close()
            else:
                print('number:'+str(number))
                print('budget:None')
                pass
