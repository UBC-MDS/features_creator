
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


def calculate_average(df, pattern):
    """[summary]

    Parameters
    ----------
    df : pandas dataframe
        The dataframe to calculate average
    pattern : string
        The prefix of the column names to calculate average. For example,  "week_payment"

    Returns
    ----------
    pandas dataframe
        A dataframe contains average columns

    Raises
    ----------
    TypeError
        If the type of data is not a pandas dataframe or
        if the pattern is not a matching string

    Examples
    ----------
    >>> data = {
        "week_payment1": [1, 2, 3],
        "week_payment2": [1, 2, 3],
        "week_payment3": [1, 2, 3],
        "othercolumn": [5, 6, 7]}
    >>> df = pd.DataFrame(data)
    >>> calculate_average(df, "week_payment")
        ID    week_payment_avg  
        0              1.0
        1              2.0
        2              3.0

    """
    ...
