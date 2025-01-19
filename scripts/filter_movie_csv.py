import argparse
import pandas as pd


"""(str) -> NoneType
Drops duplicate entries from csv file based on Title column.
Writes uniform randomly sampled filtered 600 entries to 'sample_600.csv'.
"""
def filter(csv_file):
    df = pd.read_csv(csv_file)
    
    df["Title"] = df["Title"].str.strip().str.lower()
    df["Title"] = df["Title"].str.replace('“', '"').str.replace('”', '"')
    df["Title"] = df["Title"].str.replace('‘', '"').str.replace('’', '"')
    df["Title"] = df["Title"].str.replace('`', '"').str.replace('´', '"')
    df["Title"] = df["Title"].str.replace("'", '"')
    df = df.drop_duplicates(subset=["Title"])
    df = df.drop_duplicates(subset=["Summary"])
    
    df = df.sample(n=600)
    df.to_csv("sample_600.csv", index=False)

"""
Accepts CLI text-streamed csv file name as input file to be filtered.
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_file", required=True, type=str, default="output", help="Input name of .csv file to filter.")
    args = parser.parse_args()
    
    filter(args.csv_file)

if __name__ == "__main__":
    main()
