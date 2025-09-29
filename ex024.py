

cidade = input('Digite o nome da sua cidade:')
print('O nome de sua cidade e: {}'.format(cidade))
temsanto = 'Sim' if 'santo' in cidade.lower() else 'Nao'
print('Comeca com Santo? {}'.format(temsanto))