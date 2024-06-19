#!/usr/bin/env python3
"""Implement an expiring web cache and tracker."""


import redis
import requests
from functools import wraps

temp_1 = redis.Redis()


def url_access_count(method):
    """Implement an expiring web cache and tracker."""
    @wraps(method)
    def wrapper(url):
        """Implement an expiring web cache and tracker."""
        temp_2 = "cached:" + url
        temp_3 = temp_1.get(temp_2)
        if temp_3:
            return temp_3.decode("utf-8")

        temp_4 = "count:" + url
        temp_5 = method(url)

        temp_1.incr(temp_4)
        temp_1.set(temp_2, temp_5, ex=10)
        temp_1.expire(temp_2, 10)
        return temp_5
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """Implement an expiring web cache and tracker."""
    outcome = requests.get(url)
    return outcome.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
