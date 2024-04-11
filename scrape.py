import requests
from bs4 import BeautifulSoup

# The website/url to send our http requests to
url = "https://zinduaschool.com/blog/"  

#get method allows you to send a get request - get sth from internet
#post method allows you to send a post request - post sth to internet

response = requests.get(url) #use requests.get function and pass the variable url 
                            #and the assign to a variable response
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup)

# headings = soup.find_all('h3')
# # print(headings)
# for heading in headings:
#     # print(heading)
#     print(heading.text)

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)

