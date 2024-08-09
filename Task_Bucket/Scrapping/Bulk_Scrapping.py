# # from bs4 import BeautifulSoup
# # import requests
# # for page_number in range(1,21):
# #     url = f"https://www.amazon.in/s?k=mobile+above+10000&page={page_number}&crid=3F6LBWWE3ABBY&qid=1722799603&sprefix=mobile+abo%2Caps%2C249&ref=sr_pg_{page_number}"

# #     print(url)
# #     # Send a GET request
# #     response = requests.get(url)

# #     # Parse the HTML content
# #     soup = BeautifulSoup(response.text, 'html.parser')

# #     # Extract the product containers
# #     products = soup.find_all('div', {'data-component-type': 's-search-result'})

# #     for product in products:
# #         # Extract title
# #         title = product.find('span', {'class': 'a-text-normal'}).get_text().strip()

# #         # Extract brand
# #         # brand = product.find('span', {'class': 'a-size-base-plus'}).get_text().strip()

# #         # Extract price
# #         price = product.find('span', {'class': 'a-price-whole'}).get_text()

# #         # Check stock availability
# #         # stock_info = product.select_one("span[id='submit.buy-now-announce']").get_text().strip()

# #         print(f"Title: {title}")
# #         # print(f"Brand: {brand}")
# #         print(f"Price: {price}")
# #         # print(f"Stock Availability: {stock_info}")
# #         print("\n")





# from bs4 import BeautifulSoup
# import requests

# for page_number in range(1, 21):
#     url = f"https://www.amazon.in/s?k=mobile+above+10000&page={page_number}&crid=3F6LBWWE3ABBY&qid=1722799603&sprefix=mobile+abo%2Caps%2C249&ref=sr_pg_{page_number}"

#     print(url)
#     try:
#         # Send a GET request
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Extract the product containers
#         products = soup.find_all('div', {'data-component-type': 's-search-result'})

#         for product in products:
#             try:
#                 # Extract title
#                 title = product.find('span', {'class': 'a-text-normal'}).get_text().strip()

#                 # Extract price
#                 price = product.find('span', {'class': 'a-price-whole'}).get_text()

#                 print(f"Title: {title}")
#                 print(f"Price: {price}")
#                 print("\n")

#             except AttributeError as e:
#                 print(f"Error extracting product details: {e}")

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching URL {url}: {e}")





import requests
from bs4 import BeautifulSoup
import time
import random
import json

headers_list = [
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"},
    {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"},
    # Add more user-agents if needed
]

def fetch_url(url):
    retries = 5
    delay = 1  # initial delay in seconds
    for i in range(retries):
        try:
            headers = random.choice(headers_list)
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.content
            else:
                print(f"Error fetching URL {url}: {response.status_code} {response.reason}")
        except requests.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
        print(f"Retry {i+1}/{retries}...")
        time.sleep(delay)
        delay *= 2  # exponential backoff
    return None

def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    items = []
    titles = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")
    prices = soup.find_all("span", class_="a-price-whole")
    for title, price in zip(titles, prices):
        item = {
            "title": title.get_text(strip=True),
            "price": price.get_text(strip=True)
        }
        items.append(item)
    return items

def main():
    base_url = "https://www.amazon.in/s?k=mobile+above+10000&page={page}&crid=3F6LBWWE3ABBY&qid=1722799603&sprefix=mobile+abo%2Caps%2C249&ref=sr_pg_{page}"
    all_items = []
    for page in range(1, 21):  # adjust the range as needed
        url = base_url.format(page=page)
        content = fetch_url(url)
        if content:
            items = parse_content(content)
            all_items.extend(items)
        time.sleep(random.uniform(1, 3))  # random delay between requests
    
    # Save to JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=4)
    print("Data saved to scraped_data.json")

if __name__ == "__main__":
    main()
