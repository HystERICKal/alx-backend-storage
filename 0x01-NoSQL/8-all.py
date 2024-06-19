#!/usr/bin/env python3
"""Return a list of all docs in collection."""


def list_all(mongo_collection):
    """Return a list of all docs in collection."""
    return [doc for doc in mongo_collection.find()]
