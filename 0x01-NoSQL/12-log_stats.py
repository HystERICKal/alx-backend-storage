#!/usr/bin/env python3
"""Provide some stats about Nginx logs."""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Provide some stats about Nginx logs."""
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    temp_1 = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in temp_1:
        temp_2 = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, temp_2))
    temp_3 = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(temp_3))


def run():
    """Provide some stats about Nginx logs."""
    result = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(result.logs.nginx)


if __name__ == '__main__':
    run()
