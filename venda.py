class Item(object):
    def __init__(self,produto,quantidade,preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def total(self):
        return self.preco * self.quantidade

class Pedido(object):
    def __init__(self,cliente,carrinho,promocao=None):
        self.cliente = cliente
        self.carrinho = list(carrinho)
        self.promocao = promocao

    def total(self):
        if not hasattr(self,'__total'):
            self.__total = sum(item.total() for item in self.carrinho)
        return self.__total
