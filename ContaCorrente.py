from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, account_id, saldo, limite) -> None:
        super().__init__(account_id, saldo)
        self.limite = limite
        self.saldo_total = self.saldo + self.limite
    
    def get_saldo(self):
        return self.saldo_total

    def set_saldo(self, valor):
        self.saldo_total = valor

    def sacar(self, valor):
        try:
            limite_total = self.saldo + self.limite
            if limite_total < valor:
                raise ValueError
            else:
                saldo_total = self.get_saldo() - valor
                self.set_saldo(saldo_total)
                return self.get_saldo
        except ValueError:
            print('Você não tem saldo suficiente!')

    def depositar(self, valor):
        saldo_total = self.saldo + self.limite
        saldo_total = self.get_saldo() + valor
        self.set_saldo(saldo_total)
        return self.get_saldo

manuela = ContaCorrente(0, 1500, 500)

print(f'Seu saldo é de R$',manuela.get_saldo())

manuela.depositar(int(input('Quanto você deseja depositar? R$')))()

print('Seu saldo é de R$',manuela.get_saldo())

manuela.sacar(int(input('Quanto você deseja sacar? R$')))

print('Seu saldo é de R$',manuela.get_saldo())

