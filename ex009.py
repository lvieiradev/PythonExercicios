n1 = int(input('Digite um numero para que o progrma mostre sua tabuada :'))
print('-----Tabuada do numero : {} -----'.format(n1))


for i in range(0,11):
    nx = n1*i
    print('{} X {} = {}'.format(n1,i,nx))

