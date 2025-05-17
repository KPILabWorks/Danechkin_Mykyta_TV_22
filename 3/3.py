import csv

weight1 = 0.3
weight2 = 0.7

with open('energy_50.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        expr = f"{weight1} * {row['consumption1']} + {weight2} * {row['consumption2']}"
        total_consumption = eval(expr)
        print(f"{row['station']}: {total_consumption:.2f} kWh")
