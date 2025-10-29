import requests  
import json      

API_KEY = "a8d02aaa1a3ae56c1c6f96a5"  

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}?api_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = json.loads(response.text)

        if 'rates' in data:  
            return data['rates'][to_currency]
        else:
            raise ValueError("Key 'rates' not found in API response")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        exit()  
    except (KeyError, ValueError) as e:
        print(f"Data error: {e} (check currencies or API key)")
        exit()

amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g. USD): ").upper()
to_curr = input("To currency (e.g. EUR): ").upper()

rate = get_exchange_rate(from_curr, to_curr)
converted = amount * rate
print(f"{amount} {from_curr} = {converted:.2f} {to_curr}")
