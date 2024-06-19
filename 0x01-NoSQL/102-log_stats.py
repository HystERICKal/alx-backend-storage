#!/usr/bin/env python3
"""Improve task 12."""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Improve task 12."""
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


def print_top_ips(server_collection):
    """Improve task 12."""
    print('IPs:')
    temp_4 = server_collection.aggregate(
        [
            {
                '$group': {'_id': "$temp_7", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for x in temp_4:
        temp_7 = x['_id']
        temp_8 = x['totalRequests']
        print('\t{}: {}'.format(temp_7, temp_8))


def run():
    """Improve task 12."""
    temp_9 = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(temp_9.logs.nginx)
    print_top_ips(temp_9.logs.nginx)


if __name__ == '__main__':
    run()
