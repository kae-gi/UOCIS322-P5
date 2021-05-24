"""
Nose tests for project, specifically testing the insertion and retrieval of
fields put into the database.
"""
import nose    # Testing framework
from pymongo import MongoClient
import os

client = MongoClient('mongodb://'+os.environ['MONGODB_HOSTNAME'],27017)
db=client.brevetsdb

def test_insert_retrieve_empty():
    db.brevetsdb.remove({})
    retrieved = db.brevetsdb.find_one({'a':1})
    assert retrieved == None


def test_insert_retrieve_single():
    db.brevetsdb.remove({})
    db.brevetsdb.insert_one({'a':1, 'b':2, 'c':3})
    retrieved = db.brevetsdb.find_one({'a':1, 'b':2, 'c':3})
    assert retrieved['a'] == 1
    assert retrieved['b'] == 2
    assert retrieved['c'] == 3
