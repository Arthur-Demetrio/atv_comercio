# Lista 07: interface com o usuário - só conversa com o Service
from service.service import Service


class UI:
    @staticmethod
    def menu():
        print()
        print("Clientes:   1-Inserir   2-Listar   3-Atualizar   4-Excluir")
        print("Categorias: 5-Inserir   6-Listar   7-Atualizar   8-Excluir")
        print("Produtos:   9-Inserir  10-Listar  11-Atualizar  12-Excluir  13-Reajustar")
        print("0-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def main():
        op = -1
        while op != 0:
            try:
                op = UI.menu()
                if op == 1: UI.cliente_inserir()
                elif op == 2: UI.cliente_listar()
                elif op == 3: UI.cliente_atualizar()
                elif op == 4: UI.cliente_excluir()
                elif op == 5: UI.categoria_inserir()
                elif op == 6: UI.categoria_listar()
                elif op == 7: UI.categoria_atualizar()
                elif op == 8: UI.categoria_excluir()
                elif op == 9: UI.produto_inserir()
                elif op == 10: UI.produto_listar()
                elif op == 11: UI.produto_atualizar()
                elif op == 12: UI.produto_excluir()
                elif op == 13: UI.produto_reajustar()
                elif op == 0: print("Fim da aplicação")
                else: print("Opção inválida")
            except ValueError as erro:
                print("Erro:", erro)

    # ---------------- Cliente ----------------
    @staticmethod
    def cliente_inserir():
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        Service.cliente_inserir(nome, email, fone)

    @staticmethod
    def cliente_listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: print("Nenhum cliente cadastrado")
        for c in clientes: print(c)

    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Id do cliente a atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo fone: ")
        Service.cliente_atualizar(id, nome, email, fone)

    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        Service.cliente_excluir(int(input("Id do cliente a excluir: ")))

    # ---------------- Categoria ----------------
    @staticmethod
    def categoria_inserir():
        Service.categoria_inserir(input("Descrição: "))

    @staticmethod
    def categoria_listar():
        categorias = Service.categoria_listar()
        if len(categorias) == 0: print("Nenhuma categoria cadastrada")
        for c in categorias: print(c)

    @staticmethod
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Id da categoria a atualizar: "))
        Service.categoria_atualizar(id, input("Nova descrição: "))

    @staticmethod
    def categoria_excluir():
        UI.categoria_listar()
        Service.categoria_excluir(int(input("Id da categoria a excluir: ")))

    # ---------------- Produto ----------------
    @staticmethod
    def produto_inserir():
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Id da categoria: "))
        Service.produto_inserir(descricao, preco, estoque, id_categoria)

    @staticmethod
    def produto_listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0: print("Nenhum produto cadastrado")
        for p in produtos: print(p)

    @staticmethod
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Id do produto a atualizar: "))
        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        UI.categoria_listar()
        id_categoria = int(input("Novo id da categoria: "))
        Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)

    @staticmethod
    def produto_excluir():
        UI.produto_listar()
        Service.produto_excluir(int(input("Id do produto a excluir: ")))

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Percentual (ex.: 10 para reajuste, -10 para promoção): "))
        Service.produto_reajustar(percentual)
        UI.produto_listar()
