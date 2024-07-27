import pandas as pd
from datetime import datetime

def read_data(filepath):
    """Reading the CSV data into a DataFrame."""
    try:
        return pd.read_csv(filepath orders.csv)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return pd.DataFrame()

def compute_monthly_revenue(data):
    """Computing the total revenue for each month."""
    data['order_date'] = pd.to_datetime(data['order_date'])
    data['month'] = data['order_date'].dt.to_period('M')
    data['total_price'] = data['product_price'] * data['quantity']
    return data.groupby('month')['total_price'].sum()

def compute_product_revenue(data):
    """Computing the total revenue generated by each product."""
    return data.groupby('product_name')['total_price'].sum()

def compute_customer_revenue(data):
    """Computing the total revenue generated by each customer."""
    return data.groupby('customer_id')['total_price'].sum()

def top_customers(data, top_n=10):
    """Identifying the top N customers by revenue."""
    customer_revenue = compute_customer_revenue(data)
    return customer_revenue.sort_values(ascending=False).head(top_n)

def main():
    data = read_data('orders.csv')
    if not data.empty:
        print("Monthly Revenue:")
        print(compute_monthly_revenue(data))
        print("\nProduct Revenue:")
        print(compute_product_revenue(data))
        print("\nCustomer Revenue:")
        print(compute_customer_revenue(data))
        print("\nTop 10 Customers:")
        print(top_customers(data))

if __name__ == "__main__":
    main()
