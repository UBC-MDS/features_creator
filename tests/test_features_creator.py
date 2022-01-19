

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

    