#1 
#2 

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

