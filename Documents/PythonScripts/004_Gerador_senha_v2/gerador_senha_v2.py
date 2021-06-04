# Titulo para o programa
print('=' * 28)
print(f'\033[1:7m{"GERADOR DE SENHA":=^28}\033[m')
print('=' * 28)

# Importando as bibliotecas RANDOM, STRING e TIME
import random, string, time

# Criação da variavel tamanho, e um WHILE para ficar repetindo, se o usuário não digitar número
tamanho = input('1) Escolha quantos caracteres você deseja para sua senha: ')
while not tamanho.isnumeric() or int(tamanho) < 4:
    tamanho = input('1)Escolha quantos caracteres você deseja para sua senha: ')
tamanho = int(tamanho)

# Criação da variavel Numero, que aceita S ou N, se não fica repetindo
numero = input('\n2) Deseja Número na sua senha? [S/N]').upper()
while numero != 'S' and numero != 'N':
    numero = input('2) Deseja Número na sua senha? [S/N]').upper()

# criação da variável especial, que aceita S ou N
especial = input('\n3) Deseja caracter especial? [S/N]').upper()
while especial != 'S' and especial != 'N':
    especial = input('3) Deseja caracter especial? [S/N]').upper()


# Criação da variael letras, que aceita S ou N, e se for igual a S, pergunta se vai ser maiuscula, minuscula ou tanto faz
letras = input('\n4) Deseja Letras na sua senha? [S/N]').upper()
while letras != 'S' and letras != 'N':
    letras = input('4) Deseja Letras na sua senha? [S/N]').upper()
if letras == 'S':
    tamanhoLetra = input('\n5) Você prefere minusculas(1), maiúsculas(2) ou tanto faz(3)? ')
    while tamanhoLetra != '1' and tamanhoLetra != '2' and tamanhoLetra != '3':
        tamanhoLetra = input('5) Você prefere minusculas(1), maiúsculas(2) ou tanto faz(3)? ')

# IF - se numero, letras, caracter especial for sim e se desejar letra maiuscula e minuscula
if numero == 'S' and letras == 'S' and tamanhoLetra == '3' and especial == 'S':
    chars = string.ascii_letters + string.digits + '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Letras minúsculas \n• Letras Maiúsculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero, letras, caracter especial for sim e se desejar letra apenas maiuscula
elif numero == 'S' and letras == 'S' and tamanhoLetra == '2' and especial == 'S':
    chars = string.ascii_uppercase + string.digits + '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm:  \n• Números \n• Letras Maísculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')


# IF - se numero, letras, caracter especial for sim e se desejar letra apenas minusculas
elif numero == 'S' and letras == 'S' and tamanhoLetra == '1' and especial == 'S':
    chars = string.ascii_lowercase + string.digits + '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Letras Minúsculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero e letras forem sim, caracter especial for não e se desejar letra minusculas e minusculas
elif numero == 'S' and letras == 'S' and tamanhoLetra == '3' and especial == 'N':
    chars = string.ascii_letters + string.digits
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Letras Minúsculas \n• Letras Maiúsculas\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero e letras forem sim, caracter especial for não e se desejar apenas letra maiusculas
elif numero == 'S' and letras == 'S' and tamanhoLetra == '2' and especial == 'N':
    chars = string.ascii_uppercase + string.digits
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Letras Maiúsculas\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero, letras forem sim,  caracter especial for não e se desejar apenas letra minusculas
elif numero == 'S' and letras == 'S' and tamanhoLetra == '1' and especial == 'N':
    chars = string.ascii_lowercase + string.digits
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Letras Minúsculas\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero e caracter for SIM mas não tiver letras
elif numero == 'S' and letras == 'N' and especial == 'S':
    chars = string.digits + '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - Apenas Números
elif numero == 'S' and letras == 'N' and especial == 'N':
    chars = string.digits
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Números \033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero for não, letras, caracter especial for sim e se desejar letra maiuscula e minuscula
elif numero == 'N' and letras == 'S' and tamanhoLetra == '3' and especial == 'S':
    chars = string.ascii_letters +  '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras minúsculas \n• Letras Maiúsculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')


# IF - se numero for não, letras, caracter especial for sim e se desejar apenas letra maiuscula
elif numero == 'N' and letras == 'S' and tamanhoLetra == '2' and especial == 'S':
    chars = string.ascii_uppercase +  '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras Maiúsculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - se numero for não, letras, caracter especial for sim e se desejar apenas letra minusculas
elif numero == 'N' and letras == 'S' and tamanhoLetra == '1' and especial == 'S':
    chars = string.ascii_lowercase +  '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras Minúsculas \n• Caracteres especiais\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')


# IF - Apenas letras maiúsculas e minúsculas
elif numero == 'N' and letras == 'S' and tamanhoLetra == '3' and especial == 'N':
    chars = string.ascii_letters
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras Minúsculas \n• Letras Minúsculas\033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - Apenas letras maiúsculas
elif numero == 'N' and letras == 'S' and tamanhoLetra == '2' and especial == 'N':
    chars = string.ascii_uppercase
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras Minúsculas \033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

# IF - Apenas letras  minúsculas
elif numero == 'N' and letras == 'S' and tamanhoLetra == '1' and especial == 'N':
    chars = string.ascii_lowercase
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Letras Minúsculas \033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')


# IF - Apenas caracter especial
elif numero == 'N' and letras == 'N' and especial == 'S':
    chars = '!@#$%¨&*()_-+=´`^~[{]},.?ç\///'
    rnd = random.SystemRandom()
    print('\033[1:34mSua senha contêm: \n• Caracteres Especiais \033[m')
    print('\nEstamos criando.... ')
    time.sleep(2)
    # join - junta randomicamenta "rnd" a variavel "chars" no loop dentro da range "tamanho"
    print('\033[1mSua senha é:  ' + ''.join(rnd.choice(chars) for i in range(tamanho)) + '\033[m')

else:
    print('\nBuscando informações necessárias......')
    time.sleep(2)
    print('Estamos quase terminando......')
    time.sleep(1)
    import sys
    sys.exit('Não foi possivel gerar uma senha, o programa será encerrado')