#!/usr/bin/env python3
"""Write strings to redis."""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Write strings to redis."""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Write strings to redis."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    """Write strings to redis."""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Write strings to redis."""
        temp_1 = '{}:inputs'.format(method.__qualname__)
        temp_2 = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(temp_1, str(args))
        ressult = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(temp_2, ressult)
        return ressult
    return invoker


def replay(fn: Callable) -> None:
    """Write strings to redis."""
    if fn is None or not hasattr(fn, '__self__'):
        return
    temp_4 = getattr(fn.__self__, '_redis', None)
    if not isinstance(temp_4, redis.Redis):
        return
    temp_5 = fn.__qualname__
    temp_1 = '{}:inputs'.format(temp_5)
    temp_2 = '{}:outputs'.format(temp_5)
    temp_6 = 0
    if temp_4.exists(temp_5) != 0:
        temp_6 = int(temp_4.get(temp_5))
    print('{} was called {} times:'.format(temp_5, temp_6))
    temp_7 = temp_4.lrange(temp_1, 0, -1)
    temp_8 = temp_4.lrange(temp_2, 0, -1)
    for x, y in zip(temp_7, temp_8):
        print('{}(*{}) -> {}'.format(
            temp_5,
            x.decode("utf-8"),
            y,
        ))


class Cache:
    """Write strings to redis."""

    def __init__(self) -> None:
        """Write strings to redis."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Write strings to redis."""
        temp_9 = str(uuid.uuid4())
        self._redis.set(temp_9, data)
        return temp_9

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Write strings to redis."""
        temp_10 = self._redis.get(key)
        return fn(temp_10) if fn is not None else temp_10

    def get_str(self, key: str) -> str:
        """Write strings to redis."""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Write strings to redis."""
        return self.get(key, lambda x: int(x))
