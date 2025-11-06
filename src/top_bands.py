#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    uk_top40 = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    print(bands.head())
    print(uk_top40.head())
    bands["Band"] = bands["Band"].str.lower()
    uk_top40["Artist"] = uk_top40["Artist"].str.lower()
    merged_df = pd.merge(uk_top40, bands, left_on="Artist", right_on="Band")
    print(merged_df.head())
    #why is merged_df empty?

    return merged_df


def main():
    top_bands()

if __name__ == "__main__":
    main()
