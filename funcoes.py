import asteroides
import math
#MENU PARA EXIBICAO
def exibirMenu():
    print('Bem vindo ao programa NASA para registro de asteroides em observação, favor informar o o que deseja fazer')
    print('1 - Adicionar novo asteroide à lista de observação')
    print('2 - Imprimir a lista de asteroides cadastrados')
    print('3 - Imprimir a distancia média entre todos os asteroides registrados\n')
       
#FUNCAO OPCAO DO MENU    
def opcaoMenu():
    opcao = int(input())
    if opcao <= 0 or opcao >= 4:
        print('Opçao invalida/n')
        exibirMenu()
    while opcao == 1:
        return addAsteroide()
    if opcao == 2:
        return listarAsteroide(lista)
    else:
        opcao == 3
        return print(sum(listaAsteroides.values))  
#FUNCAO ADICIONAR ASTEROIDE
def addAsteroide():
    print('Informe o nome do asteroide para adicionar à lista')
    nome = str(input())
    dicAsteroides['nome'] = nome
    print('Digite as ultimas 5 posicoes, em numeros inteiros, do', nome)
    print('Posicao 1')
    pontoA = int(input())
    dicAsteroides['pontoA'] = pontoA
    print('Posicao 2')
    pontoB = int(input())
    dicAsteroides['pontoB'] = pontoB
    print('Posicao 3')
    pontoC = int(input())
    dicAsteroides['pontoC'] = pontoC
    print('Posicao 4')
    pontoD = int(input())
    dicAsteroides['pontoD'] = pontoD
    print('Posicao 5')
    pontoE = int(input())
    dicAsteroides['pontoE'] = pontoE
    listaAsteroides.append(dicAsteroides)
    print(listaAsteroides)
    print('Asteroide cadastrado com sucesso.\n')
    exibirMenu()
#FUNCAO LISTAR ASTEROIDE
def listarAsteroide(lista):
    print (listaAsteroides)
    exibirMenu()