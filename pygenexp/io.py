import pandas as pd
import csv
import os
import re


def read_illumnia(filename):
    df = pd.read_csv(filename, sep="\t")
    return df


def read_ngd(filename):
    pass


def read_xys(xys_files, ndf_file, sep="\t"):
    new_df = pd.DataFrame()
    ndf_df = pd.read_csv(ndf_file, sep=sep)
    new_df["id"] = ndf_df["SEQ_ID"]
    for xys in xys_files:
        xys_df = pd.read_csv(xys, sep=sep, skiprows=1)  # TO DO: add param
        new_df[os.path.basename(xys)] = xys_df['SIGNAL']

    return new_df.dropna()


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


