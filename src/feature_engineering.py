import pandas as pd
import numpy as np


def create_basic_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create model-ready Airbnb listing features."""
    df = df.copy()

    if "price" in df.columns:
        df["log_price"] = np.log1p(df["price"])

    if "amenities" in df.columns:
        df["amenities_count"] = (
            df["amenities"]
            .fillna("")
            .astype(str)
            .str.count(",") + 1
        )

    if "availability_365" in df.columns:
        df["availability_rate"] = df["availability_365"] / 365

    if "room_type" in df.columns:
        df["is_entire_home"] = (df["room_type"] == "Entire home/apt").astype(int)

    if "host_since" in df.columns:
        df["host_since"] = pd.to_datetime(df["host_since"], errors="coerce")
        reference_date = pd.Timestamp.today().normalize()
        df["host_experience_days"] = (reference_date - df["host_since"]).dt.days

    return df


def create_classification_target(df: pd.DataFrame, price_col: str = "price") -> pd.DataFrame:
    """Create high-price listing target based on the 75th percentile."""
    df = df.copy()
    threshold = df[price_col].quantile(0.75)
    df["high_price_listing"] = (df[price_col] >= threshold).astype(int)
    return df