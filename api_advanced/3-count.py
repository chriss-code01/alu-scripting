#!/usr/bin/python3
"""Module that recursively counts keywords in the titles of hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Matching is case-insensitive and whole-word (split on spaces).
    Duplicate keywords in word_list are summed. Sorted by count
    descending, then alphabetically. Prints nothing if invalid.
    """
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/your_username)"}
    params = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            counts[token] = counts.get(token, 0) + 1

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    words = [word.lower() for word in word_list]
    results = {}
    for word in set(words):
        total = counts.get(word, 0) * words.count(word)
        if total > 0:
            results[word] = total
    for word, total in sorted(results.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
