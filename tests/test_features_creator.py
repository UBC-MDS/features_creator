

import pandas as pd
import numpy as np
import pytest

from features_creator.features_creator import *


@pytest.fixture
def data_df():
    data = {
        "week_payment1": [1.0, 2, 3],
        "week_payment2": [4, 5.0, 6],
        "week_payment3": [7, 8, 9.0],
        "othercolumn": [1, 1, 1]}
    df = pd.DataFrame(data)
    return df


def test_calculate_average(data_df):

    # Test for TypeError
    with pytest.raises(TypeError):
        # check if TypeError is raised when data is not a pandas dataframe
        calculate_average(1, "week_payment")
        # check if TypeError is raised when pattern is not a string
        calculate_average(data_df, 1)
    
    # Test for ValueError
    with pytest.raises(ValueError):
        # check if ValueError is raised when pattern is not a string
        calculate_average(data_df, "")
        # check if ValueError is raised when columns not found
        calculate_average(data_df, "not_a_column")

    # Test for return type
    assert isinstance(calculate_average(data_df, "week_payment"), np.ndarray)

    # Test the function with a dataframe with only one column
    data_1col = {
        "week_payment1": [1, 2, 3]}
    df_1col = pd.DataFrame(data_1col)
    assert np.array_equal(calculate_average(
        df_1col, "week_payment"), np.array([1, 2, 3]))

    # Test the function return correct value when there is only one row
    data_1row = {
        "week_payment1": [1]}
    df_1row = pd.DataFrame(data_1row)
    assert np.array_equal(calculate_average(
        df_1row, "week_payment"), np.array([1]))
    

    # Test the function return correct value 
    assert np.array_equal(calculate_average(
        data_df, "week_payment"), np.array([4, 5, 6]))

