#!/usr/bin/python3
"""
Queries Reddit API.
Prints the titles of the first 10 hot posts for a given subreddit.
"""
import json
import requests

def top_ten(subreddit):
    """Gets the top 10 posts of a subreddit."""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    
    try:
        data = requests.get("https://www.reddit.com/r/{}/hot/.json".format(subreddit),
                            headers=user_agent,
                            allow_redirects=False)
        data.raise_for_status()  # Raises an HTTPError for bad responses
        
        json_data = data.json().get("data").get("children", [])
        
        if not json_data:
            print("None")
            return
        
        for post in json_data[:10]:
            print(post.get("data").get("title"))
    
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

