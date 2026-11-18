from dao.dao import DAO
from models.categoria import Categoria


class CategoriaDAO(DAO):
    arquivo = "categorias.json"
    classe = Categoria
    objetos = []
