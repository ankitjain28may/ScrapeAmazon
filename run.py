from bs4 import BeautifulSoup
import requests
import urllib.request
import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = input("Enter Product Name\n")# you can change the query for the image  here
query= query.split()
query='+'.join(query)
url="http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+query+"&rh=i%3Aaps%2Ck%3A"+query
print(url)

#add the directory for your image here
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)
print(soup.title)


ActualImages=[]# contains the link for Large original images, type of  image
reviews=[]
for a in soup.find_all("a", class_="s-access-detail-page"):
    try:
        if a.find("h2") == None:
            name = "None"
        else:
            name = a.find("h2").string
        link = a.get("href")
        ActualImages.append((link,name))
    except Exception as e:
        print(e)

# print(ActualImages)
for i ,(link,name) in enumerate(ActualImages):
    print("%d - %s  " % (i, name))

l = len(ActualImages)
print("there are total" , l,"links")

review = int(input("Enter the product number to get reviews\n"))

if review < l:
    link,name = ActualImages[review]
    print(link)
    print("\n")
    so = get_soup(link,header)
    print(so.title)
    for rev in so.find_all(id="revMHRL"):
        data = rev.find_all("div", class_="a-row a-spacing-small")
        i=1;
        for tag in data:
            r = tag.find("div", class_="a-section")
            print("Review %d - %s" % (i, r.text))
            print("\n")
            i+=1







# for i ,(img,Type) in enumerate(ActualImages):
# 	try:
# 		if len(Type)==0:
# 			Type='jpg'
# 		path=str(i)+"."+Type
# 		print("Wait, Downloading..."+str(i))
# 		urllib.request.urlretrieve(img, "ho/"+path)
# 	except Exception as e:
# 		print(e)
# 		input(img)
