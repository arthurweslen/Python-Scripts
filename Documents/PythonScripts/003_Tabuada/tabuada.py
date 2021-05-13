#Essas primeiras linhas são apenas um título, com cores invertidas
print('='*28)
print(f'\033[1:7m{"TABUADA":=^28}\033[m')
print('='*28)

while True: #sempre vai repetir
    num = input('\nDigite um número para visualizar a tabuada \033[3:33mou qualquer letra para sair\33[m:  ')
    print('='*28)
    if num.isalpha() or num == '':
        print('\033[1:31mPrograma está sendo encerrado!\033[m ')
        break
    for x in range(1,11):
        print('{} X {:2} = {}'.format(int(num),x,int(num) * x))
