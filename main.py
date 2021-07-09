from classes.wallet import Wallet

def createWallet():
    w = Wallet()
    idWallet = w.generate_unique_id()
    print("L'UUID  a été généré : "+str(idWallet)) 
    saveWallet = w.save()
    print(saveWallet)
        
#createWallet()

def loadWallet():
    w = Wallet()
    print(w.load())

loadWallet()