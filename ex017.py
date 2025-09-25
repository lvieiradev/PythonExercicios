from math import hypot
a = float(input('Digite o valor do primeiro cateto : '))
b = float(input('Digite o valor do segundo cateto : '))
c = hypot(a,b)
print('O valor da hipotenusa e de : {:.2f} '.format(c))