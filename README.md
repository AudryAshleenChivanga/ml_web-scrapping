# Price Analysis for Silkygem Products

## Overview
This project aims to analyze the prices of products scraped from the Silkygem website. The script uses **BeautifulSoup** to scrape product data, processes it, and generates visualizations to provide insights into the pricing structure of the products. The analysis includes the cheapest and most expensive products, as well as various visualizations to highlight price distributions, price ranges, and product price comparisons.

## Steps Performed

1. **Data Scraping**: 
   - We used **BeautifulSoup** to scrape product data from the Silkygem website. This includes extracting the product names and their corresponding prices.

2. **Data Loading**: The script loads a CSV file (`silkygem_prices.csv`) containing the scraped product data.

3. **Data Cleaning**: The price column is processed to extract numerical values from the raw price data using regular expressions. This ensures that the prices are in a format suitable for analysis.

4. **Statistical Analysis**:
   - The script calculates the following statistics for the product prices:
     - Minimum price
     - Maximum price
     - Mean price
   - It also identifies the cheapest and most expensive products based on the price data.

5. **Visualizations**:
   - **Price Distribution**: A histogram showing the distribution of product prices.
   - **Price Range (Box Plot)**: A box plot to visualize the range and spread of product prices.
   - **Top 10 Cheapest Products**: A bar plot showing the 10 cheapest products and their prices.
   - **Top 10 Most Expensive Products**: A bar plot showing the 10 most expensive products and their prices.
   - **Products Above Mean Price**: A count plot to display how many products have a price above the mean price.
   - **Overall Price Distribution with KDE**: A histogram with a kernel density estimate (KDE) to visualize the overall distribution of prices.

6. **Saving Visualizations**: The generated visualizations are saved as a PNG image file (`silkygem_price_analysis.png`) for later reference.

## Requirements
- **Python 3.x**
- **Libraries**:
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `beautifulsoup4`
  - `requests`
  - `re` (regular expressions)

To install the required libraries, use the following command:

```bash
pip install pandas matplotlib seaborn beautifulsoup4 requests
