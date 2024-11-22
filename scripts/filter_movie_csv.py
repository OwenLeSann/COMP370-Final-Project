import argparse
import pandas as pd


def filter(csv_file):
    df = pd.read_csv(csv_file)
    df = df.drop_duplicates(subset=["Title"])    
    df.to_csv("sample.csv", index=False)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_file", required=True, type=str, default="output", help="Input name of .csv file to filter.")
    args = parser.parse_args()
    
    filter(args.csv_file)


if __name__ == "__main__":
    main()