# from turtle import ht
from bs4 import BeautifulSoup
import requests

# avoid 403 forbidden error === tries to prevents bots
headers = {'user-agent': 'my-app/0.0.1'}

# html content of the URL
html = requests.get("https://flatironschool.com/", headers=headers)

# convert html into nested nodes
doc = BeautifulSoup(html.text, 'html.parser')

# print(doc)
# print(doc.select(".heading-primary"))
# print(doc.select(".heading-primary")[0].contents)
print(doc.select(".heading-primary")[0].contents[0].strip())

# iterating 
courses = doc.select(".heading-25-extrabold.color-black")
for item in courses:
    print(item.contents[0].strip())
    
# name attribute 
print(doc.select(".heading-25-extrabold.color-black")[0].name)

# list of attributes === class, id ...
print(doc.select(".heading-25-extrabold.color-black")[0].attrs)

# children attribute
print(doc.select(".column-item.col-lg-3.col-sm-6")[0].children)









