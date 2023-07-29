lista = [1,2,3,4,5,6,7,8,9,10] # lista com numeros

def maior(var): #função que busca o maior valor da lista 
    maior = var [0] # percorre a lista pelo primeiro item 
    for numero in lista: 
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