# csv_practice.py
# Author: Trenton Shipe
# Module 12 Lab: Read a Sales CSV, write a Cleaned Report

# Reflection Questions
#1. Python lets me write the steps once and rerun them on any file with the same layout, while Excel is faster for quick checks, formatting, and charts.
#2. A brokerage could log every executed trade in an append-mode file, since append mode adds a new line each time without erasing the earlier history.  


import csv
from datetime import datetime
import os
from turtle import write

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SALES_FILE = os.path.join(BASE_DIR, "data", "sales.csv")
CLEANED_FILE = os.path.join(BASE_DIR, "data", "cleaned.csv")
LOG_FILE = os.path.join(BASE_DIR, "data", "log.txt")

print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("--- Exercise 2 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader) # Skip the header row
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("--- Exercise 4 ---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, quantity_str = row #unpacking
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

        
print("--- Exercise 5 ---")

high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for row in reader:
        rows_read += 1
        product, price_str, quantity_str = row
        price = float(price_str)
        quantity = int(quantity_str)
        total = price * quantity
        if total > 100:
            high_value.append((product, f"${price:.2f}", quantity, f"${total:.2f}"))

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    writer.writerows(high_value)

print(f"Wrote {len(high_value)} of {rows_read} rows to cleaned.csv")  



print("--- Exercise 6 ---")

dict_total = 0 
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total sales: ${dict_total:.2f}")


print("--- Exercise 7 ---")
summary = {}

with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = row["product"]
            total = float(row["price"]) * int(row["quantity"])
            summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--- Exercise 8 ---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")