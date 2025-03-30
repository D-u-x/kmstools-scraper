import requests
from bs4 import BeautifulSoup
import csv
import json
import time

# Change User-Agent to avoid 403 Forbidden error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
# Set website URL that need to be scraped
basic_url = "https://skg4w4.a.searchspring.io/api/search/search.json" \
            "?ajaxCatalog=v3" \
            "&resultsFormat=native" \
            "&siteId=skg4w4" \
            "&domain=https%3A%2F%2Fwww.kmstools.com%2Fhand-tools.html" \
            "&bgfilter.category_hierarchy=Hand%20Tools"

# Function to get page data
def get_page_data(page_number):
    url = f"{basic_url}&page={page_number}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Request was successful for page", page_number)
        return response.json()
    else:
        print("Request failed with status code:", response.status_code)
        return None


# Function to extract items from the page data
def get_items(data):
    items = data.get("results", [])
    first_half_url = "https://www.kmstools.com"
    items_data = []
    for item in items:
        item_data = {
            "name": item.get("name"),
            "price": item.get("price"),
            "item_code": item.get("sku"),
            "in_stock": item.get("ss_in_stock"),
            "url": first_half_url + item.get("url"),
            "image_url": item.get("imageUrl"),
        }
        items_data.append(item_data)
    return items_data


def init_csv_file():
    # Create a CSV file and write the header to it
    with open("kmstools_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        filenames = ["name", "price", "item_code", "in_stock", "url", "image_url"]
        writer = csv.DictWriter(csvfile, fieldnames=filenames)
        writer.writeheader()
    print("CSV file initialized successfully")

# Function to append data to CSV file
def append_to_csv(items):
    # Open a CSV file and write the data to it
    with open("kmstools_data.csv", "a", newline="", encoding="utf-8") as csvfile:
        filenames = ["name", "price", "item_code", "in_stock", "url", "image_url"]
        writer = csv.DictWriter(csvfile, fieldnames=filenames)
        for item in items:
            writer.writerow(item)
    print("Data has been written to kmstools_data.csv")


# Function to write or append data to JSON file
def whrite_to_json(items):
    # Create a JSON file and write the data to it
    with open("kmstools_data.json", "a", encoding="utf-8") as jsonfile:
        for item in items:
            jsonfile.write(json.dumps(item, ensure_ascii=False, indent=4) + "\n")
    print("Data has been written to kmstools_data.json")


# Send GET request to the website
response = requests.get(basic_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful")
    # Get the total number of pages from the response
    pages_amount = response.json().get("pagination", {}).get("totalPages", 0)
    print("Total pages:", pages_amount)
    # Initialize CSV file
    init_csv_file()
    # Loop through each page and get data
    for i in range(1, pages_amount + 1):
        # Get data for each page
        page_data = get_page_data(i)
        if page_data:
            # Extract items from the page data and write to CSV and Json
            append_to_csv(get_items(page_data))
            whrite_to_json(get_items(page_data))
            print(f"Page {i} data retrieved successfully")
            # Sleep for 1 second to avoid overwhelming the server
            time.sleep(1)
else:
    print("Request failed with status code:", response.status_code)

