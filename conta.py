class Conta:
    def __init__(self, account_id, saldo) -> None:
        self.account_id = account_id
        self.saldo = saldo
    
    def get_account_id(self):
        return self.account_id

