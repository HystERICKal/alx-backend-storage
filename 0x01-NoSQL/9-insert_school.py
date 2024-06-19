#!/usr/bin/env python3
"""Insert new doc in a collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert new doc in a collection."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
