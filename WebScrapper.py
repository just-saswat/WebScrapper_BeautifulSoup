import requests
from bs4 import BeautifulSoup as bs
import csv
print("WebPage Scrapper Tool - $@$W@T")
url = input("Enter the URL of the Website :: ")
response = requests.get(url)
print("Response from WebSite :: ", response)

soup = (bs(response.text, "lxml"))
print("Container Type :: ", type(soup))

eleName = input("Enter the Name of the Element Tag :: ")
eleClass = input("Enter the Class of the Element Tag :: ")
names = soup.find_all(eleName, class_=eleClass)
print("Data Scrapped Successfully")
print("Length of Scraped Data :: ", len(names))

print("Contents of the Scarpped Data :: \n")
scrappedList = []
for name in names:
    scrappedList.append([(name.text).strip("\n")])
print(scrappedList)
print()

print("Want to Export Scrapped Data ???")
choice = int(input("Enter 1 to Continue or 0 to Exit :: "))
while(choice):
    print("Exporting the Scrapped Data tom CSV File")
    filename = input("Enter the Name of the File to be Export :: ")
    filename += ".csv"
    # writing to csv file
    with open(filename, 'w', newline='') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the fields
        csvwriter.writerow(["Categories"])
        # writing the data rows
        csvwriter.writerows(scrappedList)
    choice = False