from datetime import datetime
from hashlib import sha256


class Block:
    time = datetime.now()

    def __init__(self, transaction, previous_hash):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = 0
        self.timestamp = datetime.now()
        self.hash = generate_hash(self)

    def print_block(self):
        print(self.transaction)
        print(self.previous_hash)
        print(self.nonce)
        print(self.timestamp)


def generate_hash(self):
    transaction = str(self.transaction)
    previous_hash = str(self.previous_hash)
    nonce = str(self.nonce)
    my_str = transaction + previous_hash + nonce
    sha256(sha256(my_str.encode('utf-8')).hexdigest())


b = Block(12, 23)
print(b)

