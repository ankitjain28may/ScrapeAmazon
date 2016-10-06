from bs4 import BeautifulSoup
import requests
import urllib.request
import json
import validators

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = input("Enter Product Name\n")# you can change the query for the product  here
query= query.split()
query='+'.join(query)
url="http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+query+"&rh=i%3Aaps%2Ck%3A"+query
print(url)

header={'User-Agent':"Mozilla/6.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)
print(soup.title)


ActualProducts=[]# contains the link for the products
reviews=[]
for a in soup.find_all("a", class_="s-access-detail-page"):
    try:
        if a.find("h2") != None and validators.url(a.get("href")):
            name = a.find("h2").string
            link = a.get("href")
            ActualProducts.append((link,name))
    except Exception as e:
        print(e)

# print(ActualProducts)
for i ,(link,name) in enumerate(ActualProducts):
    try:
        print("%d - %s" % (i, name))
    except Exception as e:
        print(e)

l = len(ActualProducts)
print("there are total " ,l," links")

review = int(input("Enter the product number to get reviews\n"))

if review < l:
    link,name = ActualProducts[review]
    print(link)
    so = get_soup(link,header)
    print(so.title.string)
    print("\n")
    i=1;
    flag=0
    product = so.find_all(id="revMHFRL")
    if len(product) != 0:
        flag=1
        for rev in product:
            data = rev.find_all("div", class_="a-section celwidget")
            for tag in data:
                r = tag.find("div", class_="a-section")
                try:
                    print("Review %d - %s" % (i, r.text))
                    i+=1
                except Exception as e:
                    print(e)
    product = so.find_all(id="revMHRL")
    if len(product) != 0:
        flag=1
        for rev in product:
            data = rev.find_all("div", class_="a-row a-spacing-small")
            for tag in data:
                r = tag.find("div", class_="a-section")
                try:
                    print("Review %d - %s" % (i, r.text))
                    i+=1
                except Exception as e:
                    print(e)
    if flag != 1:
        print("No Reviews Found")
else:
    print("Invalid Input")