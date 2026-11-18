from datetime import datetime


class Venda:
    FORMATO_DATA = "%d/%m/%Y %H:%M"

    def __init__(self, id):
        self.set_id(id)
        self.set_data(datetime.now())
        self.set_carrinho(True)    # True = ainda é carrinho, False = venda finalizada
        self.set_total(0.0)
        self.set_id_cliente(0)

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_carrinho(self): return self.__carrinho
    def get_total(self): return self.__total
    def get_id_cliente(self): return self.__id_cliente

    def set_id(self, id):
        if id < 0: raise ValueError("Id inválido")
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def set_total(self, total):
        if total < 0: raise ValueError("Total não pode ser negativo")
        self.__total = total

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def __str__(self):
        return (f"{self.__id} - {self.__data.strftime(Venda.FORMATO_DATA)} - "
                f"carrinho: {self.__carrinho} - R$ {self.__total:.2f} - "
                f"cliente: {self.__id_cliente}")

    def to_json(self):
        return {"id": self.__id,
                "data": self.__data.strftime(Venda.FORMATO_DATA),
                "carrinho": self.__carrinho,
                "total": self.__total,
                "id_cliente": self.__id_cliente}

    @staticmethod
    def from_json(dic):
        v = Venda(dic["id"])
        v.set_data(datetime.strptime(dic["data"], Venda.FORMATO_DATA))
        v.set_carrinho(dic["carrinho"])
        v.set_total(dic["total"])
        v.set_id_cliente(dic["id_cliente"])
        return v
