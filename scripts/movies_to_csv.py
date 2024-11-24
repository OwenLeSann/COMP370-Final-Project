import csv
import argparse
import requests
from datetime import datetime, timedelta


def fetch_films(date_range, number_of_calls, movies, output_file, api_key):
    URL = "https://api.newscatcherapi.com/v2/search"
    
    headers = {
        "x-api-key": api_key
    }
    
    params = {
        "q": " OR ".join(movies),
        "from": date_range[0].strftime("%Y-%m-%d"),
        "to": date_range[1].strftime("%Y-%m-%d"),
        "lang": "en",
        "page_size": number_of_calls
    }
    
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        exit(f"HTTP Error: {e}")
    
    if response.status_code == 200:
        data = response.json()
        with open(output_file, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Author", "Published Date", "Link", "Summary"])
            
            for article in data.get("articles", []):
                title = article.get("title", "title unavailable")
                author = article.get("author", "author unavailable")
                published_date = article.get("published_date", "published date unavailable")
                link = article.get("link", "link unavailable")
                summary = article.get("summary", "summary unavailable")
                
                matching_movies = [movie for movie in movies if movie.lower() in title.lower()]

                if len(matching_movies) == 1:
                    writer.writerow([title, author, published_date, link, summary])

    else:
        exit(f"Error: {response.status_code}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--date_range_days", type=int, default=28, help="Specify number of days to look back and ahead of for aticles published on movie_date. The default is 28.")
    parser.add_argument("-d", "--movie_date", required = True, type=str, help="Specify date YYYY-MM-DD of movie to center date range in search.")
    parser.add_argument("-o", "--output", type=str, default="movies", help="Specifies name of [output].csv file.")
    parser.add_argument("-n", "--number_of_calls", type=int, default=10, help="Specifies the number of API calls. The default is 10.")
    parser.add_argument("-m", "--movies", required=True, type=str, nargs="+", help="List of movies to search for articles for.")
    parser.add_argument("-k", "--api_key", required=True, type=str, help="API key for call.")
    
    args = parser.parse_args()
    
    try:
        movie_date = datetime.fromisoformat(args.movie_date).date()
        lower_bound_date = movie_date - timedelta(days=args.date_range_days)
        upper_bound_date = movie_date + timedelta(days=args.date_range_days)
        
        if lower_bound_date < datetime.now().date() - timedelta(days=180) or upper_bound_date > datetime.now().date():
            raise ValueError("Lookback days must be in the range [today - 180 days, today].")
      
    except Exception as e:
        exit(f"Error: {e}. Please try again.")  
        
    fetch_films(date_range=(lower_bound_date, upper_bound_date), 
                number_of_calls=args.number_of_calls, 
                movies=args.movies, 
                output_file=f"{args.output}.csv",
                api_key=args.api_key)
    
    
if __name__ == "__main__":
    main()