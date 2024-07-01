import requests
from bs4 import BeautifulSoup as bs
url = "https://www.indianhobbycenter.com/#"
response = requests.get(url)
print("WebPage Scrapper Tool - $@$W@T")
print("Response from WebSite :: ", response)

soup = (bs(response.text, "lxml"))
print("Container Type :: ", type(soup))

names = soup.find_all("a", class_="item-menu")
print("Length of Scraped Data :: ", len(names))

print("Following Scarpped Data :: \n")
scrappedList = []
for name in names:
    scrappedList.append((name.text).strip("\n"))
print(scrappedList)
