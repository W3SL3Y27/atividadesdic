#1

alunos = [
    {"nome":"maria","idade":17,"nota":8},
    {"nome":"arthur","idade":16,"nota":6},
    {"nome":"ana","idade":14,"nota":9}
]

for aluno in alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")


#2

notas_alunos = [
    {"nome":"maria","nota":6},
    {"nome":"arthur","nota":9},
    {"nome":"wesley","nota":7},
    {"nome":"carlos","nota":4}
]

for aluno in notas_alunos:
    if aluno["nota"] >= 5:
        print(aluno)


#3

livros = [
    {"titulo":"naruto","autor":"Masashi Kishimoto"},
    {"titulo":"bleach","autor":"Tite Kubo"},
    {"titulo":"cavaleiros do zodiaco","autor":"Masami Kurumada"},
]

perg = input("digite um titulo: ")

for livro in livros:
    if perg == livro["titulo"]:
        print(livro)
    else:
        print("nao tem esse titulo")

#4

funcionarios = [
    {"nome": "Maria", "salario": 2500},
    {"nome": "Carlos", "salario": 1800},
    {"nome": "João", "salario": 2300},
    {"nome": "Ana", "salario": 3200}
]

total_salarios = 0

for funcionario in funcionarios:
    total_salarios += funcionario["salario"]

print(f"total gasto com funcionario: {total_salarios}")

#5

produtos = [
    {"nome": "Arroz", "preco": 20},
    {"nome": "Feijão", "preco": 12},
    {"nome": "Macarrão", "preco": 8},
    {"nome": "Leite", "preco": 5}
]

produto_mudança = "Feijão"
novo_preco = 15

for produto in produtos:
    if produto["nome"] == produto_mudança:
        produto["preco"] = novo_preco
        break 

print(produtos)
