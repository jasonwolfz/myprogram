from bs4 import BeautifulSoup
import urllib.request
import requests as rq
import re
import pandas as pd
import time
import csv

name_yearly = '2018'

a = open(name_yearly+'imdb_url.csv','w',newline='')
a1 = csv.writer(a)
a1.writerow(['number']+['url'])
a.close()
mojo_serch = pd.read_csv(name_yearly+'google_date.csv')
imdb_url1 = []
imdb_url2 = []
for i in range(len(mojo_serch)):
  number = mojo_serch.number[i]
  title = mojo_serch.title[i]
  title = title.strip()
  number = mojo_serch.number[i]
  print('搜尋名稱:'+title)
  url = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+title+'&s=all'
  print('搜尋網址:'+url)
  try:
    page = urllib.request.urlopen(url)
  except:
    pass
  else:
    bs = BeautifulSoup(page,'lxml')
    tr = bs.find_all('tr',class_='findResult odd')
    for trs,trrs in zip(tr,range(1)):
      try:
        td = trs.find('td',class_='result_text')
      except:
        pass
      else:
        tds = td.find('a')
        ttds = tds.text
        ttds = ttds.replace(' ','+')
        if ttds == title:
          print('標題:'+td.text)
          print('網址:'+tds['href'])
          hrefs = tds['href']
          a = open(name_yearly+'imdb_url.csv','a',newline='')
          a1 = csv.writer(a)
          a1.writerow([number]+['https://www.imdb.com'+hrefs+'?ref_=fn_al_tt_1'])
          a.close()
          #time.sleep(1)
        else:
          pass

