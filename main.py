from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

# use beautiful soup to parse the website
soup = BeautifulSoup(yc_webpage, "html.parser")

# make it prettier
# print(soup.prettify())

#we try to find some articles
articles = soup.find_all(name="span", class_="titleline")
# print(articles)


# to find any thing in the article, lets say the article topic
# article_text = articles.getText()
# print(article_text)
article_texts = []
article_links = []


for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

article_votes = [int(soup.getText().split()[0]) for soup in soup.find_all(name="span", class_="score")]





# to get hold of the article link and upvote
print(article_texts)
print(article_links)
print(article_votes)

largest_number = max(article_votes)
largest_index = article_votes.index(largest_number)
name_position = article_texts[largest_index]

print(f"the highest number is {largest_number}")
print(f"the highest now is {name_position}")




























"""we started our web scraping here."""

# with open("website.html" , encoding='utf-8') as file:
#     contents = file.read()
#href
#
#
# soup = BeautifulSoup(contents, "html.parser")
# all_anchors = soup.find_all(name="a")
# all_anchors
# print(all_anchors)