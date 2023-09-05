import csv
import json

# pull in the csv - for now, just using test file in project, will need to implement importing one
imported_csv = '/Users/sarah/Desktop/Development/from-csv-python/stockCsv.csv'
def convert_csv(file):
    csv_file = open(file, 'r', encoding='utf-8-sig')
    json_of_csv = csv.DictReader(csv_file)
    data = [row for row in json_of_csv]
    csv_file.close()

    stocks_for_account = find_stocks_for_account(data, '1')
    return stocks_for_account
    
# parse out the csv
# find all accounts related to the account number
def find_stocks_for_account(data,accountNum):
    for account in data:
        for key, value in account.items():
            if value == accountNum:
                return account
            else:
                return 'No account found'
print(convert_csv(imported_csv))