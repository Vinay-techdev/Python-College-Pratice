from bs4 import BeautifulSoup
import requests

#? sends on HTTP Get request to the given url
# the server responds with data
#sucess 200   #not found 404

html = requests.get("https://www.thehindu.com/") 
print("\nStatus Code: ",html.status_code)

#? using urlib.reqeust 
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

#! url = "https://www.thehindu.com/"  Forbidden from extracting
# html = urlopen(url)
# soup = BeautifulSoup(html,"lxml") #defult html.pares but we can give lxml
# print(soup.title.text)


from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html) #defult html.pares but we can give lxml
print("\nTitle text: ",soup.title.text)
print("\nType: ",type(html))

#? display the Content from the website
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

html = requests.get("https://www.thehindu.com/")
print("\nStatus: ",html.status_code)
print("\nHTML text: ",html.text)

soup = BeautifulSoup(html.content)
print("\nHTML title: ",soup.title)
print("\nHTML title text: ",soup.title.text)
print("\nHTML title string: ",soup.title.string)

#? Response & JSON Response 
url = "https://openlibrary.org/subjects/love.json"
response = requests.get(url)
print("\nResponse: ",response)

print("\nJson Response: ",response.json())

#? get_text -> title.text
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html) #defult html.pares but we can give lxml
#print(soup.title.text)
text = soup.get_text()
print("\nget_text(): ",text)

#? Tag names - find_all()
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html) #defult html.pares but we can give lxml
#print(soup.title.text)
text = soup.get_text()
#print(text)
all_tags = soup.find_all(True)

print("\nTag Names: ")
for tag in all_tags:
    print(tag.name)

#? find_all('a) - only achors tags

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html) #defult html.pares but we can give lxml
text = soup.get_text()
anchors = soup.find_all('a')
print("\n achars Tags:")
for a in anchors:
    print(a.get_text(strip=True))# strip=True removes extra spaces

#? find_all('p') -> only paragraph tag
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://quotes.toscrape.com/"
html = urlopen(url)
soup = BeautifulSoup(html) #defult html.pares but we can give lxml
text = soup.get_text()
paragarp = soup.find_all('p')
print("\n Paraghrap Tags:")
for p in paragarp:
    print(p.get_text(strip=True))  # strip=True removes extra spaces