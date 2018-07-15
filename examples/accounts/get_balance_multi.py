from etherscan.accounts import Account
import json
import math

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = ['0x002e5398336213f7890a3647dea7f8e425feb863', 
           '0xdb7FD07891697f74A7E5102Cc2cC522c25dc06e9',
           '0xFD666ec8Cd0178C027B9A41E8f2F311D854F898d',
           '0x9b6ACdc56871010C00F765dcaDBB3E99aD3c6593',
           '0x9392718a74278ccF741a31bd0c9C5d2BeBB5bAB9',
           '0xbf9299779Df4297f9A8Fb38E2c2e70416023Cbe0',
           '0x83fE4c5638889318ccE79103efe3881E1EfC3DF8',
           '0x52e448aF9bf91916Fb7555cd59A6eB38Ba613E00',
           '0xD5c0e626eD1Ea60776b452C018524D374C30bC26',
           '0x4b11F5AcB84A4E12AD90C4253bB602Cd56Dd3a4F',
           '0xA79B8c2B89f3E7Eb04ead67e65bBF3fCA6d9935E',
           '0x847830bcf9135dc4548a64a55ca2b48a8a75c9bb',
           '0xD9E68069917393974A464e25F123F22C208afc1D',
           '0xD3db32545817a0574938Dc0ab27697699A86efed',
           '0x53c7a8d887d8517aa5a8b268ad48caab20a53a50',
           '0xa4aAA1B5f371Ac9Df6DB74b4aaAB4cAe91810ce8',
           '0x036BBfafae484e8964d861822C9415707b694D4E',
           '0x17AB69ccE747130a5faC74Cb033A3Fa9eFb26d41',
           '0xCdCd8B86263496270568D6CA74626038Bb6c7Edf',
           '0xA5aaC3ff6a6eA1134037752F8eaB76c1854c12e0']

address_extra = ['0xcf6f8CC2B2B2f06F9Cf2c2f919BB8b128F3D0FFA',
                   '0x63ECc6c4594171289a304FCb9e3829cC35Eb6b9C']

api = Account(address=address, api_key=key)
balances = api.get_balance_multiple()
balances_show = [{'account':info.get('account'), 
                  'balance':float(info.get('balance'))/math.pow(10,18)} for info in balances]
print(balances_show)

api = Account(address=address_extra, api_key=key)
balances_extra = api.get_balance_multiple()
balances_extra_show = [{'account':info.get('account'), 
                        'balance':float(info.get('balance'))/math.pow(10,18)} for info in balances_extra]
print(balances_extra_show)