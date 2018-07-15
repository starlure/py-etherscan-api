from etherscan.accounts import Account
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0xC822CFce2Ea209Bc8561d66453E8015DeF94CC23'

api = Account(address=address, api_key=key)
transactions = api.get_transaction_page(page=1, offset=10000, sort='asc')
#print(transactions[0])

hash_list = []
for transaction in transactions:
    if transaction.get('input') == '0x4e7407ea':
        hash_list.append(transaction.get('hash'))
        
print (hash_list)
            