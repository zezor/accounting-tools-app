import streamlit as st
def treasury_bill_calculator():
    print("\n--- Treasury Bill Calculator ---")
    print("Treasury Bill Rates in Ghana (April 2025):")
    print(" 91 DAY BILL ----Rate 15.0606%")
    print(" 182 DAY BILL ----Rate 15.2438%")
    print(" 364 DAY BILL ----Rate 15.8464%")

    try:
        amount_invested = float(input("Enter amount to invest (GHS): "))
        T_bill_type = int(input("Enter Treasury Bill type in days (91, 182, 364): "))

        rates = {91: 15.0606, 182: 15.2438, 364: 15.8464}
        if T_bill_type not in rates:
            print("Invalid Treasury Bill Type. Choose 91, 182, or 364.")
            return

        rate = rates[T_bill_type]
        interest_convert = (rate / 100 + 1) ** (T_bill_type / 365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested

        print("\n.......Results......")
        print(f"Principal Amount: GHS {amount_invested}")
        print(f"Treasury Bill Type: {T_bill_type} DAY BILL")
        print(f"Rate: {rate}%")
        print(f"Interest Return: GHS {round(interest_amt, 2)}")
        print(f"Total Return: GHS {round(amt_invest_plus_interest, 2)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


def vat_flat_calculator():
    print("\n--- VAT Flat Rate Calculator ---")
    print("VAT Flat Rate = 3% of total amount")

    try:
        amount = float(input("Enter base amount (GHS): "))
        vat = amount * 0.03
        total = amount + vat

        print("\n.......Results......")
        print(f"Base Amount: GHS {amount}")
        print(f"VAT (3%): GHS {round(vat, 2)}")
        print(f"Total (Incl. VAT): GHS {round(total, 2)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def vat_standard_calculator():
    print("\n--- VAT Standard Rate Calculator ---")
    print("VAT Breakdown (15% Total):")
    print(" - VAT: 12.5%\n - NHIL: 2.5%\n - GETFund: 2.5%\n - COVID Levy: 1%")

    try:
        amount = float(input("Enter base amount (GHS): "))

        vat = amount * 0.125
        nhil = amount * 0.025
        getfund = amount * 0.025
        covid = amount * 0.01
        total_tax = vat + nhil + getfund + covid
        total = amount + total_tax

        print("\n.......Results......")
        print(f"VAT (12.5%): GHS {round(vat, 2)}")
        print(f"NHIL (2.5%): GHS {round(nhil, 2)}")
        print(f"GETFund (2.5%): GHS {round(getfund, 2)}")
        print(f"COVID Levy (1%): GHS {round(covid, 2)}")
        print(f"Total Tax: GHS {round(total_tax, 2)}")
        print(f"Total (Incl. VAT): GHS {round(total, 2)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def paye_calculator():
    print("\n--- PAYE Calculator ---")
    print("Ghana Income Tax Rates (Monthly - 2025):")
    print(" 0 – 494 GHS: 0%\n 494.01 – 656 GHS: 5%")
    print(" 656.01 – 3,124 GHS: 10%\n 3,124.01 – 6,000 GHS: 17.5%")
    print(" 6,000.01 – 10,000 GHS: 25%\n Above 10,000 GHS: 30%")

    try:
        salary = float(input("Enter monthly salary (GHS): "))
        taxable = salary
        tax = 0
        prev_limit = 0

        brackets = [
            (494, 0.00),
            (656, 0.05),
            (3124, 0.10),
            (6000, 0.175),
            (10000, 0.25),
            (float('inf'), 0.30)
        ]

        print("\n.......Tax Breakdown.......")
        for limit, rate in brackets:
            if taxable > prev_limit:
                band = min(taxable, limit) - prev_limit
                band_tax = band * rate
                tax += band_tax
                print(f"GHS {prev_limit + 0.01:.2f} – GHS {limit:.2f}: {rate * 100}% → GHS {band_tax:.2f}")
                prev_limit = limit

        net_salary = salary - tax
        print(f"\nTotal PAYE Tax: GHS {round(tax, 2)}")
        print(f"Net Salary After Tax: GHS {round(net_salary, 2)}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def ssnit_calculator():
    print("\n--- SSNIT Calculator ---")
    try:
        salary = float(input("Enter your monthly basic salary (GHS): "))
        ssnit = salary * 0.055
        print(f"SSNIT Contribution (5.5%): GHS {round(ssnit, 2)}")
    except ValueError:
        print("Please enter a valid number.")


def loan_calculator():
    print("\n--- Loan Repayment Calculator ---")
    try:
        principal = float(input("Loan Amount (GHS): "))
        rate = float(input("Annual Interest Rate (%): "))
        time = float(input("Loan Duration (in years): "))

        interest = (principal * rate * time) / 100
        total_amount = principal + interest
        monthly_payment = total_amount / (time * 12)

        print(f"Interest: GHS {round(interest, 2)}")
        print(f"Total Repayment: GHS {round(total_amount, 2)}")
        print(f"Monthly Payment: GHS {round(monthly_payment, 2)}")
    except ValueError:
        print("Enter valid numbers only.")


def withholding_tax_calculator():
    print("\n--- Withholding Tax Calculator ---")
    try:
        amount = float(input("Enter amount paid for service (GHS): "))
        wht = amount * 0.075
        net = amount - wht
        print(f"Withholding Tax (7.5%): GHS {round(wht, 2)}")
        print(f"Net Payment After Tax: GHS {round(net, 2)}")
    except ValueError:
        print("Invalid input.")

# ============================
# 🧠 Main Menu to Run App
# ============================

def main():
    while True:
        print("\n==== KEMMA'S FINANCIAL CALCULATORS ====")
        print("1. Treasury Bill Calculator")
        print("2. VAT Flat Rate Calculator")
        print("3. VAT Standard Rate Calculator")
        print("4. PAYE Calculator")
        print("5. SNNIT calculator")
        print("6. LOAN calculator")
        print("7. WITHHOLDING TAX calculator")
        print("8. Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            treasury_bill_calculator()
        elif choice == "2":
            vat_flat_calculator()
        elif choice == "3":
            vat_standard_calculator()
        elif choice == "4":
            paye_calculator()
        elif choice == "5":
            ssnit_calculator()
        elif choice == "6":
            loan_calculator()
        elif choice == "7":
            withholding_tax_calculator()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 7.")

# Run the program
if __name__ == "__main__":
    main()
# FOOTER SECTION
def app_footer():
    st.markdown("""
        <hr style="border-top: 1px solid #bbb;">
        <div style="text-align: center; font-size: 14px; color: gray;">
            Developed by <strong>Kemma Solutions</strong><br>
            📧 <a href="mailto:kemma@example.com" style="color: gray;">kemma@example.com</a><br>
            🔗 <a href="https://www.linkedin.com/company/kemma-solutions" target="_blank" style="color: gray;">LinkedIn</a> | 
            <a href="https://twitter.com/kemma_solutions" target="_blank" style="color: gray;">Twitter</a><br><br>
            &copy; 2025 All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)