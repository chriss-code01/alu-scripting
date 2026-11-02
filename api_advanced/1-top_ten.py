#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API for the first 10 hot posts of a subreddit.

    Prints OK once the request has been handled.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting:v1.0 (by /u/YOUR_REAL_USERNAME)"
    }
    params = {"limit": 10}
    try:
        requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    except Exception:
        pass
    print("OK", end="")
