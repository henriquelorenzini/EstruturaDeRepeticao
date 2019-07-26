# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("digite uma nota de 0 a 10: "))
while 0 > nota or 10 < nota:
    nota = float(input("Valor inválido, digite uma nota de 0 a 10:  "))

print('Nota: {:.1f}'.format(nota))