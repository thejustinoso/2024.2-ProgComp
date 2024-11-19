import sys

peso = float(input('Informe o peso (kg)...: '))
if peso <= 0:
    sys.exit('Peso Inválido...\nO peso tem de ser positivo!!!')

altura = float(input('Informe sua altura (m): '))
if altura <= 0:
    sys.exit('Altura Inválida...\nA altura tem de ser positiva!!!')

imc = round(peso / (altura**2), 1)
print(f'IMC = {imc}')

if imc >= 40:
    print('Obesidade Grau III (Mórbida)...')
elif imc >= 35:
    print('Obesidade Grau II ...')
elif imc >= 30:
    print('Obesidade Grau I ...')
elif imc >= 25:
    print('Sobrepeso ...')
elif imc >= 18.5:
    print('Peso Normal ...')
else:
    print('Abaixo do Peso ...')