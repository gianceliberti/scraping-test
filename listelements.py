import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup



response = requests.get("https://scrapeme.live/shop/")
soup = BeautifulSoup(response.content, "html.parser")
product_elements = soup.select("li.product")

# the list of dictionaries containing the
# scrape data
pokemon_products = []

for product_element in product_elements:
    name = product_element.find("h2").get_text()
    url = product_element.find("a")["href"]
    image = product_element.find("img")["src"]
    price = product_element.select_one(".amount").get_text()

    # define a dictionary with the scraped data
    new_pokemon_product = {
        "name": name,
        "url": url,
        "image": image,
        "price": price
    }
    # add the new product dictionary to the list
    pokemon_products.append(new_pokemon_product)

import csv

# scraping logic...

# create the "products.csv" file
csv_file = open('products.csv', 'w', encoding='utf-8', newline='')

# initialize a writer object for CSV data
writer = csv.writer(csv_file)

# convert each element of pokemon_products
# to CSV and add it to the output file
for pokemon_product in pokemon_products:
    writer.writerow(pokemon_product.values())

# release the file resources
csv_file.close()

import json

# scraping logic...

# create the "products.json" file
json_file = open('data.json', 'w')

# convert pokemon_products to JSON
# and write it into the JSON output file
json.dump(pokemon_products, json_file)

# release the file resources
json_file.close()
