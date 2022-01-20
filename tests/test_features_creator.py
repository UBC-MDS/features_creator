import pandas as pd
import numpy as np
import pytest

from features_creator.features_creator import *


def test_get_matching_column_names():
    """
    Tests the `get_matching_column_names` function.
    Verifies that it raises the correct exceptions, works in
    "normal" usage, and does not return any extra columns.
    """
    test_df = pd.DataFrame({
        "week_payment1": [1, 2, 3],
        "week_payment2": [1, 2, 3],
        "week_payment3": [1, 2, 3],
        "othercolumn": [5, 6, 7],
        "week_payment_string4": [5, 6, 7]
    })

    # Returns the correct type
    assert isinstance(get_matching_column_names(
        test_df, "week_payment"), list), "Returned the wrong data type"

    # Does not return extra columns
    assert "othercolumn" not in get_matching_column_names(
        test_df, "week_payment"), "`othercolumn` was returned"
    assert "week_payment_string7" not in get_matching_column_names(
        test_df, "week_payment"), "`week_payment_string7` was returned"

    # Raises exceptions for wrong types
    with pytest.raises(TypeError):
        get_matching_column_names("FakeDF", "week_payment")
        get_matching_column_names(test_df, [12, 34])

    # Raises an exception for no matches
    with pytest.raises(ValueError):
        get_matching_column_names(test_df, "fake_string")

    # Normal usage test
    assert get_matching_column_names(test_df, "week_payment") == [
        "week_payment1", "week_payment2", "week_payment3"], "Incorrect columns were returned"



test_df = pd.DataFrame({
        "week_payment1": [1.0, 2, 3],
        "week_payment2": [4, 5.0, 6],
        "week_payment3": [7, 8, 9.0],
        "othercolumn": [1, 1, 1]
})

@pytest.mark.parametrize(
    'json',
    (
        ### Check data type of the first argument:data
        {"data": 3.141, "pattern": "week_payment", "check": "TypeErrorInput1"},
        {"data": "test.txt", "pattern": "week_payment", "check": "TypeErrorInput1"},
        {"data": ["list", "of", "words"], "pattern": "week_payment", "check": "TypeErrorInput1"},
        ### Check data type of the second argument:pattern
        {"data": test_df, "pattern": 3.14, "check": "TypeErrorInput2"},
        {"data": test_df, "pattern": pd.DataFrame([]), "check": "TypeErrorInput2"},
        {"data": test_df, "pattern": ["list", "of", "words"], "check": "TypeErrorInput2"},
        ### Check if the dataframe has non-numeric values
        {"data": test_df.astype(str), "pattern": "week_payment", "check": "TypeErrorNumeric"},
        
        ### Check data type of the output
        {"data": test_df, "pattern": "week_payment", "check": "TypeErrorOutput"},
        ### Check accuracy of the output
        {"data": test_df, "pattern": "week_payment", "check": "AccuracyOutput"}
    )
)
def test_calculate_standard_deviation(json):
    
    """Check TypeError raised when input is not data frame."""
    
    if json["check"] == "TypeErrorInput1":
        with pytest.raises(TypeError):
            print(json["data"], json["pattern"])
            calculate_standard_deviation(json["data"], json["pattern"])
            

    if json["check"] == "TypeErrorInput2":
        with pytest.raises(TypeError):
            print(type(json["data"]), json["pattern"])
            calculate_standard_deviation(json["data"], json["pattern"])
            
            
    if json["check"] == "TypeErrorNumeric":
        with pytest.raises(TypeError):
            print(type(json["data"]), json["pattern"])
            calculate_standard_deviation(json["data"], json["pattern"])
            
            
    if json["check"] == "TypeErrorOutput":
        assert isinstance(calculate_standard_deviation(json["data"], json["pattern"]), pd.DataFrame), \
            "Returned the wrong data type, output should be data frame"
            
            
    if json["check"] == "AccuracyOutput":
        # Test if the function return correct value when there is only one element
        assert calculate_standard_deviation(test_df.iloc[0:1, 0:1], "week_payment").values == np.array([[0]]), \
            "Should return [0], if input data frame has only one element"
        # Test if the function return correct value when there is only one column
        assert np.array_equal(calculate_standard_deviation(test_df.iloc[:, 0:1], "week_payment").values, np.array([[0]]*test_df.shape[0])), \
            "Should a column of 0, if input data frame has only one column"
        # Test if the function return correct value 
        assert np.array_equal(calculate_standard_deviation(test_df, "week_payment").values, np.array([[6.], [6.], [6.]])), \
            "The result is not right"
        