# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

username = input('Digite o nome do usuário: ')
password = input('Digite a senha: ')

while username == password:
    print('Usuário e senha iguais, digite valores diferentes: \n')
    username = input('Usuário: ')
    password = input('Senha: ')

print('Login feito com sucesso.')