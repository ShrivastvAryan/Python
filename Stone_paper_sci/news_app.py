import requests
from datetime import datetime
import json

# Input from user for the type of news
query = input('What type of news are you interested in? ')

# Get today's date in the required format
today_date = datetime.today().strftime('%Y-%m-%d')

# API URL with dynamic date
url = f'https://newsapi.org/v2/everything?q=tesla&from=2025-06-28&sortBy=publishedAt&apiKey=b9abdcdad38b409bb13565836d31f81a'

# Sending GET request to fetch the news
try:
    r = requests.get(url)
    r.raise_for_status()  # Raise an error for bad status codes (4xx, 5xx)

    # Load the response JSON into a dictionary
    news = r.json()

    # Checking if the response contains news articles
    if 'articles' in news:
        print("News articles fetched successfully.")
        for article in news['articles']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}\n")
    else:
        print("No articles found for the given query.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
