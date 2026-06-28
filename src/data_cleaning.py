import pandas as pd
import numpy as np


def clean_price_column(series: pd.Series) -> pd.Series:
    """Convert price strings such as '$1,200.00' to numeric values."""
    return (
        series.astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .replace("nan", np.nan)
        .astype(float)
    )


def standardize_boolean(series: pd.Series) -> pd.Series:
    """Convert Inside Airbnb t/f columns to 1/0."""
    return series.map({"t": 1, "f": 0, True: 1, False: 0})


def remove_price_outliers(df: pd.DataFrame, price_col: str = "price") -> pd.DataFrame:
    """Remove non-positive and extreme price values using IQR."""
    df = df.copy()
    df = df[df[price_col].notna()]
    df = df[df[price_col] > 0]

    q1 = df[price_col].quantile(0.25)
    q3 = df[price_col].quantile(0.75)
    iqr = q3 - q1

    lower = max(1, q1 - 1.5 * iqr)
    upper = q3 + 1.5 * iqr

    return df[(df[price_col] >= lower) & (df[price_col] <= upper)]