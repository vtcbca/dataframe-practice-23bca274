# Accessing data from " result.csv" file

import csv

f=open("D:\\sqlite\\csv\\result.csv","r") 
r=csv.reader(f)
for row in r:
    print(row)

f.close()

# Print Total and Percentage of five subjects

import csv

with open("D:\\sqlite\\csv\\result.csv","r") as f:
    row = csv.DictReader(f)
    for r in row:
        r1 = float(r['python'])
        r2 = float(r['oop'])
        r3 = float(r['stat'])
        r4 = float(r['iks'])
        r5 = float(r['mil'])
        total = r1 + r2 + r3 + r4 + r5
        per = total / 5
        print(f"Student ID: {r['student_id']}\t   Name: {r['student_name']}\t   Total: {total}\t    Percentage: {per}")
