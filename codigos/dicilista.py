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

ivros = [
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
