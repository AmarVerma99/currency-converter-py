import tkinter as tk
from tkinter import ttk

conversion_table = {
    "USD": {
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 109.71,
        "CAD": 1.22,
        "AUD": 1.32,
        "INR": 83.51,  
    },
    "EUR": {
        "USD": 1.18,
        "GBP": 0.85,
        "JPY": 129.67,
        "CAD": 1.47,
        "AUD": 1.59,
        "INR": 88.14
    },
    "GBP": {
        "USD": 1.39,
        "EUR": 1.18,
        "JPY": 151.37,
        "CAD": 1.70,
        "AUD": 1.84,
        "INR": 102.52
    },
    "JPY": {
        "USD": 0.0091,
        "EUR": 0.0077,
        "GBP": 0.0066,
        "CAD": 0.011,
        "AUD": 0.012,
        "INR": 0.67
    },
    "CAD": {
        "USD": 0.82,
        "EUR": 0.68,
        "GBP": 0.59,
        "JPY": 87.47,
        "AUD": 1.08,
        "INR": 57.39
    },
    "AUD": {
        "USD": 0.76,
        "EUR": 0.63,
        "GBP": 0.54,
        "JPY": 81.75,
        "CAD": 0.93,
        "INR": 52.84
    },
    "INR": {
        "USD": 0.013,
        "EUR": 0.011,
        "GBP": 0.0097,
        "JPY": 1.49,
        "CAD": 0.017,
        "AUD": 0.019
    }
}

conversion_history = []

def convert_currency():
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    if base_currency == target_currency:
        converted_amount = amount
    else:
        conversion_rate = conversion_table[base_currency][target_currency]
        converted_amount = amount * conversion_rate

    result_label.config(text=f"{converted_amount:.2f} {target_currency}")

    
    conversion_history.append(f"{amount:.2f} {base_currency} = {converted_amount:.2f} {target_currency}")

def show_history():
    history_window = tk.Toplevel()
    history_window.title("Conversion History")

    history_listbox = tk.Listbox(history_window, width=50, height=10)
    history_listbox.pack(padx=20, pady=20)

    for item in conversion_history:
        history_listbox.insert(tk.END, item)

window = tk.Tk()
window.title("Currency Converter")
window.configure(background='#f0f0f0')

label_font = ('Helvetica', 14)
button_font = ('Helvetica', 12)

label1 = tk.Label(window, text="Amount:", font=label_font, bg='#f0f0f0')
label1.pack()

entry = tk.Entry(window, font=label_font)
entry.pack()

label2 = tk.Label(window, text="Base Currency:", font=label_font, bg='#f0f0f0')
label2.pack()

base_currency_var = tk.StringVar()
base_currency_var.set("USD")

base_currency_menu = tk.OptionMenu(window, base_currency_var, *conversion_table.keys())
base_currency_menu.config(font=label_font)
base_currency_menu.pack()

label3 = tk.Label(window, text="Target Currency:", font=label_font, bg='#f0f0f0')
label3.pack()

target_currency_var = tk.StringVar()
target_currency_var.set("EUR")

target_currency_menu = tk.OptionMenu(window, target_currency_var, *conversion_table.keys())
target_currency_menu.config(font=label_font)
target_currency_menu.pack()

convert_button = tk.Button(window, text="Convert", font=button_font, bg="blue", fg="white", command=convert_currency)
convert_button.pack(pady=10)

history_button = tk.Button(window, text="Show History", font=button_font, bg="green", fg="white", command=show_history)
history_button.pack(pady=10)

label4 = tk.Label(window, text="Converted Amount:", font=label_font, bg='#f0f0f0')
label4.pack()

result_label = tk.Label(window, text="", font=('Helvetica', 16, 'bold'), bg='#f0f0f0', fg='green')
result_label.pack()

window.mainloop()
