financeiro = {
    'receitas': [],
    'despesas': []
}

def adicionar_receita(valor, descricao):
    financeiro['receitas'].append({'valor': valor, 'descricao': descricao})
    print(f'Receita de R${valor} adicionada com sucesso!')

def adicionar_despesa(valor, descricao, categoria):
    financeiro['despesas'].append({'valor': valor, 'descricao': descricao, 'categoria': categoria})
    print(f'Despesa de R${valor} registrada na categoria "{categoria}" com sucesso!')

def calcular_saldo():
    total_receitas = sum([receita['valor'] for receita in financeiro['receitas']])
    total_despesas = sum([despesa['valor'] for despesa in financeiro['despesas']])
    saldo = total_receitas - total_despesas
    return saldo

def gerar_relatorio():
    saldo = calcular_saldo()
    print("\nRelatório Financeiro:")
    print(f"Total de Receitas: R${sum([receita['valor'] for receita in financeiro['receitas']]):.2f}")
    print(f"Total de Despesas: R${sum([despesa['valor'] for despesa in financeiro['despesas']]):.2f}")
    print(f"Saldo Atual: R${saldo:.2f}")
    print("\nDespesas por Categoria:")
    
    categorias = {}
    for despesa in financeiro['despesas']:
        categoria = despesa['categoria']
        if categoria not in categorias:
            categorias[categoria] = 0
        categorias[categoria] += despesa['valor']
    
    for categoria, total in categorias.items():
        print(f"{categoria}: R${total:.2f}")

def exibir_menu():
    print("\nControle Financeiro - Menu")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Gerar Relatório Financeiro")
    print("4. Sair")
    escolha = input("Escolha uma opção (1-4): ")
    return escolha

def executar_programa():
    while True:
        escolha = exibir_menu()
        
        if escolha == '1':
            valor = float(input("Digite o valor da receita: R$"))
            descricao = input("Digite uma descrição para a receita: ")
            adicionar_receita(valor, descricao)
        
        elif escolha == '2':
            valor = float(input("Digite o valor da despesa: R$"))
            descricao = input("Digite uma descrição para a despesa: ")
            categoria = input("Digite a categoria da despesa (ex: Alimentação, Lazer, Saúde): ")
            adicionar_despesa(valor, descricao, categoria)
        
        elif escolha == '3':
            gerar_relatorio()
        
        elif escolha == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

executar_programa()
