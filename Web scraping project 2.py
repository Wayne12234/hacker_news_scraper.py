from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

title_headline = soup.find_all("tr", class_="athing submission")

# headline, article and points
for details in title_headline:
    title = details.find("span", class_="titleline").text
    link = details.a["href"]

    print(title)
    print(f"Link: {link}")
    print("-" * 30)

scores = soup.find_all("span", class_="score")

for score in scores:
    print(score.text)