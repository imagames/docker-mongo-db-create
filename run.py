#!/usr/bin/env python3
import os
import sys
from pymongo import MongoClient

config = {}

config['MONGO_URL'] = os.environ.get('MONGO_URL')
config['MONGO_ADMIN_USER'] = os.environ.get('MONGO_ADMIN_USER')
config['MONGO_ADMIN_PASS'] = os.environ.get('MONGO_ADMIN_PASS')
config['MONGO_DB_NAME'] = os.environ.get('MONGO_DB_NAME')
config['MONGO_USER'] = os.environ.get('MONGO_USER')
config['MONGO_PASS'] = os.environ.get('MONGO_PASS')

nonekeys = []
for key, value in config.items():
    if value is None:
        nonekeys.append(key)

if len(nonekeys) != 0:
    print('MISSING ENV VARIABLES:', file=sys.stderr)
    print(",".join(nonekeys), file=sys.stderr)
    exit(1)

client = MongoClient("mongodb://"+config['MONGO_URL'],
                     username=config['MONGO_ADMIN_USER'],
                     password=config['MONGO_ADMIN_PASS'])


db = client[config['MONGO_DB_NAME']]
db.command("createUser", config['MONGO_USER'],
           pwd=config['MONGO_PASS'], roles=["dbOwner"])
