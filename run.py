from bs4 import BeautifulSoup
import re
import requests
import urllib.request
import json
import validators

def get_soup(url, header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def create_base_url():
    return "http://www.amazon.in"

def create_url_from_query(query):
    query = '+'.join(query.split())
    return create_base_url() + "/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+query+"&rh=i%3Aaps%2Ck%3A"+query

def get_review(data, index):
    review_rating = data.find("i", class_="review-rating")

    if review_rating is not None:
        rating = review_rating.text
    else:
        rating = "N/A"

    review_date = data.find("span", class_="review-date")

    if review_date is not None:
        date = review_date.text
    else:
        date = "N/A"

    review_title = data.find("a", class_="review-title")

    if review_title is not None:
        title = review_title.text
    else:
        title = "N/A"

    review_text = data.find("span", class_="review-text")

    if review_text is not None:
        text = review_text.text
    else:
        text = "-"

    print("Review - " + str(index) + " " + date + " | (" + rating + ")")
    print("---")
    print(str(title))
    print("---")
    print(text + "\n")

def get_reviews_pages(data):
    index = 0
    lastIndex = len(data) - 2

    for page in pages:
        if index == lastIndex: return int(page.text)
        index = index + 1

    return 1

def get_review_page_url(data):
    try:
        return create_base_url() + data.find("a").get("href")
    except Exception as e:
        print(e)
        return create_base_url()

def get_review_page_number_url(data, number):
    return str(re.sub("btm_[0-9]+", "btm_" + str(number), data)) + str("&pageNumber=") + str(number)

def get_reviews_all(index, url, pages):
    pageNumber = 1

    while pageNumber <= pages:
        pageUrl = get_review_page_number_url(url, pageNumber)
        #print("[D] pageNumber: " + str(pageNumber) + ", index: " + str(index) + ", pageUrl: " + str(pageUrl))
        index = get_reviews_from_html(get_soup(pageUrl, header), index)
        pageNumber = pageNumber + 1

def get_reviews_from_html(data, index):
    reviews = data.find_all("div", class_="a-section review")

    for review in reviews:
        index = index + 1
        get_review(review, index)

    return index

query = input("Enter Product Name\n") # you can change the query for the product  here
url = create_url_from_query(query)
#print(url)

header = { 'User-Agent': "Mozilla/6.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36" }
soup = get_soup(url, header)
#print(soup.title)

ActualProducts=[] # contains the link for the products
reviews=[]

for a in soup.find_all("a", class_="s-access-detail-page"):
    try:
        if a.find("h2") != None and validators.url(a.get("href")):
            name = a.find("h2").string
            link = a.get("href")
            ActualProducts.append((link,name))
    except Exception as e:
        print(e)

#print(ActualProducts)

for i ,(link,name) in enumerate(ActualProducts):
    try:
        print("%d - %s" % (i, name))
    except Exception as e:
        print(e)

l = len(ActualProducts)
print("\nThere are total ", l, " links")

review = int(input("Enter the product number to get reviews\n"))

if review < l:
    link,name = ActualProducts[review]
    #print("[D] Link: " + str(link))
    so = get_soup(link, header)
    print("\n" + str(so.title.string))

    product = so.find_all(id="revSAFRLU")

    if len(product) > 0:
        reviewsUrl = product[0].get('href')
        #print("[D] Review url: " + str(reviewsUrl))
        reviewsMain = get_soup(reviewsUrl, header)

        # Get page url
        pageUrlBody = reviewsMain.find("li", class_="a-selected page-button")
        pageUrl = get_review_page_url(pageUrlBody)

        # Get count of pages
        pages = reviewsMain.find("ul", class_="a-pagination")

        if pages is not None:
            pages = get_reviews_pages(pages)
        else:
            pages = 0

        print("\nNumber of review pages: " + str(pages) + "\n")
        numberPagesForFetch = int(input("Enter the number of pages for fetch\n"))

        # Fetch reviews
        get_reviews_all(0, pageUrl, numberPagesForFetch)
else:
    print("Invalid Input")
