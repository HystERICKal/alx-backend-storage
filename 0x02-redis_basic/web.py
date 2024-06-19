#!/usr/bin/env python3
"""Implement an expiring web cache and tracker."""
import redis
import requests
from functools import wraps
from typing import Callable


temp_1 = redis.Redis()
"""Implement an expiring web cache and tracker."""


def data_cacher(method: Callable) -> Callable:
    """Implement an expiring web cache and tracker."""
    @wraps(method)
    def invoker(url) -> str:
        """Implement an expiring web cache and tracker."""
        temp_1.incr(f'count:{url}')
        result = temp_1.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        temp_1.set(f'count:{url}', 0)
        temp_1.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    """Implement an expiring web cache and tracker."""
    return requests.get(url).text