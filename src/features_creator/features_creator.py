def calculate_standard_deviation(data, cols):
    """Returns a dataframe with standard deviation of specific columns.

    Calculating standard deviation of columns inputed.

    Parameters
    ----------
    data : pandas dataframe
        The dataframe to calculate standard deviation
    cols : list
        The column names to calculate

    Returns
    ----------
    columns : pandas dataframe
        A dataframe with input columns and standard deviation

    Raises
    ----------
    TypeError
        If the type of data is not a pandas dataframe or
        if the cols containes elements not in the dataframe

    Examples
    ----------
    >>> data = {
        "week_payment1": [1, 1, 1],
        "week_payment2": [1, 1, 1],
        "week_payment3": [2, 2, 2],
        "othercolumn": [5, 6, 7]}
    >>> df = pd.DataFrame(data)
    >>> cols = ["week_payment1", "week_payment2", "week_payment3"]
    >>> calculate_standard_deviation(df, cols)
        week_payment1  week_payment2  week_payment3
     0              0              0              0

    """
    ...
