

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


