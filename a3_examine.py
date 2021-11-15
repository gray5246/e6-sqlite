import csv
def dicter():
    with open("data/coffees.csv") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect=dialect)
        dict = list(reader)
        print(dict)