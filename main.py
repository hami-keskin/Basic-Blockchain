import hashlib
import datetime
from Crypto.Hash import SHA3_256

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.datetime.now().isoformat()

    def calculate_hash(self):
        # Calculate the hash for the transaction using SHA-3 (SHA3_256) algorithm.
        hash_string = self.sender + self.receiver + str(self.amount) + self.timestamp
        sha3_hash = SHA3_256.new(hash_string.encode())
        return sha3_hash.hexdigest()

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Initialize nonce for Proof of Work
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the hash for the current block using SHA-256 algorithm and nonce for Proof of Work.
        transaction_hashes = "".join([transaction.calculate_hash() for transaction in self.transactions])
        hash_string = str(self.index) + str(self.timestamp) + transaction_hashes + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Perform Proof of Work by finding a hash with a specific number of leading zeros (difficulty).
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        # Initialize the blockchain with a genesis block (the first block in the chain).
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Set the difficulty level for Proof of Work

    def create_genesis_block(self):
        # Create the genesis block with index 0, current timestamp, initial data, and "0" as the previous hash.
        return Block(0, datetime.datetime.now().isoformat(), [], "0")

    def get_latest_block(self):
        # Get the latest block in the chain.
        return self.chain[-1]

    def add_block(self, transactions):
        # Add a new block to the blockchain with the given list of transactions.
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), datetime.datetime.now().isoformat(), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)  # Perform mining for the new block
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Check the validity of the entire blockchain.
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the hash of the current block is valid.
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if the previous hash reference in the current block is correct.
            if current_block.previous_hash != previous_block.hash:
                return False

            # Check if the indices of consecutive blocks are valid.
            if current_block.index != previous_block.index + 1:
                return False

        return True

# Example usage with added transaction support
blockchain = Blockchain()

# Create and add transactions
transaction1 = Transaction("Alice", "Bob", 10)
transaction2 = Transaction("Bob", "Charlie", 5)
transactions = [transaction1, transaction2]

blockchain.add_block(transactions)

# Display the blocks in the blockchain.
for block in blockchain.chain:
    print("Block Index: ", block.index)
    print("Timestamp: ", block.timestamp)
    print("Transactions: ", [transaction.__dict__ for transaction in block.transactions])
    print("Previous Hash: ", block.previous_hash)
    print("Nonce: ", block.nonce)
    print("Hash: ", block.hash)
    print("---------------------")