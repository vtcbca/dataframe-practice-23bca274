
import pandas as pd
import csv

# Create a list of cricketer
cricketers = [
    (1, "Virat Kohli", "India", 254, 12311),
    (2, "Joe Root", "England", 158, 8249),
    (3, "Kane Williamson", "New Zealand", 151, 6173),
    (4, "Steve Smith", "Australia", 140, 4917),
    (5, "Babar Azam", "Pakistan", 99, 4925),
    (6, "David Warner", "Australia", 128, 5455),
    (7, "Rohit Sharma", "India", 241, 9681),
    (8, "Shakib Al Hasan", "Bangladesh", 100, 4276),
    (9, "Ross Taylor", "New Zealand", 101, 5649),
    (10, "Quinton de Kock", "South Africa", 124, 5047),
    (11, "Jos Buttler", "England", 148, 3954),
    (12, "Tamim Iqbal", "Bangladesh", 213, 7666),
    (13, "Kieron Pollard", "West Indies", 123, 3194),
    (14, "Hashim Amla", "South Africa", 181, 8113),
    (15, "Angelo Mathews", "Sri Lanka", 168, 5835)
]

# Create a CSV file and write the records

with open("D:/sqlite/csv/crick.csv","w",newline='') as f:
    writer = csv.writer(f)
    #header
    writer.writerow(['cid', 'cname', 'country', 'match', 'run'])  
    writer.writerows(cricketers)

# 1.Create dataframe from csv file.

df = pd.read_csv("D:/sqlite/csv/crick.csv")

# 2.Print all records.
df

# 3.Print only first 5 records.
df.head()

# 4.Print only last 5 records.
df.tail()

# 5.Print records from records number 8.
df.iloc[7]

# 6.Change index numbering. start from 100.
df.index = range(100, 100 + len(df))
df

# 7.Add New column "Average" with average value and print all records.
df['Average'] = df['run'] / df['match']
df

# 8.Print only Cname.
df['cname']

# 9.Print Cricketer Name and its Average.
df[['cname','Average']]

# 10.Change column name with "Cid, Cricketer_Name, Match, Run, Average".
df.columns = ['Cid', 'Cricketer_Name', 'Country', 'Match', 'Run', 'Average']
df

# 11.Print those record where cricker play match > 25.
df[df['Match'] > 25]

# 12.Print those record where cricker play match > 25 and country is "India".
(df[(df['Match'] > 25) & (df['Country'] == 'India')])

# 13. Print all those records whose crickert average is more than 30.
df[df['Average'] > 30]

# 14.Print only crickert name whose average > 30.
df[df['Average'] > 30]['Cricketer_Name']

# 15.Print cricket name and country whose average > 30.
df[df['Average'] > 30][['Cricketer_Name', 'Country']]

# Print player records with average. 
df

# Write this data into player.csv file.
df.to_csv("D:/sqlite/csv/player.csv", index=False)
print(" Done ! ")   
