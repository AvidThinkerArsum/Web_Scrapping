import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.cityoforinda.org/275/Major-Development-Projects"

content = requests.get(url)
htmlContent = content.content
# print(htmlContent)

# I want to go through each of the projects, open them and then find the key details and lookout for errors.

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(htmlContent, "html.parser")

# Find all <li> elements with class "megaMenuItem"
project_elements = soup.select(".megaMenuItem")

numeric_pattern = r'\b\d+\b'

# Extract and print project names and descriptions
for project_element in project_elements:
    project_name = project_element.select_one(".widgetTitle a").text.strip()
    project_description = project_element.select_one(".widgetDesc").text.strip()

    # Search for numeric values next to the word "units"
    units_matches = re.findall(numeric_pattern + r'\s*units', project_description, re.IGNORECASE)
    
    if units_matches:
        # Extract numeric values from matches and sum them up
        units_values = [int(match.split()[0]) for match in units_matches]
        total_units = sum(units_values)
        
    print("Project Name:", project_name)
    print("Project Description:", project_description)
    print("Project Units")