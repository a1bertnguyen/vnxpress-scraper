from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
import json

app = Flask(__name__) #edit binh dep trai


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/scraping")
def scraping():
    scrape_vnexpress = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(scrape_vnexpress.text, "html.parser")
    titles = soup.find_all("h3", class_="title-news")
    title = [title.a.text for title in titles]

    return jsonify(title)


@app.route("/scarping_url")
def scraping_url():
    scrape_vnexpress = requests.get("https://vnexpress.net/")
    soup = BeautifulSoup(scrape_vnexpress.text, "html.parser")
    news_post = []
    titles = soup.find_all("h3", class_="title-news")
    for title in titles:
        description_url = requests.get(title.a.get("href"))
        soup_des = BeautifulSoup(description_url.text, "html.parser")
        des = soup_des.find("p", class_="description")
        news_post.append(
            ({"title": title.text, "des": des.get_text(), "url": title.a.get("href")})
        )

    return jsonify(news_post)


if __name__ == "__main__":
    app.run(debug=True)
