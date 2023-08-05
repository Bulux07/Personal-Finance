import csv
import gspread
import time
#we need a timer because google only lets us pass in information every other second 

#We just change this to switch from different csv files
MONTH = 'july'
#no need to change the file name it knows because month is being change
file= f"bofa_{MONTH}.CSV"
#a list of all the transactions, dates, amount and category
transactions = []


def chase_fin(file):
#This is the way my bank is setup
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[1]
            amount = float(row[2])
            transaction = ((date, name, amount))
            print (transaction)
            transactions.append(transaction)
        return transactions


sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = chase_fin(file)

for row in rows:
    wks.insert_row([row[0],row[1],row[2]],8)
    time.sleep(2)
