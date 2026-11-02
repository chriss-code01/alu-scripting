#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ALUStudent/1.0)"
    }

    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts[:10]:
            title = post.get("data", {}).get("title")
            if title:
                print(title)

    except requests.RequestException:
        print(None)


if __name__ == "__main__":
    pass
