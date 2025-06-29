def calcular_nivel_rankeado(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = ""
    if vitorias <= 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    return saldo_vitorias, nivel

try:
    vitorias_heroi = int(input("Digite a quantidade de vitórias: "))
    derrotas_heroi = int(input("Digite a quantidade de derrotas: "))

    saldo, nivel = calcular_nivel_rankeado(vitorias_heroi, derrotas_heroi)

    print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")

except ValueError:
    print("Erro: Por favor, digite apenas números inteiros válidos.")
