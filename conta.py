class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Seu saldo é de {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor_saque):
        return valor_saque <= self.__saldo + self.__limite

     
    def saca(self, valor_saque):
        if self.__pode_sacar(valor_saque):
            self.__saldo -= valor_saque
        else:
            print(f'O valor {valor_saque} é superior ao disponível na conta!')

    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}





#conta = Conta(123, 'Raissa', 15000, 5000)