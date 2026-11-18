from dao.dao import DAO
from models.produto import Produto


class ProdutoDAO(DAO):
    arquivo = "produtos.json"
    classe = Produto
    objetos = []
