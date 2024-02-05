import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

# download the target page
response = requests.get("https://scrapeme.live/shop/")


# parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")
# product_search_element = soup.find(id="woocommerce-product-search-field-0")

# # get the first <h1> element
# # on the page
# h1_element = soup.find("h1")

# # find the first element on the page
# # with "search_field" class 
# search_input_element = soup.find(class_="search_field")

# # find the first element on the page
# # with the name="s" HTML attribute
# search_input_element = soup.find(attrs={"name": "s"})

# # find the first element identified
# # by the "input.search-field" CSS selector
# search_input_element = soup.select_one("input.search-field")

# h1_title = soup.select_one(".beta.site-title").getText()
# print(h1_title)


#venosaur_element = soup.find(class_="post-730") 

# extracting data from the nested nodes
# extracting data from the nested nodes
## inside the Venosaur product element
#venosaur_image_url = venosaur_element.find("img")["src"]
#venosaur_price = venosaur_element.select_one(".amount").get_text()
#
#print(venosaur_image_url)
#print(venosaur_price)
#
#
#wartortle_element = soup.find(class_="post-735") 
#wartortle_image_url = wartortle_element.find("img")["src"]
#wartortle_price = wartortle_element.select_one(".amount").get_text()
#wartortle_url = wartortle_element.find("a")["href"]
#wartortle_name = wartortle_element.find("h2").get_text()
#
#print(wartortle_image_url)
#print(wartortle_price)
#print(wartortle_url)
##print(wartortle_name)
##
#
#response = requests.get("https://scrapeme.live/shop/Charizard/")
#soup = BeautifulSoup(response.content, "html.parser")
#
#additional_info_div = soup.select_one(".woocommerce-Tabs-panel--additional_information")
#print(additional_info_div.prettify())
#
## get the table contained inside the 
## "Additional Information" div
#additional_info_table = additional_info_div.find("table")
#
## iterate over each row of the table
#for row in additional_info_table.find_all("tr"):
#    category_name = row.find("th").get_text()
#    cell_value = row.find("td").get_text()
#    print(category_name, cell_value)
#

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
