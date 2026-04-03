from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("https://www.nytimes.com/")
soup = BeautifulSoup(page.text, "html.parser")
headlines = soup.find_all("div", class_="css-xdandi")


file = open("headlines.txt", "w")
writer = csv.writer(file)

writer.writerow(["HEADLINES"])

findCount = 0
totalCount = 0

toFind = input("What are you searching for? ")

for headline in headlines:
    head = headline.find("p", class_="indicate-hover css-91bpc3")
    if head:
        print(head.text)
        totalCount += 1
        find = head.text.lower().find(toFind.lower())
        if find != -1:
            findCount += 1
        min = headline.find
        writer.writerow([head.text])
        
print("\nTotal Articles: ", totalCount, "\n")
print("Articles Mentioning", toFind, ": ", findCount)

for headline in headlines:
    head = headline.find("p", class_="indicate-hover css-91bpc3")
    if head:
        find = head.text.lower().find(toFind.lower())
        if find != -1:
            print(head.text)

print("\nFound Percentage: ", round(findCount/totalCount,2),"\n")