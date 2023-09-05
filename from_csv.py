import csv
import json
# pull in the csv
imported_csv = '/Users/sarah/Desktop/Development/from-csv-python/stockCsv.csv'
def convert_csv(file):
    csv_file = open(file, 'r', encoding='utf-8-sig')
    json_of_csv = csv.DictReader(csv_file)
    data = [row for row in json_of_csv]
    csv_file.close()

    return data[0]
    

# print(convert_csv(imported_csv))
# parse out the csv

#handle if an account doesn't have 10 stocks

#print out results

#ui