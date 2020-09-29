def date_mod(x,date):
    """
    param x is a dataframe
    param date is the name of the column containing the date

    function will split dates into multiple columns
    """
    import pandas as pd
    x[date] = pd.to_datetime(x[date], infer_datetime_format=True)
    x['year'] = x[date].dt.year
    x['month'] = x[date].dt.month
    x['day'] = x[date].dt.day

