'''
   Exemplo 01: Laço de Repetição com While
'''

multiplicador = int(input('Digite o multiplicador: '))

multiplicando = 1

print(f'Tabuada de {multiplicador}:')

while multiplicando <= 10:
   print(f'{multiplicador} x {multiplicando} = {multiplicador * multiplicando}')
   multiplicando += 1

print('Fim da tabuada.')