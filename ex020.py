import random
alunos = []

for i in range(1,5):
    nome = input('Digite um nome de aluno de cada vez:'.format(i))
    alunos.append(nome)

random.shuffle(alunos)

print('Ordem de apresentacao :{}'.format(alunos))
