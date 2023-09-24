import pandas as pd
from pathlib import Path
import os

budget_data = r"C:\Users\ellio\Documents\github\python-challenge\PyBank\Resources\budget_data.csv"

df = pd.read_csv(budget_data)

#The total number of months included in the dataset
len(df.Date.unique())

#The net total amount of "Profit/Losses" over the entire period
df["Profit/Losses"].sum()

greatest_increase = (df["Profit/Losses"].diff() ==df["Profit/Losses"].diff().max())
df[greatest_increase]
df[greatest_increase].Date.iloc[0]

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
df["Profit/Losses"].diff().mean()

#The greatest increase in profits (date and amount) over the entire period
df["Profit/Losses"].diff().max()

#he greatest decrease in profits (date and amount) over the entire period
df["Profit/Losses"].diff().min()

greatest_decrease =(df["Profit/Losses"].diff() ==df["Profit/Losses"].diff().min())
df[greatest_decrease]
df[greatest_decrease].Date.iloc[0]

#combined analysis
print("Total Months:", len(df.Date.unique()))
print("------------------------")
print("Total: $", df["Profit/Losses"].sum())
print("------------------------")
print("Average Change: $", df["Profit/Losses"].diff().mean())
print("------------------------")
print("Greatest Increase: $", df[greatest_increase].Date.iloc[0], df["Profit/Losses"].diff().max())
print("------------------------")
print("Greatest Decrease: $", df[greatest_decrease].Date.iloc[0], df["Profit/Losses"].diff().min())
print("------------------------")


#create a text file with results
output_file = r"C:\Users\ellio\Documents\github\python-challenge\PyBank\analysis\Results.txt"

with open(output_file, "w") as results:
    results.write("Total Months: " + str(len(df.Date.unique())) + "\n")
    results.write("------------------------ \n")
    results.write("Total: $" + str(df["Profit/Losses"].sum()) + "\n")
    results.write("------------------------ \n")
    results.write("Average Change: $" + str(df["Profit/Losses"].diff().mean()) + "\n")
    results.write("------------------------ \n")
    results.write("Greatest Increase: " + str(df[greatest_increase].Date.iloc[0]) + " $" + str(df["Profit/Losses"].diff().max()) + "\n")
    results.write("------------------------ \n")
    results.write("Greatest Decrease: " + str(df[greatest_decrease].Date.iloc[0]) + " $" + str(df["Profit/Losses"].diff().min()) + "\n")
    results.write("------------------------ \n")