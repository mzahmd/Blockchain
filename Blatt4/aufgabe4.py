from datetime import datetime
from hashlib import sha256


class Block:
    time = datetime.now()

    def __init__(self, transaction, previous_hash, nonce=0):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = datetime.now()
        self.hash = self.generate_hash()

    def print_block(self):
        print(self.timestamp)
        print(self.transaction)
        print(self.hash)

    def generate_hash(self):
        my_str = str(self.timestamp) + str(self.transaction) + str(self.previous_hash) + str(self.nonce)
        hash_str = sha256(my_str.encode()).hexdigest()
        return hash_str


b = Block(12, 0)
print(b.hash)

