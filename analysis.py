def high_risk_customers(df):

    avg = df["Monthly_Bill"].mean()

    risk = df[
        (df["Churn"] == "yes")
        |
        (df["Support_Calls"] > 5)
        |
        (df["Monthly_Bill"] > avg)
    ]

    print(risk)


def average_bill(df):

    print(
        "\nAverage bill:",
        round(
            df["Monthly_Bill"].mean(),
            2
        )
    )


def high_support(df):

    result = df[
        df["Support_Calls"] > 5
    ]

    print(result)