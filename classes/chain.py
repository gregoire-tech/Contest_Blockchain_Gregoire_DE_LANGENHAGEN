import hashlib
from random import random

class Chain():
    
    def __init__(self):
        self.blocs = []
        self.last_transaction_number = 0
        
    def generate_hash(self):
        hashed = hashlib.sha3_256(self.str(random.randint(0,1000000000)).encode().hexdigest)
        return hashed
    
    def verify_hash():
        pass
    
    def add_block():
        pass
    
    def get_block():
        pass
    
    def add_transaction():
        pass
    