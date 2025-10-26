"""
Classe Pessoa (Abstrata):
• __init__(self, nome, idade): inicializa os atributos.
• @property nome: retorna o nome da pessoa.
• @nome.setter: altera o nome da pessoa.
• @property idade: retorna a idade.
• @idade.setter: altera a idade, impedindo valores negativos.
• mostrar_informacoes(self): método abstrato (será sobrescrito pelas subclasses).
"""
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self._nome=nome
        self._idade=idade
    
    @property 
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        self._nome=valor

    @property 
    
    def idade(self):
        return self._idade
    
    @idade.setter
    
    def idade(self):
        pass

    @abstractmethod
    def mostrar_informacoes(self):
        pass
"""
• __init__(self, nome, idade, dias_estadia, quarto=None): inicializa hóspede e dias de estadia.
• @property quarto: retorna o quarto atual.
• @quarto.setter: define o quarto, mas apenas se ele estiver livre.
• atribuir_quarto(self, quarto): associa o quarto ao hóspede.
• calcular_conta(self): retorna o valor total da estadia.
• mostrar_informacoes(self): exibe nome, idade e número do quarto.
• checkout(self): limpa quarto e imprime mensagem de saída."""
class Hospede(Pessoa):
    lista_quartos=[]
    def __init__(self, nome="", idade=0, dias_estadia=0, quarto=""):
        super().__init__(nome, idade)

        self.dias_estadia=dias_estadia
        self._quarto=quarto
        

    @property
    def quarto(self):
        return self._quarto
    
    @quarto.setter
    def quarto(self,novo_quarto):
        self._quarto=novo_quarto
        
    def atribuir_quarto(self):
        print("quartos")
        print("quarto 1 - Simples - R$300")
        print("quarto 2 - Luxo - R$1000")
        escolha=input("Escolha o quarto desejado (1 ou 2): ")
        if escolha=="1":
            from quartos import QuartoSimples
            quarto1=QuartoSimples(1,300)
            if not quarto1.ocupado:
                self.quarto=quarto1.numero
                quarto1._ocupado=True
                print(f"Quarto {quarto1.numero} atribuído ao hóspede: {self.nome}.")
            else:
                print("Quarto indisponível.")

        

    
    def calcular_conta(self,valor_total_estadia):
        return valor_total_estadia#continuar
    
    def mostrar_informacoes(self):
        print(f"\nNome do Hospede: {self.nome}\nIdade: {self.idade}\nNº Quarto: {self.quarto}")
    
    def checkout(self):
        #Continuar
        print(f"Fez {self.nome} checkout do quarto: {self.quarto}(quarto disponivel)")

