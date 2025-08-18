#1
compras = ["arroz","feijao","leite",]

compras.append(input("digite um item: "))
compras.append(input("digite um item: "))
compras.append(input("digite um item: "))
print(compras)
remover = input("qual item q desejar remover: ")
compras.remove(remover)

print(compras)

#2

numeros = [6, 2, 7, 1, 9]

numeros.sort()

print(numeros)

numeros.sort(reverse=True)

print(numeros)

#3

notas = [6,9,2,9,3]

soma = 0

for nota in notas:
    soma += nota

media = soma/5
print(f"notas: {notas}")
print(f"media: {media}")

#4

nomes = ["joao","maria","pedro","henderson","ana"]

ver = input("digite um nome: ")

if ver in nomes:
    print("tem esse nome na lista")

else:
    print("nao tem na lista")

#5

num = [4,15,37,58,73,92,83,69,47,25]
print(num)

print("primeiros numeros:")
print(num[0])
print(num[1])
print(num[2])
print("ultimos numeros:")
print(num[7])
print(num[8])
print(num[9])

cont = 1

print("numeros posiçoes pares:")
while True:
    print(num[cont])
    cont += 2
    if cont == 11:
        break