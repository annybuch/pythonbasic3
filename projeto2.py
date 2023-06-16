# Inicio das Variáveis globais:
lista_peca = []   # Lista vazia para armazenar as peças
codigo_peca = 0   # Variável para controlar o código das peças
# Fim das Variáveis globais.

# Inicio de cadastrarPeca:
def cadastrarPeca(codigo):
  print('Você selecionou o menu de Cadastrar Peças')
  cdg = str(codigo).zfill(3)   # para ficar com zeros a esquerda (preenche com zeros à esquerda até completar 3 dígitos)
  print('Código da peça: {}'.format(cdg))
  nome = input('Entre com o nome da peça: ')   # Solicita ao usuário que insira o nome da peça
  fabricante = input('Entre com o Fabricante da peça: ')   # Solicita ao usuário que insira o fabricante da peça
  preco = float(input('Entre com o preço da peça: '))   # Solicita ao usuário que insira o preço da peça
  dicionario_peca = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'preco': preco}   # Cria um dicionário com as informações da peça
  lista_peca.append(dicionario_peca.copy())   # Adiciona o dicionário à lista de peças
# Fim de cadastrarPeca.

# Inicio de consultarPeca:
def consultarPeca():
  print('Você selecionou o menu de Consultar Peças')
  while True:
    opcao_consultar = input('''
Escolha a opção desejada:
1 - Consultar todas as peças
2 - Consultar Peças por código
3 - Consultar Peça por fabricante
4 - Retornar
''')
    if opcao_consultar == '1':
      print('Você escolheu a opção Consultar todas as peças')
      for peca in lista_peca:   # Itera sobre cada dicionário de peça na lista de peças
        print('-------------------------')
        for key, value in peca.items():   # Itera sobre cada chave e valor do dicionário da peça
          print('{}: {}'.format(key, value))   # Imprime a chave e o valor
        print('-------------------------')

    elif opcao_consultar == '2':
      print('Você escolheu a opção Consultar peças por código')
      valor_codigo = input('Digite o código desejado: ')
      for peca in lista_peca:
        if peca['codigo'] == valor_codigo:   # Verifica se o valor do código da peça no dicionário é igual ao valor desejado
          print('-------------------------')
          for key, value in peca.items():
            print('{}: {}'.format(key, value))
      else:
        print('Este codigo não existe. Tente novamente, por favor!')    # Caso o numero seja digitado errado.

    elif opcao_consultar == '3':
      print('Você escolheu a opção Consultar peças por fabricante')
      valor_codigo = input('Digite o fabricante desejado: ')
      for peca in lista_peca:
        if peca['fabricante'] == valor_codigo:   # Verifica se o valor do fabricante da peça no dicionário é igual ao valor desejado
          print('-------------------------')
          for key, value in peca.items():
            print('{}: {}'.format(key, value))

    elif opcao_consultar == '4':
      return   # Retorna ao menu principal
    else:
      print('Opção Inválida. Tente Novamente')
      continue   # Caso digite errado, volta para o início do menu
# Fim de consultarPeca.

# Inicio de removerPeca:
def removerPeca():
  print('Você escolheu o menu de Remover Peças')
  valor_codigo = int(input('Digite o código da peça que deseja remover: '))
  for peca in lista_peca:
    if peca['codigo'] == valor_codigo:   # Verifica se o valor do código da peça no dicionário é igual ao valor desejado
      lista_peca.remove(peca)   # Remove o dicionário da peça da lista de peças
      print('Produto Removido')
# Fim de removerPeca.

# Inicio Main:
print('Bem-vindo ao controle de estoque da Bicicletaria da Raiany Cristina')
while True:
  opcao_principal = input('''
Escolha a opção desejada:
1 - Cadastrar peça
2 - Consultar Peça
3 - Remover Peça
4 - Sair
''')
  if opcao_principal == '1':
    codigo_peca = codigo_peca + 1   # Incrementa o código da peça
    cadastrarPeca(codigo_peca)   # Chama a função para cadastrar uma peça, passando o código como argumento
  elif opcao_principal == '2':
    consultarPeca()   # Chama a função para consultar peças
  elif opcao_principal == '3':
    removerPeca()   # Chama a função para remover uma peça
  elif opcao_principal == '4':
    break    # Encerra o programa
  else:
    print('Opção Inválida. Tente Novamente')
    continue   # Caso digite errado, volta para o início do menu
# Fim Main.