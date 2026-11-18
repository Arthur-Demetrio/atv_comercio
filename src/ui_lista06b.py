# Lista 06B - Tarefa 3: UI que acessa os DAOs diretamente
from models.cliente import Cliente
from models.categoria import Categoria
from models.produto import Produto
from dao.clientedao import ClienteDAO
from dao.categoriadao import CategoriaDAO
from dao.produtodao import ProdutoDAO


class UI:
    @staticmethod
    def Menu():
        print()
        print("Clientes:   1-Listar   2-Inserir   3-Atualizar   4-Excluir")
        print("Categorias: 5-Listar   6-Inserir   7-Atualizar   8-Excluir")
        print("Produtos:   9-Listar  10-Inserir  11-Atualizar  12-Excluir")
        print("0-Fim")
        return int(input("Informe uma opção: "))

    @staticmethod
    def Main():
        op = -1
        while op != 0:
            try:
                op = UI.Menu()
                if op == 1: UI.Cliente_Listar()
                elif op == 2: UI.Cliente_Inserir()
                elif op == 3: UI.Cliente_Atualizar()
                elif op == 4: UI.Cliente_Excluir()
                elif op == 5: UI.Categoria_Listar()
                elif op == 6: UI.Categoria_Inserir()
                elif op == 7: UI.Categoria_Atualizar()
                elif op == 8: UI.Categoria_Excluir()
                elif op == 9: UI.Produto_Listar()
                elif op == 10: UI.Produto_Inserir()
                elif op == 11: UI.Produto_Atualizar()
                elif op == 12: UI.Produto_Excluir()
            except ValueError as erro:
                print("Erro:", erro)

    # ---------------- Cliente ----------------
    @staticmethod
    def Cliente_Listar():
        for c in ClienteDAO.Listar(): print(c)

    @staticmethod
    def Cliente_Inserir():
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        ClienteDAO.Inserir(Cliente(0, nome, email, fone))

    @staticmethod
    def Cliente_Atualizar():
        UI.Cliente_Listar()
        id = int(input("Id do cliente a atualizar: "))
        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo fone: ")
        ClienteDAO.Atualizar(Cliente(id, nome, email, fone))

    @staticmethod
    def Cliente_Excluir():
        UI.Cliente_Listar()
        ClienteDAO.Excluir(int(input("Id do cliente a excluir: ")))

    # ---------------- Categoria ----------------
    @staticmethod
    def Categoria_Listar():
        for c in CategoriaDAO.Listar(): print(c)

    @staticmethod
    def Categoria_Inserir():
        CategoriaDAO.Inserir(Categoria(0, input("Descrição: ")))

    @staticmethod
    def Categoria_Atualizar():
        UI.Categoria_Listar()
        id = int(input("Id da categoria a atualizar: "))
        CategoriaDAO.Atualizar(Categoria(id, input("Nova descrição: ")))

    @staticmethod
    def Categoria_Excluir():
        UI.Categoria_Listar()
        CategoriaDAO.Excluir(int(input("Id da categoria a excluir: ")))

    # ---------------- Produto ----------------
    @staticmethod
    def Produto_Listar():
        for p in ProdutoDAO.Listar(): print(p)

    @staticmethod
    def Produto_Inserir():
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        UI.Categoria_Listar()
        id_categoria = int(input("Id da categoria: "))
        ProdutoDAO.Inserir(Produto(0, descricao, preco, estoque, id_categoria))

    @staticmethod
    def Produto_Atualizar():
        UI.Produto_Listar()
        id = int(input("Id do produto a atualizar: "))
        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: "))
        estoque = int(input("Novo estoque: "))
        UI.Categoria_Listar()
        id_categoria = int(input("Novo id da categoria: "))
        ProdutoDAO.Atualizar(Produto(id, descricao, preco, estoque, id_categoria))

    @staticmethod
    def Produto_Excluir():
        UI.Produto_Listar()
        ProdutoDAO.Excluir(int(input("Id do produto a excluir: ")))


if __name__ == "__main__":
    UI.Main()
