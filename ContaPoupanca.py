from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, account_id, saldo) -> None:
        super().__init__(account_id, saldo)
    
    def get_saldo(self):
        return self.saldo

    def set_saldo(self, valor):
        self.saldo = valor

    def sacar(self, valor):
        try:
            if self.saldo < valor:
                raise ValueError
            else:
                saldo_total = self.get_saldo() - valor
                self.set_saldo(saldo_total)
                return self.get_saldo
        except ValueError:
            print('Você não tem saldo suficiente!')

    def depositar(self, valor):
        saldo_total = self.get_saldo() + valor
        self.set_saldo(saldo_total)
        return self.get_saldo
    
class VerifiqueRendimento(ContaPoupanca):
    def __init__(self, account_id, saldo, taxa_de_rendimento) -> None:
        super().__init__(account_id, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento

    def verificar_rendimento_ao_ano(self, saldo, taxa_de_rendimento):
        rendimento = saldo * (taxa_de_rendimento/100)
        saldo_final = saldo + rendimento
        self.set_saldo(saldo_final)
        return self.get_saldo
    
    def verificar_rendimento_por_dia(self, saldo, taxa_de_rendimento):
        rendimento = (saldo * (taxa_de_rendimento/100)) / 365
        saldo_diário = rendimento
        self.set_saldo(saldo_diário)
        return self.get_saldo

manuela = VerifiqueRendimento(0, 1500, 10)

print(f'Você tem R${manuela.saldo} de saldo e a taxa de rendimento anual é de {manuela.taxa_de_rendimento}% ')

manuela.verificar_rendimento_ao_ano(manuela.saldo, manuela.taxa_de_rendimento)

print(f'O saldo final após um ano é de R$',manuela.get_saldo())

manuela.verificar_rendimento_por_dia(manuela.saldo, manuela.taxa_de_rendimento)

print(f'Isso significa que seu rendimento por dia é de R${manuela.get_saldo():.2f}')

manuela = ContaPoupanca(0, 1500)

manuela.depositar(int(input('Quanto você deseja depositar? R$')))()

print('Seu saldo é de R$',manuela.get_saldo())

manuela.sacar(int(input('Quanto você deseja sacar? R$')))

print('Seu saldo é de R$',manuela.get_saldo())
