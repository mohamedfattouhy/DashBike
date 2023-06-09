"""
This module contains functions for pre-processing data
and using it for visualization
"""

# MANAGE ENVIRONNEMENT
import json
import os
import pandas as pd


def preprocess_json_files(path_to_json_file: str) -> pd.DataFrame:
    """pre-processing data"""

    with open(path_to_json_file, "r") as f:
        data = json.load(f)
        f.close()

    df = pd.DataFrame.from_dict(data)
    df = df[["intensity", "dateObserved", "location", "id"]]

    df["Date"] = df["dateObserved"].str[:10]
    df["Date"] = pd.to_datetime(df["Date"])
    df["week"] = df["Date"].dt.day_name()
    df["Date"] = df["Date"].astype(str)

    df = df.drop(["dateObserved"], axis="columns")

    df["coord"] = df["location"].apply(lambda x: x["coordinates"])
    df = df.drop(["location"], axis="columns")
    df = df.drop_duplicates(["Date"])

    df["id"] = df["id"].str.split("_").str[2]

    df["Date"] = pd.to_datetime(df["Date"])
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")  # iso format

    df[["lon", "lat"]] = pd.DataFrame(df["coord"].tolist(),
                                      columns=["lon", "lat"])

    df = df.drop(["coord"], axis="columns")

    # Delete rows with missing values (NA)
    df = df.dropna()

    df["intensity"] = df["intensity"].astype(int)

    return df


# counters = ['X2H19070220',
#             'X2H20042632',
#             'X2H20042634',
#             'X2H20063162'
#             ]

# counters = ['X2H19070220', 'X2H20042632', 'X2H20042634', 'X2H20063162']


def dict_of_df(counters: list = None) -> dict:
    """
    Put dataframes, each containing counter data, into a dictionary
    """

    if counters is not None:
        counters_list = counters
    else:
        counters_list = [
            'X2H19070220',
            'X2H20042632',
            'X2H20042634',
            'X2H20063162'
            ]

    df_dict = {}

    for counter in counters_list:
        path_to_data = os.path.join("data", "preprocess",
                                    counter + ".json")
        data = preprocess_json_files(path_to_data)
        df = pd.DataFrame(data)
        df_dict[counter] = df

    return df_dict


# counters = ['X2H19070220', 'X2H20042632', 'X2H20042634', 'X2H20063162']
# dict_test = dict_of_df(counters=counters)
