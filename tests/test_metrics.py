import pandas as pd

# Load dataset
df = pd.read_csv('/home/tina/my_mini-project/product_sales_analysis/data/product_sales.csv')  

# Define test functions
def test_average_revenue_per_sale():
    avg_revenue_per_sale = df['revenue'].sum() / df['nb_sold'].sum()
    assert avg_revenue_per_sale > 0, "Average revenue per sale should be greater than 0"

def test_conversion_rate():
    conversion_rate = (df['nb_sold'].count() / df['customer_id'].nunique()) * 100
    assert 0 <= conversion_rate <= 100, "Conversion rate should be between 0 and 100%"
