"""
 Este código utiliza a quantidade em polegadas e pede para que
  digite o número correpondente ao formato (Ex: 1 - (21:9)) e
   faz uma função chamada pitagoras() que recebe 2 valores.
"""


# importação da biblioteca math
import math
# 2 inputs para pegar os valores necessários
polegada = float(input('Quantas polegadas tem a sua Tela? '))
formato = input('Qual o formato: 1 - (21:9), 2 - (16:9), 3 - (4:3), 4 - (3:2)? ')

# inicio da função pitagoras()
def pitagoras(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))
    t = 2.5
    x = (polegada * t)
    m = (x / c)
    alt = (b * m)
    lar = (a * m)
    print(f'A altura da sua tela é: {alt:.2f}')
    print(f'A largura da sua tela é: {lar:.2f}')

# utilizando a função pitagoras() dentro de vários condicionais (if)
if formato == '1':
    pitagoras(21, 9)

elif formato == '2':
    pitagoras(16, 9)

elif formato == '3':
    pitagoras(4, 3)

elif formato == '4':
    pitagoras(3, 2)

