import csv
def dicter(filename):
    with open(f"data/{filename}") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect=dialect)
        dicte = list(reader)
        return dicte