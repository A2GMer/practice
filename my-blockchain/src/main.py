import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# ブロックチェーンの操作例
my_blockchain = Blockchain()
my_data = "Hello, World!"  # ここに登録したい文字列データを設定

# 文字列データをブロックに登録し、ブロックチェーンに追加
new_block = Block(len(my_blockchain.chain), my_blockchain.get_latest_block().hash, int(time.time()), my_data)
my_blockchain.add_block(new_block)

# ブロックチェーンの内容を表示
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("\n")

