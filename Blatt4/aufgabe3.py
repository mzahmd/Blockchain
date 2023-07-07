from datetime import datetime


class Block:
    time = datetime.now()

    def __init__(self, transaction, previous_hash):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now()

    def print_block(self):
        print(self.transaction)
        print(self.previous_hash)
        print(self.nonce)
        print(self.timestamp)


b = Block(100, 20)

