import requests
import pandas as pd
import argparse
from datetime import datetime

def fetch_films(date, range):
    url = "https://api.themoviedb.org/3/discover/movie"
    # Continue filling in this pseudocode
    lower_bound_date = datetime
    upper_bound_date = datetime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--+-date_range_days", type=int, default=28)
    parser.add_argument("-d", "--movie_date", required = True)
    
    args = parser.parse_args()
    
    

if __name__ == "__main__":
    main()