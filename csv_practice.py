#1 In Python, you can reuse code, unlike Excel, where you often have to copy and paste formulas. This makes Python more efficient for data analysis tasks, as you can write a function once and call it multiple times with different inputs.
#2 A real-world use of append mode in Python is when you want to add new data to an existing log file without overwriting the previous entries. For example, if you're tracking sales transactions, you can open the log file in append mode and write each new transaction to the end of the file, preserving the history of all transactions.

#Exercise 2
import csv
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Exercise 3
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    header=next(reader)
    print("Header: ", header)
    print("-" * 40)
    print("Data Rows: ")
    for row in reader:
        print(row)

#Exercise 4
total = 0.0
totalrevenue = 0.0
with open('data/sales.csv', 'r') as file:
    reader = csv.reader(file)
    header=next(reader)
    for row in reader:
        item=row[0]
        quantity=int(row[2])
        price=float(row[1])
        total=quantity*price
        totalrevenue+=total
        print(f"Item: {item}, Quantity: {quantity}, Price: {price}, Total: ${total:,.2f}")

print(f"Total Revenue: ${totalrevenue:,.2f}")

#Exercise 5
import os
input_file = 'data/sales.csv'
output_file = 'data/cleaned.csv'
original_count = 0
written_count = 0

with open(input_file, mode='r', encoding='utf-8', newline='') as infile, \
    open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    original_header = next(reader)
    writer.writerow(['Product', 'Price', 'Qty', 'Total'])
    for row in reader:
        original_count += 1
        product = row[0]
        qty = float(row[1])
        price = float(row[2])
        total = qty * price
        if total > 100.0:
            writer.writerow([product, price, qty, total])
            written_count += 1

print(f"Original data rows: {original_count}")
print(f"Rows written (> $100): {written_count}")

#Exercise 6
totalrevenue0 = 0.0

with open('data/sales.csv', 'r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        item_name=row['product']
        qty=int(row['quantity'])
        price=float(row['price'])
        line_total=qty*price
        totalrevenue+=line_total
        print(f"Item: {item_name}, Quantity: {qty}, Price: {price}, Total: ${line_total:,.2f}")

print(f"Total Revenue: ${totalrevenue:,.2f}")

# DictReader allows you to access the data in each row by column name instead of index, which can make the code more readable and maintainable.
# Reader just gives you a list of values for each row, and you have to access the values by their index, which can be less clear, especially if the CSV file has many columns.

#Exercise 7
product_totals={}
with open('data/sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product=row['product']
        qty=int(row['quantity'])
        price=float(row['price'])
        line_total=qty*price
        product_totals[product]=product_totals.get(product,0)+line_total

print(f"{'Product':<20} {'Total Revenue':>15}")

for product in sorted(product_totals.keys()):
    print(f"{product:<20} ${product_totals[product]:>14,.2f}")

#Exercise 8
from datetime import datetime

totalrevenue = 0.0
csv_path='data/sales.csv'

with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        quantity=int(row['quantity'])
        price=float(row['price'])
        line_total=quantity*price
        totalrevenue+=line_total

current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file='data/run_log.txt'
os.makedirs(os.path.dirname(log_file), exist_ok=True)
log_entry=f"{current_time} - Total Revenue: ${totalrevenue:,.2f}\n"

with open(log_file, 'a') as log:
    log.write(log_entry)

print(f"Log entry added to {log_file}: {log_entry.strip()}")