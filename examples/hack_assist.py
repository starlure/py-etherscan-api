#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:34:06 2018

@author: jasonw
"""

#from etherscan.accounts import Account
from  etherscan.proxies import Proxies
#import numpy as np
import json
import time

def longestSubstringFinder(string1, string2):
    ans = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i+j)<len1 and string1[i+j]==string2[j]:
                match += string2[j]
            else:
                break
        if len(match) > len(ans):
            ans = match
            
    return ans

def main():
    with open('../api_key.json', mode='r') as key_file:
        key = json.loads(key_file.read())['key']
    
    # get steven's contract initialization input data as a reference
    api = Proxies(api_key=key)
    transaction_1 = api.get_transaction_by_hash(
    	tx_hash='0x5920ad6d2c1caa27dae2e85b4764a28c7665d8f4ecfc17150c0abd9f26cb2ca4')
    target_input_1 = transaction_1['input']
    transaction_2 = api.get_transaction_by_hash(
    	tx_hash='0x881bd88aac40ba6f49e7e6130e7bafc154a9e918b6f792742ff10cf731309cce')
    target_input_2 = transaction_2['input']
    
    target_input = longestSubstringFinder(target_input_1, target_input_2)
    # Search over all Tx within all blocks between 6pm and 7pm local time
    #block = api.get_block_by_number(3638953)
    #print(block.keys())
    
    hash_list = []
    block_number_all = list(range(3626750,3626760))
    for block_number in block_number_all:
        block = api.get_block_by_number(block_number)
        for transaction in block['transactions']:
            if transaction['input'][0:5960] == target_input:
                hash_list.append(transaction['hash'])
            
    print (hash_list)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
