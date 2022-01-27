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
        
def test_calculate_percentage_change():
    """Test calculate_percentage_change function"""
    # Create dataset
    test_df = pd.DataFrame(
        {
            "subscriber_id": [1, 2, 3],
            "data_usage1": [5, 10, 15],
            "data_usage2": [20, 10, 10],
            "data_usage3": [25, 10, 5],
            "data_usage4": [15, 20, 25],
        }
    )

    # Raises errors for wrong input type
    with pytest.raises(TypeError):
        # Check df
        calculate_percentage_change([1, 2, 3, 4], "data_usage")

    with pytest.raises(TypeError):
        # Check pattern
        calculate_percentage_change(test_df, ["data_usage"])

    with pytest.raises(TypeError):
        # Check compare_period
        calculate_percentage_change(test_df, "data_usage", compare_period="1, 1")

    with pytest.raises(TypeError):
        # Check time_filter
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 1), time_filter="1, 3"
        )

    # Check Value error
    with pytest.raises(ValueError):
        calculate_percentage_change(test_df, "data_usage", compare_period=(1, 4))

    with pytest.raises(ValueError):
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 1), time_filter=(1, 5)
        )

    # Check return type
    assert isinstance(calculate_percentage_change(test_df, "data_usage"), np.ndarray)

    assert isinstance(
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 1), time_filter=(1, 3)
        ),
        np.ndarray,
    )

    # Check percentage_change return values
    # Value for comparison are calculated manually using a online calculator
    np.testing.assert_allclose(
        calculate_percentage_change(test_df, "data_usage"),
        np.array([-37.5, -33.33333333, -16.66666667]),
    )
    np.testing.assert_allclose(
        calculate_percentage_change(test_df, "data_usage", compare_period=(1, 2)),
        np.array([-77.77777778, 0.0, 100.0]),
    )
    np.testing.assert_allclose(
        calculate_percentage_change(test_df, "data_usage", compare_period=(3, 1)),
        np.array([11.11111111, -50.0, -60.0]),
    )
    np.testing.assert_allclose(
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 2), time_filter=(1, 3, 4)
        ),
        np.array([-75.0, -33.33333333, 0.0]),
    )
    np.testing.assert_allclose(
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 2), time_filter=(4, 2, 1)
        ),
        np.array([-71.42857143, -33.33333333, -14.28571429]),
    )

