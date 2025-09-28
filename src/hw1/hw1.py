from multiprocessing.forkserver import write_signed
import httpx
from numpy import record
import pandas as pd
import numpy as np

import constants as consts


def hw1_solutions():
    print("### HW1 SOLUTIONS ####")
    file_name = consts.DATA_FOLDER / "hw1_car_fuel_efficiency.csv"

    # check if the file already exists
    if file_name.exists():
        print("Download skipped, file already exists.")
    else:
        data_url = "https://raw.githubusercontent.com/alexeygrigorev/datasets/master/car_fuel_efficiency.csv"

        with httpx.Client(timeout=30.0) as client:
            res = client.get(data_url)

            with open(file_name, "wb") as f:
                f.write(res.content)

    df = pd.read_csv(file_name)
    print(df.columns)
    print(df.describe())
    print(df.count())

    # Answers
    answers = {}

    # Q1: Pandas version
    answers["q1"] = pd.__version__

    # Q2: Record count
    record_count = df.shape[0]
    answers["q2"] = record_count

    # Q3: Distinct fuel types
    unique_fuel_count = df["fuel_type"].unique()
    answers["q3"] = unique_fuel_count.shape[0]

    # Q4: Column count with missing values
    cols_w_na_stat = df.count() != record_count
    cols_w_na_count = cols_w_na_stat.sum()
    answers["q4"] = int(cols_w_na_count)

    # Q5: Max fuel_efficiency from Asia
    max_stats = df.groupby(by=["origin"]).max()
    answers["q5"] = float(round(max_stats.loc["Asia", "fuel_efficiency_mpg"], 2))

    # Q6: Horsepower median before and after
    horsepower_median_raw = df["horsepower"].median()
    horsepower_mode_raw = df["horsepower"].mode()
    horsepower_filled_na = df["horsepower"].fillna(horsepower_mode_raw)
    horsepower_median_new = horsepower_filled_na.median()
    horsepower_mode_new = horsepower_filled_na.mode()
    print(horsepower_median_raw)
    print(horsepower_mode_raw)
    print(horsepower_median_new)
    print(horsepower_mode_new)

    answers["q6"] = horsepower_median_raw != horsepower_median_new

    # Q7: Sum of weights
    df_cars_asia = df[df["origin"] == "Asia"]
    df_cars_asia = df_cars_asia[["vehicle_weight", "model_year"]][:7]
    print(df_cars_asia)

    X = df_cars_asia.to_numpy(copy=True)
    print(X)

    XTX = X.T.dot(X)
    print(XTX)

    XTX_inv = np.linalg.inv(XTX)

    print(XTX_inv)

    y = [1100, 1300, 800, 900, 1000, 1100, 1200]

    w = XTX_inv.dot(X.T).dot(y)

    w_sum = w.sum()

    print(w_sum)

    print(answers)
