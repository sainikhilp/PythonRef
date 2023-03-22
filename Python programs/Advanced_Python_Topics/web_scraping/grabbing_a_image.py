
import requests
import bs4

result=requests.get("http://www.example.com/")

#print(result.text) #returns the entire html document as a single page

soup=bs4.BeautifulSoup(result.text,"lxml") #converts into proper structured css,html doc

print(soup)
print(soup.select('title')) #selects the title tag from the soup structured doc and 
                            #returns a list

print(soup.select('title')[0].getText())





