#!/usr/bin/python3
"""
Contains a function that works with Reddit API
"""
import json
import requests

def number_of_subscribers(subreddit):
    """Function that takes a subreddit and returns the number of subscribers."""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    
    try:
        data = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers=user_agent,
                            allow_redirects=False)
        data.raise_for_status()  # Raises an HTTPError for bad responses
        
        json_data = data.json()
        results = json_data.get("data").get("subscribers")
        return results
    
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        return 0

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))

