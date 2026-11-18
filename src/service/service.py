# Lista 07: camada de serviço - a UI chama o Service, o Service usa o modelo e os DAOs
from models.cliente import Cliente
from models.categoria import Categoria
from models.produto import Produto
from dao.clientedao import ClienteDAO
from dao.categoriadao import CategoriaDAO
from dao.produtodao import ProdutoDAO


class Service:
    # ---------------- Cliente ----------------
    @staticmethod
    def cliente_inserir(nome, email, fone):
        ClienteDAO.Inserir(Cliente(0, nome, email, fone))   # id gerado no DAO

    @staticmethod
    def cliente_listar():
        return ClienteDAO.Listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.Listar_Id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        ClienteDAO.Atualizar(Cliente(id, nome, email, fone))

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO.Excluir(id)

    # ---------------- Categoria ----------------
    @staticmethod
    def categoria_inserir(descricao):
        CategoriaDAO.Inserir(Categoria(0, descricao))

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.Listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.Listar_Id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        CategoriaDAO.Atualizar(Categoria(id, descricao))

    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO.Excluir(id)

    # ---------------- Produto ----------------
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        Service.__validar_categoria(id_categoria)
        ProdutoDAO.Inserir(Produto(0, descricao, preco, estoque, id_categoria))

    @staticmethod
    def produto_listar():
        return ProdutoDAO.Listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.Listar_Id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        Service.__validar_categoria(id_categoria)
        ProdutoDAO.Atualizar(Produto(id, descricao, preco, estoque, id_categoria))

    @staticmethod
    def produto_excluir(id):
        ProdutoDAO.Excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        # percentual positivo = reajuste, negativo = promoção (ex.: 10 ou -15)
        for p in ProdutoDAO.Listar():
            p.set_preco(round(p.get_preco() * (1 + percentual / 100), 2))
            ProdutoDAO.Atualizar(p)

    @staticmethod
    def __validar_categoria(id_categoria):
        if CategoriaDAO.Listar_Id(id_categoria) is None:
            raise ValueError(f"Categoria {id_categoria} não existe")
