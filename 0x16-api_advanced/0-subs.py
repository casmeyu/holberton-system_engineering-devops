#!/usr/bin/python3
""" Returns the ammount of subscribers to any giver subreddit """
import requests
import json


def number_of_subscribers(subreddit):
    """ Returns number of subscribers or 0 if it fails """
    if subreddit is None:
        return (0)
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url,
                            headers={'User-agent': 'ojitos v0.1'},
                            allow_redirects=False)
    data = json.loads(response.text)
    try:
        data = data['data']['subscribers']
        return(data)
    except Exception as ex:
        return(0)
