transaction1 = {
    'amount': '30',
    'sender': 'Alice',
    'receiver': 'Bob'
}
transaction2 = {
    'amount': '200',
    'sender': 'Bob',
    'receiver': 'Alice'
}
transaction3 = {
    'amount': '300',
    'sender': 'Alice',
    'receiver': 'Timothy'
}
transaction4 = {
    'amount': '300',
    'sender': 'Rodrigo',
    'receiver': 'Thomas'
}
transaction5 = {
    'amount': '200',
    'sender': 'Timothy',
    'receiver': 'Thomas'
}
transaction6 = {
    'amount': '400',
    'sender': 'Tiffany',
    'receiver': 'Xavier'
}

mempool = [transaction1, transaction2, transaction3, transaction4, transaction5, transaction6]

my_transaction = {
    'amount': 200,
    'sender': 'Peter',
    'receiver': 'Hase'
}

mempool.append(my_transaction)

block_transaction = []

for i in range(3):
    block_transaction.append(mempool[i])

for i in block_transaction:
    print(i['receiver'])
