import os
import requests
from bs4 import BeautifulSoup
import string

URL = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
N_of_pages = int(input())
TypeOfArticle = str(input())

def extractText(url, folder_name):
    new_r = requests.get(url)
    new_soup = BeautifulSoup(new_r.content, "html.parser")
    new_article = new_soup.find("div", {"class" : ("c-article-body" or "c-article-body u-clearfix")})
    a = new_article.text.strip()
    fileName = artName.text.strip(string.punctuation).replace(" ", "_")

    FilePath = os.path.join(folder_name, f"{fileName}.txt") #  задаем относительный путь к файлу, склеивая его имя с именем папки
    file = open(f"{FilePath}", "w", encoding = "utf-8")
    file.write(a.replace("\n", ""))
    file.close()

def FindArt_of_Type (pageURL):
    r = requests.get(pageURL)
    soup = BeautifulSoup(r.content, "html.parser")
    articles = soup.find_all("article", {"class": "u-full-height c-card c-card--flush"})
    for article in articles:
        artType = article.find("span", {"class" : "c-meta__type"})
        global artName
        artName = article.find("a", {"class":"c-card__link u-link-inherit"})
        if artType.text == TypeOfArticle:
            url = "https://www.nature.com" + (article.find("a")).get("href")
            extractText(url, folder_name)

for N in range (N_of_pages):
    pageURL = f"{URL}&page={N+1}" #определем адрес
    folder_name = f"Page_{N+1}" #  задаем имя папки
    os.mkdir(folder_name) #  создаем папку с этим именем
    FindArt_of_Type(pageURL) #ищем статьи опр. типа по этому адресу

print("Saved all articles")
