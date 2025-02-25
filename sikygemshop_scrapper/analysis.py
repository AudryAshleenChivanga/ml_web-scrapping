import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Function to extract numeric price values
def extract_price(price_str):
    match = re.search(r"[\d,\.]+", price_str)
    if match:
        return float(match.group(0).replace(",", ""))
    return None

def main():
    try:
        # Load the scraped data
        df = pd.read_csv("silkygem_prices.csv")
        print("Data loaded successfully from silkygem_prices.csv")

        # Convert price column to numeric values
        df["Price_numeric"] = df["Price"].apply(extract_price)

        # Display summary statistics
        print("\nPrice Summary:")
        print(df["Price_numeric"].describe())

        # Insights:
        cheapest_product = df.loc[df["Price_numeric"].idxmin()]
        most_expensive_product = df.loc[df["Price_numeric"].idxmax()]
        min_price = df["Price_numeric"].min()
        max_price = df["Price_numeric"].max()
        mean_price = df["Price_numeric"].mean()

        print(f"\nCheapest Product: {cheapest_product['Product Name']} with a price of ${cheapest_product['Price']}")
        print(f"Most Expensive Product: {most_expensive_product['Product Name']} with a price of ${most_expensive_product['Price']}")
        print(f"Minimum Price: ${min_price}")
        print(f"Maximum Price: ${max_price}")
        print(f"Mean Price: ${mean_price:.2f}")

        # Visualizations
        plt.figure(figsize=(14, 8))

        # Histogram of Price Distribution
        plt.subplot(2, 3, 1)
        df["Price_numeric"].dropna().hist(bins=15, color="skyblue", edgecolor="black")
        plt.title("Price Distribution")
        plt.xlabel("Price ($)")
        plt.ylabel("Number of Products")

        # Box plot for Price Range
        plt.subplot(2, 3, 2)
        sns.boxplot(data=df["Price_numeric"].dropna(), color="orange")
        plt.title("Price Range (Box Plot)")

        # Price vs Product Name (Top 10 Cheapest Products)
        top_cheapest = df.nsmallest(10, "Price_numeric")
        plt.subplot(2, 3, 3)
        sns.barplot(x="Price_numeric", y="Product Name", data=top_cheapest, palette="Blues_d")
        plt.title("Top 10 Cheapest Products")

        # Price vs Product Name (Top 10 Most Expensive Products)
        top_expensive = df.nlargest(10, "Price_numeric")
        plt.subplot(2, 3, 4)
        sns.barplot(x="Price_numeric", y="Product Name", data=top_expensive, palette="Reds_d")
        plt.title("Top 10 Most Expensive Products")

        # Distribution of Products Above Mean Price
        above_mean = df[df["Price_numeric"] > mean_price]
        plt.subplot(2, 3, 5)
        sns.countplot(x="Price_numeric", data=above_mean, color="lightcoral")
        plt.title("Products Above Mean Price")

        # Overall Price Distribution (Seaborn Histogram)
        plt.subplot(2, 3, 6)
        sns.histplot(df["Price_numeric"].dropna(), bins=20, kde=True, color="green")
        plt.title("Overall Price Distribution with KDE")

        # Save the visualizations to a PNG file
        plt.tight_layout()
        plt.savefig("silkygem_price_analysis.png")  # Save the figure as a PNG file
        print("Visualizations saved as 'silkygem_price_analysis.png'")

        # Show the plots
        plt.show()

    except FileNotFoundError:
        print("Error: CSV file not found. Run the scraper first.")

if __name__ == "__main__":
    main()
