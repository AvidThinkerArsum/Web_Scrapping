import requests
from bs4 import BeautifulSoup
import csv

def scrape_major_projects():
    url = "https://www.cityoforinda.org/275/Major-Development-Projects"

    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch data from {url}")
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the container for project cards
    project_container = soup.find("div", class_="span8 content-desc")

    # Find all project cards (assuming each project is listed in a div tag with class 'views-row')
    project_cards = project_container.find_all("div", class_="views-row")

    # Create a CSV file to save the data
    with open("major_projects.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name of project", "Description", "Number of units", "Status", "Last update date", "Importance to the city"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # Iterate through each project card and extract relevant information
        for project_card in project_cards:
            name = project_card.find("div", class_="views-field-title").text.strip()
            description = project_card.find("div", class_="views-field-field-description").text.strip()
            num_units = project_card.find("div", class_="views-field-field-number-of-units").text.strip()
            status = project_card.find("div", class_="views-field-field-status").text.strip()
            last_update_date = project_card.find("div", class_="views-field-field-status-date").text.strip()
            importance = project_card.find("div", class_="views-field-field-importance-to-the-city").text.strip()

            # Write the data to the CSV file
            writer.writerow({"Name of project": name, "Description": description, "Number of units": num_units,
                             "Status": status, "Last update date": last_update_date, "Importance to the city": importance})

if __name__ == "__main__":
    scrape_major_projects()
