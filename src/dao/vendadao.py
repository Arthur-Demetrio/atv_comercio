from dao.dao import DAO
from models.venda import Venda


class VendaDAO(DAO):
    arquivo = "vendas.json"
    classe = Venda
    objetos = []
