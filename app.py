import streamlit as st
import requests

API_KEY = 'fca_live_0olYR2nWglkV9UnzbAuoI17LlOYfyvo0MV5OSMYA'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "INR", "JPY"]

def convert_currency(base, target, amount):
    url = f"{BASE_URL}&base_currency={base}&currencies={target}"
    try:
        response = requests.get(url)
        data = response.json()
        if target in data['data']:
            converted_amount = data['data'][target] * amount
            return converted_amount
        else:
            st.error("Invalid target currency.")
            st.stop()
    except Exception as e:
        st.error("Error fetching data from the API.")
        st.stop()

st.title("Currency Converter")

base_currency = st.selectbox("Select Base Currency:", CURRENCIES)
target_currency = st.selectbox("Select Target Currency:", CURRENCIES)
amount_to_convert = st.number_input("Enter Amount to Convert:", value=1.00)

if st.button("Convert"):
    converted_amount = convert_currency(base_currency, target_currency, amount_to_convert)
    st.write(f"Converted Amount ({target_currency}): {converted_amount}")
