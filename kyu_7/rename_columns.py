import pandas as pd


# renaming columns without changing the original input
def rename_columns(df, names):
    df1=df.copy()
    df1.columns = names
    print(df1)
    return df1
