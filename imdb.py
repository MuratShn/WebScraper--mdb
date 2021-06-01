import requests
from  bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 

baslık = []
yıl = []
süre = []
kategori = []
oy = []

start = np.arange(1,1001,50)
print(start)

def islem(link):
    url = link
    response = requests.get(url)
    icerik = response.content
    soup = BeautifulSoup(icerik,"html.parser")

    for i in soup.find_all("h3",{"class": "lister-item-header"}):
        a = i.find("a").text
        baslık.append(str(a))


    for i in soup.find_all("h3",{"class": "lister-item-header"}):
        a = i.find("span",{"class": "lister-item-year text-muted unbold"}).text
        a = a.strip("()I II	III IV V ")
        a = int(a)
        yıl.append(a)


    for i in soup.find_all("span",{"class" :"runtime"}):
        a = i.text
        a = int(a.replace("min",""))
        süre.append(a)


    for i in soup.find_all("span",{"class": "genre"}):
        a = i.text
        a = a.replace("\n","")
        kategori.append(str(a))
        
    for i in soup.find_all("div",{"class": "inline-block ratings-imdb-rating"}):
        a = i.get("data-value")
        oy.append(float(a))


## https://www.imdb.com/search/title/?groups=top_1000&start=101&ref_=adv_nxt
for i in start:
    url = "https://www.imdb.com/search/title/?groups=top_1000&start={}&ref_=adv_nxt".format(i)
    islem(url)



df = pd.DataFrame({"isim" : baslık,
                   "yıl" : yıl,
                   "süre" : süre,
                   "kategori" : kategori,
                   "oy" : oy
                   })


df.to_csv("imdb.csv") #csv dosyası olusturma

print(df.info())
print(df.index)
print(df.head())