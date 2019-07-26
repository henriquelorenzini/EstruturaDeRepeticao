# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_A = int(input('Digite a população atual do país A: '))
porcentagem_crescimento_A = float(input('Digite a porcentagem de crescimento ao ano: '))
pais_B = int(input('Digite a população atual do país B: '))
porcentagem_crescimento_B = float(input('Digite a porcentagem de crescimento ao ano: '))
taxa_crescimento_A = porcentagem_crescimento_A / 100
taxa_crescimento_B = porcentagem_crescimento_B / 100
anos = 0

while pais_A < pais_B:
    pais_A = pais_A * (1 + taxa_crescimento_A)
    pais_B = pais_B * (1 + taxa_crescimento_B)
    anos = anos + 1

print('Será necessário {} anos para a população do país A ser maior que a do país B'.format(anos))
print('População atual do país A após {} anos : {:.0f}'.format(anos, pais_A))
print('População atual do país B após {} anos : {:.0f}'.format(anos, pais_B))