
#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit."""

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
            return

        posts = response.json().get("data", {}).get("children", [])

        for post in posts[:10]:
            print(post.get("data", {}).get("title"))

    except requests.RequestException:
        return

