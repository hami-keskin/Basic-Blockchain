# Blockchain Implementation

This is a simple implementation of a blockchain with a Proof of Work (PoW) algorithm in Python. The blockchain consists of blocks, each containing multiple transactions.

## Requirements
- Python 3.x
- `hashlib` library
- `Crypto` library for SHA-3 hashing

## Overview

### Transaction Class

The `Transaction` class represents a single transaction in the blockchain. Each transaction includes the sender's address, receiver's address, the amount transferred, and the timestamp.

### Block Class

The `Block` class represents a block in the blockchain. Each block contains a list of transactions, a timestamp, a previous block's hash, a nonce (used in PoW), and its own hash. PoW is performed to mine a block by finding a hash with a specific number of leading zeros (difficulty).

### Blockchain Class

The `Blockchain` class manages the entire blockchain. It starts with a genesis block (the first block) and has a difficulty level for PoW. It can add new blocks with multiple transactions, and it also verifies the integrity of the blockchain.

## Example Usage

```python
from blockchain import Blockchain, Transaction

# Create a new blockchain
blockchain = Blockchain()

# Create and add transactions
transaction1 = Transaction("Alice", "Bob", 10)
transaction2 = Transaction("Bob", "Charlie", 5)
transactions = [transaction1, transaction2]

# Add a new block to the blockchain containing the transactions
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

```
