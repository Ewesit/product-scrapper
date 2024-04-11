import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.jumia.co.ke/mlp-top-deals/"

response = requests.get(url)
# if response == 200:
#     print("The link can be scrapped.")
# elif response == 404:
#     print("The link is not found")
# else:
#     print(f"The link returned status code {response}.")


soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)
div = soup.find('div')
# print(div)
articles = div.find_all('article', class_='prd _fb _p col c-prd')
# print(articles)
# titles = articles.find('a', class_='btn _i _rnd -mas -fsh0 -me-start _wslt _sec')
# print(titles)

with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'New Price', 'Old Price', 'Rating'])

    for article in articles:
        name = article.find('h3', class_='name')
        new_price = article.find('div', class_='prc')
        old_price = article.find('div', class_='old')
        rating = article.find('div', class_='stars _s')
        reviewers = article.find('div', class_='rev')

        if name and new_price and old_price and rating and reviewers:
            rating_text = rating.text.strip()
            total_reviews = reviewers.text.strip()
            writer.writerow(['Name:', name.text])
            writer.writerow(['New Price:', new_price.text])
            writer.writerow(['Old Price:', old_price.text])
            writer.writerow(['Rating:', rating_text])
            writer.writerow(['Number of reviews:', reviewers.text])
            writer.writerow(['.' * 20])
            print("Name:", name.text)
            print("New Price:", new_price.text)
            print("Old Price:", old_price.text)
            print("Rating:", rating_text)
            print("Number of Reviews:", total_reviews)
            print("." * 20)