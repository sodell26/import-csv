import csv
import json

# pull in the csv - for now, just using test file in project, will need to implement importing one
# make the below empty string the path to your file
imported_csv = 'INSTER_FILE_PATH_HERE!!!'
def convert_csv(file):
    csv_file = open(file, 'r', encoding='utf-8-sig')
    json_of_csv = csv.DictReader(csv_file)
    data = [row for row in json_of_csv]
    csv_file.close()

    # stocks_for_account = find_stocks_for_account(data, '1')
    accounts_with_stock = find_accounts_with_stocks(data, 'GOOG')
    return accounts_with_stock
    
# parse out the csv
# find all accounts related to the account number
def find_stocks_for_account(data,accountNum):
    for account in data:
        for key, value in account.items():
            if value == accountNum:
                return account
            else:
                return 'No account found'

def find_accounts_with_stocks(data, stockName):
    accounts = []
    for stock in data:
        for key, value in stock.items():
            if value == stockName:
                accounts.append(stock['account_number'])
            
    return accounts

print(convert_csv(imported_csv))