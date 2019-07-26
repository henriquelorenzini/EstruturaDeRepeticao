# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')
while len(nome) < 3:
    nome = input('Digite um nome com 3 ou mais letras: ')

idade = int(input('Digite sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade entre 0 e 150: '))

salario = float(input('Digite seu salário: R$ '))
while salario < 0:
    salario = float(input('Digite um salário maior que 0: R$ '))

sexo = input('[M]asculino ou [F]eminino: ')
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite um sexo válido, [M]asculino ou [F]eminino: ')

estado_civil = input('Estado civíl: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ')
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    estado_civil = input('Digite um estado civíl válido: [S]olteiro, [C]asado, [V]iúvo, [D]ivorciado: ')



print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)