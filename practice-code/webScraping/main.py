# Web scraping means automatically extracting data from websites using a program instead of copying it manually.

#? 3 Steps in web scraping

# 1. Fetching web pages - Use urllib.request to open the URL and get HTML.
import urllib.request

url = "https://github.com/Vinay-techdev"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

# 2. Parsing web pages - Use BeautifulSoup to convert HTML into a structured format.
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")

# 3.Step 3: Extract the Required Data - Find and extract elements (text, links, etc.).
print(soup.title.text)

for link in soup.find_all("a"):
    print(link.get("href"))  #! get actual data we need

# Full code user friendly
import urllib.request
from bs4 import BeautifulSoup

url = "https://github.com"

# Step 1: Fetch
html = urllib.request.urlopen(url).read().decode("utf-8")

# Step 2: Parse
soup = BeautifulSoup(html, "html.parser") #default -> "html.parser"

# Step 3: Extract
print(soup.title.text)


#! Example

url2 = "https://quotes.toscrape.com"
html2 = urllib.request.urlopen(url2).read().decode("utf-8")
soup2 = BeautifulSoup(html2, "html.parser")
print(soup2.title.text)

