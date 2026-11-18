import json
import os

PASTA_DADOS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


class DAO:
    """Classe base de persistência. Cada DAO filho define:
       arquivo  -> nome do arquivo JSON
       classe   -> classe do modelo (precisa ter to_json / from_json)
       objetos  -> lista de objetos (atributo de classe)"""
    arquivo = ""
    classe = None
    objetos = []

    @classmethod
    def Inserir(cls, obj):
        cls.Abrir()
        # id com incremento automático: maior id + 1
        maior = max((o.get_id() for o in cls.objetos), default=0)
        obj.set_id(maior + 1)
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls):
        cls.Abrir()
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id):
        cls.Abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj):
        aux = cls.Listar_Id(obj.get_id())
        if aux is None:
            raise ValueError(f"Id {obj.get_id()} não encontrado")
        cls.objetos.remove(aux)
        cls.objetos.append(obj)
        cls.objetos.sort(key=lambda o: o.get_id())
        cls.Salvar()

    @classmethod
    def Excluir(cls, id):
        # aceita o id ou o próprio objeto
        if not isinstance(id, int):
            id = id.get_id()
        aux = cls.Listar_Id(id)
        if aux is None:
            raise ValueError(f"Id {id} não encontrado")
        cls.objetos.remove(aux)
        cls.Salvar()

    @classmethod
    def _caminho(cls):
        return os.path.join(PASTA_DADOS, cls.arquivo)

    @classmethod
    def Abrir(cls):
        cls.objetos = []
        try:
            with open(cls._caminho(), mode="r", encoding="utf-8") as arq:
                for dic in json.load(arq):
                    cls.objetos.append(cls.classe.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def Salvar(cls):
        os.makedirs(PASTA_DADOS, exist_ok=True)
        with open(cls._caminho(), mode="w", encoding="utf-8") as arq:
            json.dump([obj.to_json() for obj in cls.objetos], arq,
                      indent=4, ensure_ascii=False)
