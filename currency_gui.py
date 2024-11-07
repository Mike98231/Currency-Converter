import tkinter as tk
from currency_converter import convert_currency

def perform_conversion():
    amount = float(amount_entry.get())
    base_currency = base_currency_entry.get().upper()
    target_currency = target_currency_entry.get().upper()
    result = convert_currency(amount, base_currency, target_currency)
    result_label.config(text=f"{amount} {base_currency} = {result:.2f} {target_currency}")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")

tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="Base Currency:").grid(row=1, column=0)
base_currency_entry = tk.Entry(root)
base_currency_entry.grid(row=1, column=1)

tk.Label(root, text="Target Currency:").grid(row=2, column=0)
target_currency_entry = tk.Entry(root)
target_currency_entry.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()
