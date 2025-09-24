import math
a = float(input('Digite o valor do primeiro cateto : '))
b = float(input('Digite o valor do segundo cateto : '))
c = math.sqrt((a**2) + (b**2))
print('O valor da hipotenusa e de : {:.2f} '.format(c))