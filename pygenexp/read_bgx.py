import csv
import pandas as pd


def read_bgx(filename):
    meta_data = {}
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter="\t")
        for i, line in enumerate(csv_reader):
            if len(line) > 1:
                meta_data[line[0]] = line[1]
            if line[0] == "[Probes]":
                break

    return meta_data, pd.read_csv(filename, sep="\t", skiprows=i)
