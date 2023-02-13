#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    coll = {}
    for key, value in kwargs.items():
        coll[key] = value
    result = mongo_collection.insert_one(coll)
    return result.inserted_id
