class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f"{self._nome} - R$ {self._preco:.2f}"


class Restaurante:
    def __init__(self, nome, categoria):
        self._nome = nome.lower().strip()
        self._categoria = categoria
        self._cardapio = []

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    def adicionar_item(self, item: ItemCardapio):
        if any(i.nome == item.nome for i in self._cardapio):
            return
        self._cardapio.append(item)

    def exibir_cardapio(self):
        if not self._cardapio:
            print("Cardápio vazio.\n")
            return
        print(f"Cardápio de {self._nome.capitalize()}:")
        for item in self._cardapio:
            print(f" - {item}")
        print()

    def detalhes(self):
        print(f"\nNome: {self._nome.capitalize()}")
        print(f"Categoria: {self._categoria}")
        if not self._cardapio:
            print("Cardápio vazio.")
        else:
            print("Cardápio:")
            for item in self._cardapio:
                print(f" - {item}")
        print()


class Pedido:
    def __init__(self, restaurante: Restaurante):
        self.restaurante = restaurante
        self.itens = []

    def adicionar_item(self, item: ItemCardapio):
        self.itens.append(item)

    def resumo(self):
        total = sum(item.preco for item in self.itens)
        print("\nResumo do Pedido:")
        for item in self.itens:
            print(f" - {item}")
        print(f"Total a pagar: R$ {total:.2f}\n")
        return total


class Pagamento:
    def processar(self, valor):
        raise NotImplementedError


class PagamentoPix(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado via Pix.\n")


class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no Cartão.\n")


class SistemaDelivery:
    def __init__(self):
        self.restaurantes = {}
        self._precarregar_dados()

    def _precarregar_dados(self):
        self.cadastrar_restaurante("Pizzaria do Otávio", "Italiana")
        rest1 = self.restaurantes["pizzaria do otávio"]
        rest1.adicionar_item(ItemCardapio("Pizza Calabresa", 35.0))
        rest1.adicionar_item(ItemCardapio("Pizza Margherita", 30.0))

        self.cadastrar_restaurante("Lanchonete Rapidão", "Fast Food")
        rest2 = self.restaurantes["lanchonete rapidão"]
        rest2.adicionar_item(ItemCardapio("X-Burguer", 15.0))
        rest2.adicionar_item(ItemCardapio("Batata Frita", 10.0))

    def cadastrar_restaurante(self, nome, categoria):
        nome = nome.lower().strip()
        if nome in self.restaurantes:
            return
        self.restaurantes[nome] = Restaurante(nome, categoria)

    def listar_restaurantes(self):
        if not self.restaurantes:
            print("Nenhum restaurante cadastrado.\n")
            return
        print("Restaurantes cadastrados:")
        for r in self.restaurantes.values():
            print(f"- {r.nome.capitalize()} (Categoria: {r.categoria})")
        print()

    def buscar_restaurante(self, nome):
        return self.restaurantes.get(nome.lower())

    def filtrar_por_categoria(self, categoria):
        encontrados = [r for r in self.restaurantes.values() if r.categoria.lower() == categoria.lower()]
        if not encontrados:
            print("Nenhum restaurante encontrado.\n")
            return
        print(f"Restaurantes da categoria {categoria.capitalize()}:")
        for r in encontrados:
            print(f"- {r.nome.capitalize()}")
        print()

    def simular_entrega(self, restaurante):
        print(f"Pedido do restaurante '{restaurante.nome}' saiu para entrega.")
        print("Pedido entregue com sucesso!\n")

    def fazer_pedido_demo(self):
        restaurante = self.restaurantes["pizzaria do otávio"]
        pedido = Pedido(restaurante)
        pedido.adicionar_item(restaurante._cardapio[0])
        pedido.adicionar_item(restaurante._cardapio[1])  
        total = pedido.resumo()
        PagamentoPix().processar(total)
        self.simular_entrega(restaurante)


if __name__ == "__main__":
    menu()

