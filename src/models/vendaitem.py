class VendaItem:
    def __init__(self, id, qtd, preco):
        self.set_id(id)
        self.set_qtd(qtd)
        self.set_preco(preco)
        self.set_id_venda(0)
        self.set_id_produto(0)

    def get_id(self): return self.__id
    def get_qtd(self): return self.__qtd
    def get_preco(self): return self.__preco
    def get_id_venda(self): return self.__id_venda
    def get_id_produto(self): return self.__id_produto

    def set_id(self, id):
        if id < 0: raise ValueError("Id inválido")
        self.__id = id

    def set_qtd(self, qtd):
        if qtd <= 0: raise ValueError("Quantidade deve ser positiva")
        self.__qtd = qtd

    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço não pode ser negativo")
        self.__preco = preco

    def set_id_venda(self, id_venda):
        self.__id_venda = id_venda

    def set_id_produto(self, id_produto):
        self.__id_produto = id_produto

    def __str__(self):
        return (f"{self.__id} - qtd: {self.__qtd} - R$ {self.__preco:.2f} - "
                f"venda: {self.__id_venda} - produto: {self.__id_produto}")

    def to_json(self):
        return {"id": self.__id, "qtd": self.__qtd, "preco": self.__preco,
                "id_venda": self.__id_venda, "id_produto": self.__id_produto}

    @staticmethod
    def from_json(dic):
        i = VendaItem(dic["id"], dic["qtd"], dic["preco"])
        i.set_id_venda(dic["id_venda"])
        i.set_id_produto(dic["id_produto"])
        return i
