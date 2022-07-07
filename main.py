
# 1 - Imports / bibliotecas

# 2 - Classes

# 3 - Métodos e funções

# Def = Definição

def print_hi(josefino):

    print(f'Ola, {josefino}')
    print(f'vai pra desgraca {josefino} ;)')

def area_do_retangulo(largura, comprimento):
    return largura * comprimento

def area_do_quadrado(lado):
    return lado ** 2

def area_do_triangulo (base,altura):
    return base * altura / 2

def contagem_progressiva (max):
    for number in range(max):   # repetir o bloco do 0 até o max
        print (f'{number}')     # exibir numero

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
            print(number,'Plim Plim desgraca')
        else:
            print(number)

def exibir_dia_if(number):
    if number == 1:
        print('O dia é Domingo')
    elif number ==2:
        print('O dia é Segunda')
    elif number == 3:
        print('O dia é Terça')
    elif number == 4:
        print('O dia é Quarta')
    elif number == 5:
        print('O dia é Quinta')
    elif number == 6:
        print('O dia é Sexta')
    elif number == 7:
        print('O dia é Sábado')
    else:
        print('valor inválido. 1-7.')

def para_ou_continua():
    resposta = 'C' #continua
    while resposta.upper()=='C':
        resposta = input ('Digite C para continuar')
    print('Voce decidiu parar com a brincadeira')

# estrutura == indentificação / estruturação e execução do script

if __name__ == '__main__':
    print_hi('Cyano')

#resultante
answer3 = area_do_triangulo(3,4)
print(f'resultado triangulo {answer3}')
answer2 = area_do_quadrado(3)
print(f'resultado quadrado {answer2}')
answer = area_do_retangulo(3, 4)
print(f'resultado retangulo {answer}')
contagem_progressiva(10)
apoio_ao_candidato('pablinho do povo, vote 44556778',10)
Plm_plim(12)

# exemplo dia da semana com if - elif - else
exibir_dia_if(1)

#exemplo com while - para ou continua
para_ou_continua()

