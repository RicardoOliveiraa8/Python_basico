lista = [1,2,3,4,5,6,7,8,9,10] # lista vazia

def maior(var): #função que busca o maior valor da lista 
    maior = var [0] #começa a buscar o maior número no primeiro item da lista
    for numero in lista: # percorre os números na lista
     if numero > maior: 
         maior = numero
    print('O maior número da lista é: ', maior)
    
def menor(var):
    menor = var[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    print('O menor número é: ', menor)

maior(lista)
menor(lista)