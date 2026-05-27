def yearly_revenue(df):

    revenue = (df["Monthly_Bill"].sum()* 12)

    print("\nYearly Revenue:",revenue)


def customer_loyalty(df):

    loyalty = (df["Tenure_Months"].mean())
    print("\nCustomer Loyalty:",loyalty)


def churn_score(df):

    scores = []

    for _, row in df.iterrows():

        score = 0

        if row["Support_Calls"] > 5:
            score += 30

        if row["Monthly_Bill"] > 150:
            score += 40

        if row["Tenure_Months"] < 12:
                score += 30

        scores.append(score)

    df["Score"] = scores

    print(df[["Customer_ID","Score"]])