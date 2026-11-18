from dao.dao import DAO
from models.cliente import Cliente


class ClienteDAO(DAO):
    arquivo = "clientes.json"
    classe = Cliente
    objetos = []
