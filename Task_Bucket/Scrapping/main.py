from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup

app = FastAPI()

class ProductRequest(BaseModel):
    url: str

@app.post("/scrape")
async def scrape_product(request: ProductRequest):
    try:
        response = requests.get(request.url)
        response.raise_for_status()  # Check if the request was successful

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title_element = soup.find('span', {'class': 'VU-ZEz'})
        title = title_element.get_text() if title_element else 'Not Available'

        # Extract brand
        brand_element = soup.find('span', {'class': 'mEh187'})
        brand = brand_element.get_text() if brand_element else 'Not Applicable'

        # Extract price
        price_element = soup.find('div', {'class': 'Nx9bqj CxhGGd'})
        price = price_element.get_text() if price_element else 'Not Available'

        # Check stock availability
        stock_button = soup.find('button', {'class': 'QqFHMw vslbG+ _3Yl67G _7Pd1Fp'})
        stock_availability = 'In Stock' if stock_button else 'Out of Stock'

        return {
            "Title": title,
            "Brand": brand,
            "Price": price,
            "Stock Availability": stock_availability
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
