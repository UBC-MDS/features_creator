import pandas as pd
import numpy as np
import pytest

from features_creator.features_creator import calculate_percentage_change


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
        # Check pattern
        calculate_percentage_change(test_df, ["data_usage"])
        # Check compare_period
        calculate_percentage_change(test_df, "data_usage", compare_period="1, 1")
        # Check time_filter
        calculate_percentage_change(
            test_df, "data_usage", compare_period=(1, 1), time_filter="1, 3"
        )

    # Check Value error
    with pytest.raises(ValueError):
        calculate_percentage_change(test_df, "data_usage", compare_period=(1, 4))
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
