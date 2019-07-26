# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pais_A = 8000
pais_B = 20000
taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015
anos = 0
while pais_A < pais_B:
    pais_A = pais_A * (1 + taxa_crescimento_A)
    pais_B = pais_B * (1 + taxa_crescimento_B)
    anos = anos + 1

print('Será necessário {} anos para a população do país A ser maior que a do país B'.format(anos))
print('População atual país A: {:.0f}'.format(pais_A))
print('População atual país B: {:.0f}'.format(pais_B))