
#task: is to find all the books from the site
#      whose rating is 2 and a half stars

import requests
import bs4

list_of_books=[]

base_url="http://books.toscrape.com/catalogue/page-{}.html"

for index in range(1,51):
    scrape_url=base_url.format(index)
    web_page=requests.get(scrape_url)
    soup=bs4.BeautifulSoup(web_page.text,"lxml")
    books=soup.select(".product_pod")

    for book in books:
        if []==book.select(".star-rating.Two"):
            continue
        else:
            book_title=book.select('a')[1]['title']
            list_of_books.append(book_title)


print(list_of_books)

















