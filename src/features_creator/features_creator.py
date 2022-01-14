def get_matching_column_names(data, pattern):
    """Returns a subset of the columns whose names match the pattern.

    Matching columns are columns whose names start
    with the given pattern and end with an incrementing integer.

    Parameters
    ----------
    data : pandas dataframe
        The dataframe from which to extract columns
    pattern : string
        The prefix of the column names to extract

    Returns
    ----------
    columns : pandas dataframe
        A dataframe consisting of the matching columns

    Raises
    ----------
    TypeError
        If the type of data is not a pandas dataframe or
        if the pattern is not a string

    Examples
    ----------
    >>> data = {
        "week_payment1": [1, 2, 3],
        "week_payment2": [1, 2, 3],
        "week_payment3": [1, 2, 3],
        "othercolumn": [5, 6, 7]}
    >>> df = pd.DataFrame(data)
    >>> get_matching_column_names(df, "week_payment")
        week_payment1  week_payment2  week_payment3
     0              1              1              1
     1              2              2              2
     2              3              3              3

    """
    ...


def calculate_percentage_change(
    df, pattern, compare_period=(2, 2), time_filter=None, changed_name=None
):
    """Calculate percentage change over a time period
    (months over months or weeks over weeks)
    for the given column pattern.

    Use case:
        This function aims to generate features to capture trend
        in data for a given comparison period. Example:
        Telcom - Predict customers who are more likely to decline their revenue next month/week.
        Finance - Predict customers who are going to default next month/week.

    Steps:
        1. Get matching columns for the pattern.

        2. Apply time_filter if available.
        Example: time_filter = (1, 2, 3, 4) filters out columns corresponding to
        weeks 1, 2 , 3 and 4 out of all the weeks available.
        week 1 represent last week data, week 2 last to last week and so on.

        3. Determine start and end comparison period.
        Example: compare_period = (2, 3), corresponds to the percentage for
        last 2 weeks vs previous 3 weeks (with respect to last 2 weeks)

        4. Calculate percentage change between two periods.
        Example: Percentage change of normalized week_payment in last 2 weeks
         vs percentage change in normalized week payment in
         previous 3 weeks (with rest to last 3 weeks)

        5. Change the column name as per changed_name parameter.

    Parameters
    ----------
    df : pandas.DataFrame
        A pandas dataframe
    pattern : str
        A column pattern:
        pay_amt represents pay_amt1, pay_amt2...
    compare_period: tuple
        Comparison period:
        for 2 months over 2 months , compare_period = (2, 2)
    time_filter: tuple
        Time filter (months or weeks) for comparison
    changed_name: str
        Final column name

    Returns
    -----------
    df: pandas.DataFrame
        A dataframe with all the derived features

    Raises
    ----------
    TypeError
        If the type of df is not a pandas dataframe or
        If the pattern is not a string
        If compare_period is not a tuple
        If filter is not a tuple

    Examples
    ----------
    >>> data = {
        "week_payment1": [10, 5, 20],
        "week_payment2": [50, 20, 5]
        }
    >>> df = pd.DataFrame(data)
    >>> calculate_percentage_change(df, "week_payment", (1, 1))
         week_payment1  week_payment2  week_payment_pct_change_1w_1w
     0             10             50                          80.0
     1              5             20                          75.0
     2             20              5                         -300.0
    """

    return
