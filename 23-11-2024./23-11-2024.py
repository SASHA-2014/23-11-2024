from bs4 import BeautifulSoup
import requests
# response = requests.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
# #print(response.content)
# soup = BeautifulSoup(response.text, features="html.parser")
# A_light_in_the_Attic = soup.find("p", {"class": "price_color"})
# print(A_light_in_the_Attic.text)

response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")
coins = soup.find_all('article', {"class": "product_pod"})


for coin in coins:
    print(coin.text)
