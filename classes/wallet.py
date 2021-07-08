import uuid
import random
import json

class Wallet:
    
    def __init__(self):
        self.unique_id = ''
        self.balance = random.randint(1, 10000)
        self.history = []
              
        
    def generate_unique_id(self):
        self.unique_id = uuid.uuid4()
        return self.unique_id
        
    def add_balance(self, nb):
        self.balance += nb
        return self.balance
    
    def sub_balance(self,nb):
        self.balance -= nb
        return self.balance
        
    def send():
        pass
    
    def save(self):
        walletObj =  {"unique_id": self.unique_id, "balance": self.balance, "history": self.history}
        walletObjJson = json.dumps(walletObj.__dict__)
        file = open("../content/wallets/"+self.unique_id+".json", "w")
        file.write(walletObjJson)
        print(file.read())
        file.close()
        
    def load():
        pass