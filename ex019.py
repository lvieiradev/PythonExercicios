from random import choice
aluno = input('Digite o nome dos quatro alunos separados por virgula :')
aluno = aluno.split(',')

print('O alundo escolhido foi : {}'.format(choice(aluno,)))



