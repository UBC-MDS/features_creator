from features_creator import get_matching_column_names
import pandas as pd
import pytest


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
    assert isinstance(get_matching_column_names(test_df, "week_payment"), list)

    # Does not return extra columns
    assert "othercolumn" not in get_matching_column_names(
        test_df, "week_payment")
    assert "week_payment_string7" not in get_matching_column_names(
        test_df, "week_payment")

    # Raises exceptions for wrong types
    with pytest.raises(TypeError):
        get_matching_column_names("FakeDF", "week_payment")
        get_matching_column_names(test_df, [12, 34])

    # Raises an exception for no matches
    with pytest.raises(ValueError):
        get_matching_column_names(test_df, "fake_string")

    # Normal usage test
    assert get_matching_column_names(test_df, "week_payment") == [
        "week_payment1", "week_payment2", "week_payment3"]
