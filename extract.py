from gazpacho import Soup
from bs4 import BeautifulSoup
import requests
import json
import uuid

# f=open("page_1","r")

urls = []
with open("page_1_to_3") as file_in:
    for line in file_in:
        urls.append(line.strip("\n"))

# print(urls)

books = []

for url in urls:
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    # title
    title = soup.findAll('p')[0]
    title = title.get_text()
    title = title[7:]
    # print(title)
    # bookid by uuid
    bookid = uuid.uuid1()
    bookid = str(bookid)
    # print(bookid)
    # author
    author = soup.findAll('p')[1]
    author = author.get_text()
    author = author[11:]
    # print(author)
    # imagesrc
    images = soup.findAll('img')[3]
    if(images.get("src")[0] == 'd'):
        images = soup.findAll('img')[4]
        imgsrc = images.get("src")
    else:
        imgsrc = images.get("src")
    # epub
    epub = soup.findAll('a')[28]
    epub = epub.get("href")
    # print(epub)
    # category
    category = soup.findAll('a')[35]
    category = category.get_text()
    # print(category)
    books.append({'title': title, 'bookid': bookid, 'author': author,
                  'image': imgsrc, 'epub': epub, 'category': category})
    print({'title': title, 'bookid': bookid, 'author': author,
           'image': imgsrc, 'epub': epub, 'category': category})


# print(books)
data = json.dumps(books, ensure_ascii=False).encode('utf-8')
js = open("data.json", "a")
js.write(data.decode())
# print(data)
