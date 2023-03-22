
import requests
import bs4

result_web_page=requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup=bs4.BeautifulSoup(result_web_page.text,"lxml")

computer_img=soup.select('.infobox-image img')


computer_img=computer_img[0]


computer_img_url=computer_img['src']


computer_img_url_info=requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

print(computer_img_url_info.content)
f=open('my_computer_img.jpg','wb')
f.write(computer_img_url_info.content)
f.close()
print("Image saved successful")








