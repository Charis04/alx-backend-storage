#!/usr/bin/env python3
"""A Cache class."""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class that stores data in a Redis database.

    Attributes:
        _redis (redis.Redis): Redis client instance.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class.
        Creates a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis database using a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The randomly generated key used to store the data.
        """
        key = str(uuid.uuid4())  # Generate a random UUID as a key
        self._redis.set(key, data)  # Store the data in Redis
        return key
