# Função de boas-vindas
def hello():
    print('Olá!')

# Função para realizar cálculos
def operation():
    a = int(input('Insira um número: '))
    b = int(input('Insira mais um número: '))
    add = a + b
    sub = a - b
    mult = a * b
    div = a / b
    pot = a ** b
    divInt = a // b
    mod = a % b

    # A ordem de print é a ordem de precedência aritmética em Python
    # Lembrando que potência é a 2° mais importante, sendo a 1° qualquer coisa entre ()
    print('A potência vale {}'.format(pot))
    print('A multiplicação vale {}'.format(mult))
    print('A divisão vale {}'.format(div))
    print('A divisão inteira vale {}'.format(divInt))
    print('O módulo vale {}'.format(mod))
    print('A soma vale {}'.format(add))
    print('A subtração vale {}'.format(sub))

# Função de retorno
def again():
    second = input('''Quer realizar outro cálculo? 
    Se sim, digite S 
    Se não, digite N: ''')

    if second.upper() == 'S':
        operation()

    elif second == 'N':
        bye()

    else:
        again()

# Função de despedida
def bye():
    print('Até logo!')

hello()
operation()
again()