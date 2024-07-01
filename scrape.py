from bs4 import BeautifulSoup
import requests

scrape_vnexpress = requests.get("https://vnexpress.net/")
soup = BeautifulSoup(scrape_vnexpress.text, "html.parser")
titles = soup.find_all("h3", class_="title-news")
data = []

for title in titles:
    description_url = requests.get(title.a.get("href"))
    soup_des = BeautifulSoup(description_url.text, "html.parser")
    des = soup_des.find("p", class_="description")
    data.append(
        {"title": title.text, "des": des.get_text(), "url": title.a.get("href")}
    )


for item in data:
    print(item)
