from data_loader import load_data

from analysis import *
from segmentation import *
from metrics import *
from churn_model import *


def menu():

    df = load_data()

    while True:

        print("\n========== TELECOM SYSTEM ==========")

        print("1. Identify high-risk customers")
        print("2. Calculate average bills")
        print("3. Detect support calls")
        print("4. Customer segmentation")
        print("5. Yearly revenue")
        print("6. Customer loyalty")
        print("7. Churn prediction score")
        print("8. Run AI churn prediction")
        print("9. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            high_risk_customers(df)

        elif choice == "2":
            average_bill(df)

        elif choice == "3":
            high_support(df)

        elif choice == "4":
            customer_groups(df)

        elif choice == "5":
            yearly_revenue(df)

        elif choice == "6":
            customer_loyalty(df)

        elif choice == "7":
            churn_score(df)

        elif choice == "8":
            run_model(df)

        elif choice == "9":
            break

        else:
            print("Invalid choice")


menu()