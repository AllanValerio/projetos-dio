# -*- coding: utf-8 -*-

class Heroi:
    """
    Classe que representa um herói de aventura.

    Atributos:
        nome (str): O nome do herói.
        idade (int): A idade do herói.
        tipo (str): O tipo do herói (guerreiro, mago, monge, ninja).
    """
    def __init__(self, nome, idade, tipo):
        """
        Inicializa um novo objeto Heroi.

        Args:
            nome (str): O nome para o herói.
            idade (int): A idade para o herói.
            tipo (str): O tipo para o herói.
        """
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        """
        Determina o tipo de ataque com base no tipo do herói e exibe
        uma mensagem correspondente.
        """
        ataque = ""
        if self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            # Uma mensagem padrão caso o tipo não seja um dos esperados
            ataque = 'um ataque indefinido'

        # Exibe a mensagem de ataque formatada
        print(f"o {self.tipo} atacou usando {ataque}")

# --- Início da Execução do Programa ---

if __name__ == "__main__":
    # Solicita os dados do herói ao usuário
    print("--- Cadastro de Herói ---")
    nome_heroi = input("Digite o nome do herói: ")

    # Validação simples para garantir que a idade seja um número
    while True:
        try:
            idade_heroi = int(input("Digite a idade do herói: "))
            break
        except ValueError:
            print("Idade inválida. Por favor, digite um número.")

    # Loop para garantir que o tipo seja um dos válidos
    tipos_validos = ['guerreiro', 'mago', 'monge', 'ninja']
    while True:
        tipo_heroi = input(f"Digite o tipo do herói ({', '.join(tipos_validos)}): ").lower()
        if tipo_heroi in tipos_validos:
            break
        else:
            print("Tipo inválido. Por favor, escolha um dos tipos listados.")

    print("--------------------------\n")

    # Cria uma instância (objeto) da classe Heroi com os dados fornecidos
    meu_heroi = Heroi(nome=nome_heroi, idade=idade_heroi, tipo=tipo_heroi)

    # Chama o método atacar do objeto criado
    meu_heroi.atacar()
