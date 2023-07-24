print('Formulário de cadastro para uma loja')

Lista_clientes = []

cont = 1

clientes = input('Quantos clientes serão cadastrados: ')


while cont <= int(clientes) :
    Nome_cliente = input('Digite o nome do cliente: ')
    Lista_clientes.append(Nome_cliente)   
    Endereço = input('Digite o endereço do cliente: ')
    Lista_clientes.append(Endereço)
    cpf = input('Digite o cpf do cliente: ')
    Lista_clientes.append(cpf)
    telefone = input('Digite o telefone do Cliente: ')
    Lista_clientes.append(telefone)
    documento = input('Digite o documento do cliente:')
    Lista_clientes.append(documento)
    cont += 1
    print('Cadastro realizado')
else:
    print('Os Clientes foram adicionados com sucesso')
    
    
for clientes in Lista_clientes:
    print(clientes)
    