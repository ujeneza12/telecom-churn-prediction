from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def run_model(df):

    # Clean churn values to avoid issue incase we have (yes,No)
    df["Churn"] = (
        df["Churn"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({
            "yes": 1,
            "no": 0
        })
    )

    # Remove invalid rows
    df = df.dropna(subset=["Churn"])

    X = df[
        [
            "Monthly_Bill",
            "Support_Calls",
            "Tenure_Months"
        ]
    ]

    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    pred_proba = model.predict_proba(X_test)

    for i in range(len(X_test)):
        churn_probability = pred_proba[i][1]

        print("\n----------------------")
        print(f"Customer {i + 1}")
        print(f"Churn Probability: {churn_probability * 100:.2f}%")

        if churn_probability > 0.7:
            print("Suggested Action: Offer discount + priority support")
        elif churn_probability > 0.4:
            print("Suggested Action: Send engagement campaign")
        else:
            print("Suggested Action: No action needed")