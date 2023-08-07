import requests
from bs4 import BeautifulSoup
import csv

def scrape_books():
    url = "http://books.toscrape.com/index.html"

    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all book items on the page (assuming each book is listed in an article tag with class 'product_pod')
    books = soup.find_all("article", class_="product_pod")

    # Create a CSV file to save the data
    with open("scraped_books.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Title", "Price", "Availability", "Rating"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Iterate through each book item and extract relevant information
        for book in books:
            title = book.h3.a["title"]
            price = book.select(".price_color")[0].text.strip("£")
            availability = "In stock" if "In stock" in book.select(".instock.availability")[0].text else "Out of stock"
            rating = "No rating" if "star-rating" not in book.p.attrs["class"] else book.p.attrs["class"][-1]

            # Write the data to the CSV file
            writer.writerow({"Title": title, "Price": price, "Availability": availability, "Rating": rating})

if __name__ == "__main__":
    scrape_books()
