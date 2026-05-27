import pandas as pd


def load_data():
    path = "telecom_customer_churn_dataset.xlsx"

    df = pd.read_excel(path)

    return df