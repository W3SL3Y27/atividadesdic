#1

aluno = {
    "nome": "Wesley",
    "Idade": 16,
    "nota_final": 8,
    "aprovação":"aprovado"
}

print(f"nome:{aluno["nome"]}")
print(f"idade:{aluno["Idade"]}")
print(f"nota final:{aluno["nota_final"]}")
print(f"aprovação:{aluno["aprovação"]}")



#2

produto = {
    "nome":"detergente",
    "preço": 2.00,
    "quantidade": 5,
}

produto["preço"] = 1.50

produto["disponibilidade"] = "disponivel"

print(produto)

#3

palavra = input("Digite uma palavra: ")
contador = {}

for letra in palavra:
    contador[letra] = contador.get(letra, 0) + 1

print(contador)

#4

capitais = {
    "alemanha":"berlim",
    "frança":"paris",
    "espanha":"madrid",
    "italia":"roma"
}

per = input("digite um nome de um pais: ")

for pais in capitais:
    if per == pais:
        print("tem no dicionario")
        break
    else:
        print("nao tem no dicionario")
        break

#5

funcionarios = {
    "joao":1800,
    "pedro":2600,
    "maria":1500,
    "ana":3400,
}

del funcionarios["maria"]

print(funcionarios)