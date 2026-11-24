import pytest
import pandas as pd

@pytest.fixture
def data():
    """Loads Census Data"""
    df = pd.read_csv("data/census.csv")
    return df

def test_no_empty_cells(data):
    """Checks that the census data has no empty cells."""
    empty_cells = data.isna().sum().sum()
    assert empty_cells == 0, f"Data has {empty_cells} empty cells."


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
