#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:34:06 2018

@author: jasonw
"""

from etherscan.accounts import Account
from  etherscan.proxies import Proxies
#import numpy as np
import json

with open('../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']
    
# get steven's contract initialization input data as a reference
api = Proxies(api_key=key)
transaction = api.get_transaction_by_hash(
	tx_hash='0x881bd88aac40ba6f49e7e6130e7bafc154a9e918b6f792742ff10cf731309cce')
target_input = transaction['input']

# Search over all Tx within all blocks between 6pm and 7pm local time
#block = api.get_block_by_number(3638953)
#print(block.keys())

hash_list = []
block_number_all = list(range(3638900,3639000))
for block_number in block_number_all:
    block = api.get_block_by_number(block_number)
    for transaction in block['transactions']:
        if transaction['input'] == target_input:
            hash_list.append(transaction['hash'])
        
print (hash_list)
