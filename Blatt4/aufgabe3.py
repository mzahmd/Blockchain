from datetime import datetime

print(datetime.now())


class Block:

    def __init__(self, transaction, previous_hash, nonce=0):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()

    def print_block(self):
        print(self.timestamp)
        print(self.transaction)


b = Block(100, 0)
b.print_block()
