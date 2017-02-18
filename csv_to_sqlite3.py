
import argparse
import sqlite3
import csv

def read_csv(csv_file, **kwargs):
    """read_csv(file, **kwargs) -> dict("header" : [rows], ...)
    Reads a CSV document and returns a dictionary object where keys are table
    headers, and the values for it are an array of strings.

    fileobj must have mode = "r"

    kwargs are directly passed to csv.DictReader, see help(csv.DictReader)
    for more info.
    """

    csv_contents = {}
    csv_reader = csv.DictReader(csv_file, **kwargs)

    for entry in csv_reader:
        for column in entry:
            if not column in csv_contents:
                csv_contents[column] = [entry[column]]
            else:
                csv_contents[column].append(entry[column])

    return csv_contents


if __name__ == "__main__":
    pass
