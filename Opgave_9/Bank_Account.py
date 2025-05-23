import logging
import streamlit as st

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Set the title of the Streamlit app
st.title("Bank Account")

# Initialize session state for balance if not already set
if 'balance' not in st.session_state:
    st.session_state.balance = 0.0

# Define the BankAccount class to manage bank account operations
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            logging.info(f"Deposited: ${amount:.2f}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            logging.info(f"Withdrew: ${amount:.2f}")
            return True
        return False

    def get_balance(self):
        return self.balance

# Use st.cache_data to cache the account object
@st.cache_data
def get_account(balance):
    return BankAccount(balance)

# Initialize the bank account with the balance from session state
account = get_account(st.session_state.balance)

# Create a fragment for the deposit section
@st.fragment
def deposit_fragment():
    st.subheader("Deposit Money")
    deposit_amount = st.number_input("Enter amount to deposit", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        if account.deposit(deposit_amount):
            st.success(f"Deposited: ${deposit_amount:.2f}")
            st.success(f"New Balance: ${account.get_balance():.2f}")
            st.session_state.balance = account.get_balance()
            st.rerun()
        else:
            st.error("Invalid deposit amount")

# Display the current balance
st.header("Current Balance")
st.write(f"${account.get_balance():.2f}")

# Call the deposit fragment
deposit_fragment()

# Withdrawal section
st.subheader("Withdraw Money")
withdraw_amount = st.number_input("Enter amount to withdraw", min_value=0.0, format="%.2f")
if st.button("Withdraw"):
    if account.withdraw(withdraw_amount):
        st.success(f"Withdrew: ${withdraw_amount:.2f}")
        st.success(f"New Balance: ${account.get_balance():.2f}")
        # Update session state balance
        st.session_state.balance = account.get_balance()
        # Rerun the script to update the UI with the new balance
        st.experimental_rerun()
    else:
        st.error("Invalid withdrawal amount or insufficient funds")