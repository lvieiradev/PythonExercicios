pi = float(input('Qual o preco do produto que voce quer comprar? :'))
de = 0.05
vd = pi*de
vf = pi-vd
print('O produto que voce quer comprar custa: R${} mas hoje estamos com 5% de desconto, entao o valor final dele vai ser R${}'.format(pi,vf))