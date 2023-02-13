#!/usr/bin/env python3
""" function that lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """ returns all the document in a collection"""
    return mongo_collection.find({})
