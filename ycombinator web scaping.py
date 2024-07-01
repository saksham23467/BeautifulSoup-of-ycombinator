from bs4 import BeautifulSoup

import requests

response= requests.get('https://news.ycombinator.com/newest')
yc_webpage=response.text
soup= BeautifulSoup(yc_webpage, "html.parser")

article_tag= soup.find_all(name= 'span' , class_="titleline")
article_texts=[]
article_links=[]

for article in article_tag:
    text=article.getText()
    article_texts.append(text)
    links= article.find('a').get('href')
    article_links.append(links)

print(article_texts)
print(article_links)
print(article_upvotes)

x= max(article_upvotes)
print(x) #prints the max number of upvotes
y = article_upvotes.index(x)
print(article_texts[y]) #prints the headline of the news with most upvotes
print(article_links[y]) #prints the link of the news with most upvotes
