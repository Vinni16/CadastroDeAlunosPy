print('Lista de alunos')

def menu():
    print('''
    Digite a opção desejada para seguir:
    [1] - Adicionar aluno
    [2] - Deletar aluno
    [3] - Listar aluno
    ''')

menu()
lita_de_alunos = ['vini']
opcao = (input('Escolha uma das opções acima: '))

if opcao == '1':
    aluno = input('Nome do aluno: ')
    lita_de_alunos.append(aluno)
    print('Aluno ' + aluno + ' adicionado com sucesso!')
elif opcao == '2':
    aluno = input('Nome do aluno: ')
    lita_de_alunos.pop(aluno)
    print('Aluno ' + aluno + ' adicionado com sucesso!')
