#!/usr/bin/env python3
"""function that changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name"""
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_one(myquery, newvalues)
