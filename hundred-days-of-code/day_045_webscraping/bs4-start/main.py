from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
article_tag = soup.select(selector=".titleline") # CSS select class, tag
article_texts = []
article_links = []
for article in article_tag:
    title = article.select_one(selector="a")
    text = title.getText()
    article_texts.append(text)
    link = title.get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

highest_upvote = max(article_upvotes)
index_max = article_upvotes.index(highest_upvote)
print(article_texts[index_max])
print(article_links[index_max])
print(highest_upvote)






# with open('./website.html', 'r', encoding='utf-8') as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.a)

# all_anchor_tags = soup.find_all(name="a") # find all elements with the a tag
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     # print(tag.getText()) # get the string
#     print(tag.get("href")) # get the attribute value by name
    
# heading = soup.find(name="h1", id="name") # get only h1 tag, with id="name"
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a") # first matching item, using CSS selectors
# print(company_url)

# name = soup.select_one(selector="#name") # use the id, using CSS selectors
# print(name)

# headings = soup.select(selector=".heading") # use the class selector
# print(headings)