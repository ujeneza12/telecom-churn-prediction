def segment(row):

    if row["Monthly_Bill"] > 150:
        return "Premium"

    elif (row["Support_Calls"] > 5 or row["Churn"] == "yes"):
        return "High-Risk"

    return "Standard"


def customer_groups(df):

    df["Customer_Group"] = (df.apply(segment,axis=1))

    print(
        df[
            [
                "Customer_ID",
                "Customer_Group"
            ]
        ]
    )