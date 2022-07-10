
# 1 - Imports / bibliotecas

# 2 - Classes

# 3 - Métodos e funções

# Def = Definição

def print_hi(josefino):

    print(f'Ola, {josefino}')
    print(f'Bom dia {josefino} ;)')

def area_do_retangulo(largura, comprimento):
    return largura * comprimento

def area_do_quadrado(lado):
    return lado ** 2

def area_do_triangulo (base,altura):
    return base * altura / 2

def contagem_progressiva (max):
    for number in range(max):   # repetir o bloco do 0 até o max
        print (number)     # exibir numero

def apoio_ao_candidato (name, times):
    for number in range(times):
        #contator= number + 1
        #print(f'{contator} - {name}')
        if number < 9:
            print(f'00{number+1} - {name}')
        elif number < 99:
            print(f'0{number+1} - {name}')
        else:
            print(number+1,'-',name)


def Plm_plim (deadend):
    for number in range(deadend):
        if number % 4 == 0:
            print('Plim Plim')
        else:
            print('{:0>3}'.format(number))


if __name__ == '__main__':
        resposta = 'C'
        while resposta.upper() != 'Z':

            print('\______________________________________/')
            print('|                                      |')
            print('|               M E N U                |')
            print('|______________________________________|')
            print('|         1 - Olá amigavel             |')
            print('|         2 - area do retangulo        |')
            print('|         3 - area do quadrado         |')
            print('|         4 - area do triangulo        |')
            print('|         5 - cntagem progres.         |')
            print('|         6 - Apoiador de Cand.        |')
            print('|         7 - Plim Plim                |')
            print('|                                      |')
            print('|          Z -  S A I R                |')
            print('|                                      |')
            print('\______________________________________/')



            resposta = input('Escolha sua opcao')
            print(f'A sua escolha foi: {resposta}')

            if resposta.upper() != 'Z':
                if resposta == '1':
                    print_hi('seniore')
                elif resposta == '2':
                   resultado = area_do_retangulo(3,4)
                   print(f'{resultado}')
                elif resposta == '3':
                    resultado = area_do_quadrado(5)
                    print(f'{resultado}')
                elif resposta == '4':
                    resultado = area_do_triangulo(3,4)
                    print(f'{resultado}')
                elif resposta == '5':
                    contagem_progressiva(10)
                elif resposta == '6':
                        apoio_ao_candidato('josé cleiton', 10)
                elif resposta == '7':
                        Plm_plim(12)






print('voce escolheu sair, volte sempre')
