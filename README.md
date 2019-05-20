# c0ban Insight API Wrapper
c0banAPI is a c0ban Insight API wrapper which can be use to obtain information of c0ban blockchain 
like transaction details, block details, difficulty, block height etc. 
c0banAPI is based on [c0ban insight](https://insight-beta.c0ban.com/) API.

## Installation 
### PyPI
```
pip install c0banAPI
```
### Source (Github)

git clone https://github.com/dc-aichara/c0banAPI.git

[cd]() c0banAPI

python3 setup.py install

### Usage 

```python
from c0banAPI import c0banAPI
c0ban = c0banAPI()
```

### Examples 


```python
>>> c0ban.get_block(1)
{'hash': '000000004d2907c4e21c500a96f47a1a71e73f28be14f91326b554e5c7c20071',
 'size': 179,
 'height': 1,
 'version': 536870912,
 'merkleroot': 'ff4c293d3282d194c61aaafe63630297473a738beb2c36409739a667d1351abd',
 'tx': ['ff4c293d3282d194c61aaafe63630297473a738beb2c36409739a667d1351abd'],
 'time': 1481982128,
 'nonce': 333601012,
 'bits': '1d00ffff',
 'difficulty': 1,
 'chainwork': '0000000000000000000000000000000000000000000000000000000200020002',
 'confirmations': 2108365,
 'previousblockhash': '000000005184ffce04351e687a3965b300ee011d26b2089232cd039273be4a67',
 'nextblockhash': '000000000a16d208c4d6894fc627d4a626495b0a739c287499594b726675baa6',
 'reward': 22000,
 'isMainChain': True,
 'poolInfo': {}}
 
>>> c0ban.get_latest_block_difficulty()
531.5499447460068

>>> c0ban.get_block_difficullty(1000000)
6699783.9884467

>>> c0ban.get_latest_block_height()
2108373

>>> c0ban.get_transaction_count_of_address('8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK')
92490

>>> c0ban.get_balance_of_address('8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK')
518.0166468

>>> c0ban.get_transactions_of_address('8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK', 1)
[{'txid': '05f45e2b1ea2a830d482b698f76a34acb3ff0e303ed6cc0bdbf6bc6cd56d1744', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03c12b2004dc17e25c0881000161b36400e7676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': 'db27c3fc7fe3c80d17a5c207ea581f392f4425d9190fc9584211ee5b6b779f4e', 'blockheight': 2108353, 'confirmations': 28, 'time': 1558321116, 'blocktime': 1558321116, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '87aa4a276279cb4fa526294cae2f7f05fb941dd8422ae03eb50264c1d0d7a9b0', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03c02b20048917e25c0881000370870c0033676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': '271f77450f3c11dc8d71fd31374bba2c6ed763071fc3fc58b7a9f1262c0f815d', 'blockheight': 2108352, 'confirmations': 29, 'time': 1558321033, 'blocktime': 1558321033, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '9a8f1bf0f89febdf442e8e7de7b80ecc76e368291999131538e854ea099fe130', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03b62b20047216e25c088100036bf9270038676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': 'e5c8be8fa330ff308694b690b5e2d466689a4641a223b44087c627c536dd75a3', 'blockheight': 2108342, 'confirmations': 39, 'time': 1558320754, 'blocktime': 1558320754, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '8f15d3fa787de2f76fbc9e62dfc669f3cd169fa111aef3893f37f417125b69cb', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03b42b20043b16e25c088100009d07000000676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': '215c6fef92316bd40d24fdcef625c3515e386d5234b1b904d81f17dd1fd75808', 'blockheight': 2108340, 'confirmations': 41, 'time': 1558320699, 'blocktime': 1558320699, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '3c6b2d834ac71a4ab4a7cd98a485bfa55e11b9b8616e911e2abbc09e206de976', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03b12b2004cf15e25c0881000283625d22aa676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': 'dab1e837a559675cf7a7d08d81458cb31446701dc9f32b0970eeaed8795fecf4', 'blockheight': 2108337, 'confirmations': 44, 'time': 1558320591, 'blocktime': 1558320591, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '18e8051171032c92c45ff76ebc00fcfe84c9c34b07f5984170ed323ac62776ca', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03a72b20047b14e25c08810001441f000000676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': '144b542d75e53fa7287e4d9da9fa38b4b6f980451d722aabc72f67eac5f02d7b', 'blockheight': 2108327, 'confirmations': 54, 'time': 1558320251, 'blocktime': 1558320251, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '0e0e8c23743ed623b6738b1b3cbd48d6f552780435a964c4e16c52a50c07d68a', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03a62b20045d14e25c0881000361b65800f7676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': '423cfdde61eaf0e0deee3da20e021522ef54f1d6b10716057df0275ea3bfffdb', 'blockheight': 2108326, 'confirmations': 55, 'time': 1558320221, 'blocktime': 1558320221, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '07ad65f32fe6cb6215d17fb559cc1749bd5c39bd29ac0d23ba9d1aa3867594c8', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03a22b2004e913e25c0881000361c05000f3676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': 'e7ffaf17aef432ac44dd9aedb19101449a292d2e56b2ce8886784ab95f4c0804', 'blockheight': 2108322, 'confirmations': 59, 'time': 1558320105, 'blocktime': 1558320105, 'isCoinBase': True, 'valueOut': 1, 'size': 110}, {'txid': '9740abba61d5065a8ea2074f223db7e2a1864fa213b65110019b9cbf1e39d4c5', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '039e2b20045813e25c0881000373216d002a676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00007480', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': 'cbcd15196393a0ee562e00e098041c619affe43884c4dd7920b6150f67116d68', 'blockheight': 2108318, 'confirmations': 63, 'time': 1558319960, 'blocktime': 1558319960, 'isCoinBase': True, 'valueOut': 1.0000748, 'size': 110}, {'txid': 'd9f2ee2653f6e8ab97719d83d972f6d54e6d8d6022109b62be0ac3f02364b69f', 'version': 1, 'locktime': 0, 'vin': [{'coinbase': '03982b20047d12e25c0881000276e32e004a676f732e637800', 'sequence': 0, 'n': 0}], 'vout': [{'value': '1.00000000', 'n': 0, 'scriptPubKey': {'hex': '76a914a02a656b40e5361b266696cca2a7dc5dbfcbfdd188ac', 'asm': 'OP_DUP OP_HASH160 a02a656b40e5361b266696cca2a7dc5dbfcbfdd1 OP_EQUALVERIFY OP_CHECKSIG', 'addresses': ['8VgjdPKYUBS3QhB9z2ZMpu5D9kymavr4kK'], 'type': 'pubkeyhash'}, 'spentTxId': None, 'spentIndex': None, 'spentHeight': None}], 'blockhash': '0ebd6f678301f8341de181a60df292f91b2ea6c6b0f91c7f23acc348946166c1', 'blockheight': 2108312, 'confirmations': 69, 'time': 1558319741, 'blocktime': 1558319741, 'isCoinBase': True, 'valueOut': 1, 'size': 110}]


```
