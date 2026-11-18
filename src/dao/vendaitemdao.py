from dao.dao import DAO
from models.vendaitem import VendaItem


class VendaItemDAO(DAO):
    arquivo = "vendaitens.json"
    classe = VendaItem
    objetos = []
