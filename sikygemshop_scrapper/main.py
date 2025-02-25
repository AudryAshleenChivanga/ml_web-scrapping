import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_silkygem():
    url = "https://www.silkygem.com/collections/all"
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/105.0.5195.102 Safari/537.36")
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Error fetching page:", response.status_code)
        return

    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    product_containers = soup.find_all("div", class_="grid-product__content")  # Adjust class if necessary

    for product in product_containers:
        name = product.find("div", class_="grid-product__title")
        price = product.find("div", class_="grid-product__price")

        product_name = name.get_text(strip=True) if name else "N/A"
        product_price = price.get_text(strip=True) if price else "N/A"

        products.append({"Product Name": product_name, "Price": product_price})

    df = pd.DataFrame(products)
    csv_filename = "silkygem_prices.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Scraped data saved to {csv_filename}")

if __name__ == "__main__":
    scrape_silkygem()
