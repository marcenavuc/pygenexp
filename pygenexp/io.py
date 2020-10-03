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
    assert ndf_file.endswith('.ndf'), "You must specify the path to the .ndf file"
    assert os.path.exists(ndf_file), ".ndf file does not exist"
    for xys_file in xys_files:
        assert xys_file.endswith('.xys'), "You must specify the path to the .xys files"
        assert os.path.exists(xys_file), "One of the .xys files does not exist"
    new_df = pd.DataFrame()
    ndf_df = pd.read_csv(ndf_file, sep=sep)

    assert ("SEQ_ID" in ndf_df), ".ndf file must contain 'SEQ_ID' column"
    new_df["id"] = ndf_df["SEQ_ID"]

    for xys in xys_files:
        xys_df = pd.read_csv(xys, sep=sep, skiprows=1)  # TO DO: add param
        assert ("SIGNAL" in xys_df), ".xys file must contain 'SIGNAL' column"
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


