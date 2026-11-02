#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot posts of a subreddit.

    Uses the 'after' pagination token and calls itself for each page.
    Returns None if the subreddit is invalid or has no results.
    """
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return hot_list if hot_list else None
        data = response.json().get("data", {})
    except Exception:
        return hot_list if hot_list else None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list if hot_list else None
