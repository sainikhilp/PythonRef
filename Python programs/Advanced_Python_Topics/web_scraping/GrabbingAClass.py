

import requests
import bs4

result=requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup=bs4.BeautifulSoup(result.text,"lxml")



toc_texts=soup.select('.vector-toc-text')

print(toc_texts[1].text) #either .text or .getText() can be used


