def add_col(x,list):
    """
    params x is a dataframe
    and list is a list

    function takes list and adds it as a new column to the dataframe
    """
    list = pd.Series(list)
    pd.concat([x,list], axis=1)