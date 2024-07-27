import pandas as pd
import pytest
from main import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers

def test_compute_monthly_revenue():
    data = pd.DataFrame({
        'order_date': ['2022-01-15', '2022-01-20'],
        'product_price': [100, 200],
        'quantity': [1, 2]
    })
    assert compute_monthly_revenue(data)['2022-01'].item() == 500

def test_compute_product_revenue():
    data = pd.DataFrame({
        'product_name': ['Widget', 'Gadget'],
        'total_price': [300, 200]
    })
    result = compute_product_revenue(data)
    assert result['Widget'] == 300
    assert result['Gadget'] == 200

def test_compute_customer_revenue():
    data = pd.DataFrame({
        'customer_id': [1, 1, 2],
        'total_price': [100, 200, 300]
    })
    result = compute_customer_revenue(data)
    assert result[1] == 300
    assert result[2] == 300

def test_top_customers():
    data = pd.DataFrame({
        'customer_id': [1, 2, 3],
        'total_price': [1000, 500, 300]
    })
    result = top_customers(data, 2)
    assert result.index.tolist() == [1, 2]
    assert result.iloc[0] == 1000
    assert result.iloc[1] == 500

def test_empty_data_handling():
    data = pd.DataFrame()
    assert compute_monthly_revenue(data).empty
    assert compute_product_revenue(data).empty
    assert compute_customer_revenue(data).empty
    assert top_customers(data).empty

@pytest.mark.parametrize("input_data, expected_output", [
    (pd.DataFrame({'order_date': ['2022-02-28'], 'product_price': [50], 'quantity': [2]}), '2022-02'),
    (pd.DataFrame({'order_date': ['2022-03-15'], 'product_price': [75], 'quantity': [4]}), '2022-03')
])
def test_compute_monthly_revenue_parametrized(input_data, expected_output):
    result = compute_monthly_revenue(input_data)
    assert expected_output in result.index

# To Run the test:
    #pytest test_main.py

