
import streamlit as st
# HEADER SECTION
def app_header():
    st.markdown("""
        <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            padding: 10px 0;
        }
        .subtitle {
            font-size: 20px;
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        <div class="main-title">💼 E & G Accounting Tools</div>
        <div class="subtitle">Your trusted tools for smart money decisions</div>
    """, unsafe_allow_html=True)
# calling header
app_header()

def treasury_bill():
    st.header("Treasury Bill Calculator")
    amount = st.number_input("Enter amount invested (GHS)", min_value=0.0)
    t_bill_days = st.selectbox("Choose Treasury Bill Type", [91, 182, 364])
    rates = {91: 15.0606, 182: 15.2438, 364: 15.8464}
    rate = rates[t_bill_days]

    if st.button("Calculate Treasury Bill"):
        interest = (rate / 100 + 1) ** (t_bill_days / 365)
        total = amount * interest
        st.success(f"Interest Return: GHS {total - amount:,.2f}")
        # st.info(f"Total Return after {t_bill_days} Days: GHS {round(total, 2)}")
        st.info(f"Total Return after {t_bill_days} Days: GHS {total:,.2f}")


def vat_flat():
    st.header("VAT Flat Rate Calculator")
    amount = st.number_input("Enter base amount (GHS)", min_value=0.0)
    if st.button("Calculate VAT Flat"):
        vat = amount * 0.03
        st.success(f"VAT (3%): GHS {round(vat, 2)}")
        st.info(f"Total incl. VAT: GHS {round(amount + vat, 2)}")


def vat_standard():
    st.header("VAT Standard Rate Calculator")
    amount = st.number_input("Enter amount (GHS)", min_value=0.0)
    if st.button("Calculate VAT Standard"):
        vat = amount * 0.125
        nhil = amount * 0.025
        getfund = amount * 0.025
        covid = amount * 0.01
        total_tax = vat + nhil + getfund + covid
        st.success(f"Total VAT: GHS {round(total_tax, 2)}")
        st.info(f"Total incl. VAT: GHS {round(amount + total_tax, 2)}")


def paye():
    st.header("PAYE Calculator")
    salary = st.number_input("Enter gross monthly salary (GHS)", min_value=0.0)
    if st.button("Calculate PAYE"):
        tax = 0
        prev = 0
        brackets = [
            (494, 0.00),
            (656, 0.05),
            (3124, 0.10),
            (6000, 0.175),
            (10000, 0.25),
            (float("inf"), 0.30)
        ]
        for limit, rate in brackets:
            if salary > prev:
                band = min(limit, salary) - prev
                tax += band * rate
                prev = limit
        st.success(f"PAYE Tax: GHS {round(tax, 2)}")
        st.info(f"Net Salary: GHS {round(salary - tax, 2)}")


def ssnit():
    st.header("SSNIT Calculator")
    salary = st.number_input("Enter monthly basic salary (GHS)", min_value=0.0)
    if st.button("Calculate SSNIT"):
        ssnit_value = salary * 0.055
        st.success(f"SSNIT (5.5%): GHS {round(ssnit_value, 2)}")


def loan():
    st.header("Loan Calculator")
    principal = st.number_input("Loan Amount (GHS)", min_value=0.0)
    rate = st.number_input("Interest Rate (%)", min_value=0.0)
    duration = st.number_input("Loan Duration (Years)", min_value=0.0)
    if st.button("Calculate Loan"):
        interest = (principal * rate * duration) / 100
        total = principal + interest
        monthly = total / (duration * 12)
        st.success(f"Monthly Payment: GHS {round(monthly, 2)}")
        st.info(f"Total Repayment: GHS {round(total, 2)}")


def wht():
    st.header("Withholding Tax Calculator")
    amount = st.number_input("Amount Paid (GHS)", min_value=0.0)
    if st.button("Calculate Withholding Tax"):
        wht = amount * 0.075
        net = amount - wht
        st.success(f"WHT (7.5%): GHS {round(wht, 2)}")
        st.info(f"Net Payment: GHS {round(net, 2)}")


# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Select Calculator",
    (
        "Treasury Bill",
        "VAT Flat",
        "VAT Standard",
        "PAYE",
        "SSNIT",
        "Loan",
        "Withholding Tax"
    )
)

# Page Router
if menu == "Treasury Bill":
    treasury_bill()
elif menu == "VAT Flat":
    vat_flat()
elif menu == "VAT Standard":
    vat_standard()
elif menu == "PAYE":
    paye()
elif menu == "SSNIT":
    ssnit()
elif menu == "Loan":
    loan()
elif menu == "Withholding Tax":
    wht()


# Backend calculations
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
        <div style="text-align: center; font-size: 14px; color: white;">
            Developed by <strong>Kemma Solutions</strong><br>
            📧 <a href="mailto:kemma@example.com" style="color: gray;">kemma@example.com</a><br>
            🔗 <a href="https://www.linkedin.com/company/kemma-solutions" target="_blank" style="color: gray;">LinkedIn</a> | 
            <a href="https://twitter.com/kemma_solutions" target="_blank" style="color: gray;">Twitter</a><br><br>
            &copy; 2025 All Rights Reserved.
        </div>
    """, unsafe_allow_html=True)
# calling footer
app_footer()
