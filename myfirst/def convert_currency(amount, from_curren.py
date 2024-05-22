def convert_currency(amount, from_currency, to_currency):
    # Replace with actual exchange rates
    exchange_rates = {
        "USD": 100,  # Example: 1 USD = 100 RWF
        # Add other currencies and rates here
    }

    if from_currency in exchange_rates and to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[from_currency] / exchange_rates[to_currency]
        return converted_amount
    else:
        return None

# Example usage
amount_to_convert = 100
from_currency_code = "USD"
to_currency_code = "RWF"

converted_amount = convert_currency(amount_to_convert, from_currency_code, to_currency_code)
if converted_amount:
    print(f"{amount_to_convert} {from_currency_code} = {converted_amount:.2f} {to_currency_code}")
else:
    print("Invalid currency codes.")
