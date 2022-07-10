#1 - importação de bibliotecas/pacotes
import json

#import pytests
import pytest

#2 - classe

#3 - definições (funções e métodos)
dados ={}

dados['cliente']=[] # - indica a criação de vetor, matriz, lista...
dados['cliente'].append({'nome':'Juca',
                         'telefone':'11920289515',
                         'email':'juca@emailgen.com'})
dados['cliente'].append({'nome':'Heitor',
                         'telefone':'11928889515',
                         'email':'heitor@emaigen.com'})
# - criar arquivo com dados
def criar_json():
    with open('clientes.json', 'w',) as outfile:
        json.dump(dados, outfile,indent=4)

# - leitura do arquivo com dados
def read_json():
    with open('clientes2.json','r') as outfile:
        dados= json.load(outfile)
        for register in dados ['cliente']:
            print(f'nome:'+register['nome'])
            print(f'telefone:' + register['telefone'])
            print(f'email:' + register['email'])
            print('')

def readAndAddTable_json():
    with open('clientes2.json','r') as outfile:
        dados2= json.load(outfile)
        V = ','
        LoremIpsum = []
        for register in dados2['cliente']:
            # exibir no console
            print(f'nome:'+register['nome'])
            print(f'telefone:' + register['telefone'])
            print(f'email:' + register['email'])
            print('')
            # salvar na tabela
            # - 'nome':'Claudio',
            LoremIpsum.append(
                    '{\'nome\''+ ':' + '\'' + register['nome'] + '\','\
                + '\'telefone\''+ ':' + '\'' + register['telefone'] + '\','\
                + '\'email\''+ ':' + '\'' + register['email'] + '\'}'
            )
        dados['cliente'].extend(LoremIpsum)
        #dados['cliente'].append(LoremIpsum)
    with open('clientes3.json', 'w', ) as outfile:
        json.dump(dados, outfile, indent=4)


# - Teste
def test_jsonw():
    criar_json()
    print(dados['cliente'])

def test_jsonr():
    print('Json read per line')
    read_json()
    print(dados['cliente'])

def test_add_json():
    readAndAddTable_json()
    print('final new table')
    print(dados['cliente'])












