from pandas import DataFrame
# TODO helper function from assignment


def add_state_names_column(my_df):
    """
    add a column of corresponding state names to a dataframe
    params (my_df) a dataFrame with a column called "abbrev"
    Return a copy of original df with extra column
    """
    new_df = my_df.copy()
    names_map = {"CA": "California", "CO": "Colorado", "CT": "Conn"}

    new_df["name"] = new_df["abbrev"].map(names_map)
    return my_df
if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT"]})
    print(df)

    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
