# import requests
# from bs4 import BeautifulSoup

# # URL of the product
# url = 'https://www.flipkart.com/godrej-7-kg-5-star-rain-shower-spin-washing-machine-semi-automatic-top-load-grey-white/p/itm8d4974369ec36?pid=WMNGHNFWBHQWGKDS&lid=LSTWMNGHNFWBHQWGKDSUZZTOB&marketplace=FLIPKART&store=j9e%2Fabm%2F8qx&srno=b_1_1&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Semi%20Automatic%20Top%20Load&fm=search-autosuggest&iid=en_hVlTg4p2fWuHBCZztsP5C4rklUR8x7y8bY6SU2Nil7efGyNjNd9U9Egz6ydAd_VwVHFQ07xCI76A6oQ8GLNDMfUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=tx2trlohmo0000001722806482398'

# # Send a GET request
# response = requests.get(url)
# response.raise_for_status()  # Check if the request was successful

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract title
# title_element = soup.find('span', {'class': 'VU-ZEz'})
# title = title_element.get_text() if title_element else 'Not Available'

# # Extract brand
# brand_element = soup.find('span', {'class': 'mEh187'})
# brand = brand_element.get_text() if brand_element else 'Not Applicable'

# # Extract price
# price_element = soup.find('div', {'class': 'Nx9bqj CxhGGd'})
# price = price_element.get_text() if price_element else 'Not Available'

# # Check stock availability
# stock_button = soup.find('button', {'class': 'QqFHMw vslbG+ _3Yl67G _7Pd1Fp'})
# stock_availability = 'In Stock' if stock_button else 'Out of Stock'

# # Print the results
# print(f"Title: {title}")
# print(f"Brand: {brand}")
# print(f"Price: {price}")
# print(f"Stock Availability: {stock_availability}")




import requests
from bs4 import BeautifulSoup

# URL of the product
url = 'https://www.amazon.in/Pampers-Premium-Care-Diapers-Medium/dp/B07F2X8BHM/ref=sr_1_1_sspa?crid=L3M7627TI1NW&dib=eyJ2IjoiMSJ9.DrnWVjdZ1I_Y7tKI6xifyV7PZ18lxbjGALgibRT9xDsn4zkdpVz-bTwCHdEYx3RUpHcKcy9Wr8hLZFhzq-_yt3-eELFrEdOEfI2Dw_mHpoPgH87tVymiditUZiXQhvPRlJ8VjPikpzdpX5SdfJYc_f-UsBrET27l626GY4f7fF-gTvlQQTog1ASR2L3pHEgCvYo8CZGmuyUEBWekacn0k09ZCVBoLYKUcwCxlZd8Pu-ASH2_jnBhYCYbgYzlrMi3sh0lBaEyc-1NBuo-NqTbXVboMsj1geNy71el6t52lV4.PjVip_kpZxwGbl4SrHa1BhJmkK0SQ_LTVDXYnpkamXs&dib_tag=se&keywords=pampers&qid=1722796731&sprefix=pampers%2Caps%2C248&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

# Send a GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title
title = soup.find('span', {'id': 'productTitle'}).get_text().strip()

# Extract brand
brand_element = soup.find('a', {'id': 'bylineInfo'})

if brand_element:
    brand_text = brand_element.get_text().strip()
    if "Visit the" in brand_text and "Store" in brand_text:
        brand = brand_text.replace("Visit the ", "").replace(" Store", "").strip()
    elif "Brand:" in brand_text:
        brand = brand_text.replace("Brand: ", "").strip()
    else:
        brand = brand_text

# Extract price
price = soup.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).get_text()

# Check stock availability
stock_info = soup.select_one("span[id='submit.buy-now-announce']").get_text().strip()


print(f"Title: {title}")
print(f"Brand: {brand}")
print(f"Price: {price}")
print(f"Stock Availability: {True if stock_info else False}")




# # import requests
# # from lxml import html

# # # URL of the page to scrape
# # url = 'https://www.alibaba.com/product-detail/Newest-Z908-2-4G-WIFI-4K_1600608187729.html?spm=a2700.details.you_may_like.3.1df83b78mWU1Yn'

# # # Fetch the page
# # response = requests.get(url)

# # # Parse the HTML
# # tree = html.fromstring(response.content)

# # # Use the XPath to extract the desired element
# # data = tree.xpath('(//div[@class="price-list"])[1]/text()')

# # # Print the extracted data
# # print(data)





# # import requests
# # from lxml import html

# # # URL of the page to scrape
# # url = 'https://www.alibaba.com/product-detail/Newest-Z908-2-4G-WIFI-4K_1600608187729.html?spm=a2700.details.you_may_like.3.1df83b78mWU1Yn'

# # # Fetch the page
# # response = requests.get(url)
# # webpage = response.content

# # # Parse the webpage with lxml
# # tree = html.fromstring(webpage)

# # # Use the XPath to extract the title
# # title = tree.xpath("//div[@class='product-title-container']/h1/text()")

# # # Use the XPath to extract the brand
# # brand = tree.xpath("//div[@class='brand-name']/text()")

# # # Use the absolute XPath to extract the price
# # price = tree.xpath('//strong[@class="normal"]/text()')

# # # Use the XPath to check stock availability
# # stock = tree.xpath("//div[@class='stock-info']/text()")

# # # Output results
# # print('Title:', title[0] if title else 'Title not found')
# # print('Brand:', brand[0] if brand else 'Brand not specified')
# # print('Price:', price[0] if price else 'Price not available')
# # print('Stock Availability:', stock[0] if stock else 'Stock information not available')




# # import requests
# # from bs4 import BeautifulSoup

# # # URL of the product
# # url = 'https://www.alibaba.com/product-detail/Export-Red-Onion-to-India-Bangladesh_1600379178578.html?spm=a2700.galleryofferlist.wending_right.12.167b6622ABNXuw'

# # # Send a GET request
# # response = requests.get(url)

# # # Parse the HTML content
# # soup = BeautifulSoup(response.text, 'html.parser')

# # price_list = soup.find('div', {'class': 'module_price'}).get_text()

# # print(price_list)

# # # Extract title
# # title = soup.find('div', {'class': 'product-title-container'}).get_text().strip()
# # print(title)
