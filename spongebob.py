import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup


# download the target page
response = requests.get("https://en.wikipedia.org/wiki/List_of_SpongeBob_SquarePants_episodes")


# parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")
episode_table = soup.select_one(".wikitable.plainrowheaders.wikiepisodetable")#esta es la clase que tiene la tabla

# skip the header row
for row in episode_table.find_all("tr")[1:]:
    # to store cell values
    cell_values = []

    # get all row cells
    cells = row.find_all("td")
    # iterating over the list of cells in
    # the current row
    for cell in cells:
        # extract the cell content
        cell_values.append(cell.get_text())

    print("; ".join(cell_values))

