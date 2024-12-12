'''
   EXEMPLO 04:
   Fazer um programa em que o usuário informe uma palavra e em seguida
   o programa exiba a palavra invertida e diga se ela é um palíndromo ou não.

   Um palíndromo é uma palavra que se lê da mesma forma de trás para frente.

   Observação: utilizar laços de repetição para inverter a palavra.
'''

# Solicita ao usuário que informe uma palavra
palavra = input('Informe uma palavra: ')

# Inverte a palavra
palavra_invertida = ''
for i in range(len(palavra)-1, -1, -1):
    palavra_invertida += palavra[i]

# Exibe a palavra invertida
print(f'Palavra invertida: {palavra_invertida}')

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print('A palavra é um palíndromo.')


