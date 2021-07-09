import uuid
import random
import json
import datetime

class Wallet:
    
    def __init__(self):
        self.unique_id = ''
        self.balance = random.randint(1, 10000)
        self.history = []
              
        
    def generate_unique_id(self):
        self.unique_id = str(uuid.uuid4())
        return self.unique_id
    
    def addTimeStamp(self):
        self.history.append(str(datetime.datetime.now()))
        
    def add_balance(self, amount):
        self.balance += amount
        self.addTimeStamp()
        return self.balance
    
    def sub_balance(self,amount):
        self.balance -= amount
        self.addTimeStamp()
        return self.balance
        
    def send():
        pass
    
    def save(self):
        self.addTimeStamp()
        walletObj =  {"unique_id": self.unique_id, "history": {"dateTimeTransation": self.history, "balanceUpdated": self.balance, "from": "null"}}
        walletObjJson = json.dumps(walletObj)
        print(walletObjJson)
        file = open("./content/wallets/"+self.unique_id+".json", "w")
        file.write(walletObjJson)
        file.close()
        
    def load():
        id = input("Entrer l'id du wallet : ")
        file = open("./content/wallets/"+id+".json", "r")
        print(file.read())
        file.close()