from abc import ABC, abstractmethod

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
            print("Este item já existe no cardápio.\n")
            return
        self._cardapio.append(item)
        print(f"Item '{item.nome}' adicionado ao cardápio de {self._nome}.\n")

    def remover_item(self, nome_item):
        for item in self._cardapio:
            if item.nome == nome_item:
                self._cardapio.remove(item)
                print(f"Item '{nome_item}' removido.\n")
                return
        print("Item não encontrado.\n")

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
        print(f"Item '{item.nome}' adicionado ao carrinho.")

    def resumo(self):
        total = sum(item.preco for item in self.itens)
        print("\nResumo do Pedido:")
        for item in self.itens:
            print(f" - {item}")
        print(f"Total a pagar: R$ {total:.2f}\n")
        return total

class Pagamento(ABC):
    def __init__(self, descricao):
        self._descricao = descricao
    
    @property
    def descricao(self):
        return self._descricao
    
    @abstractmethod
    def processar(self, valor):
        pass

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        super().__init__("Pagamento via PIX")
        self._chave_pix = chave_pix
    
    @property
    def chave_pix(self):
        return self._chave_pix
    
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado via PIX.")
        print(f"Chave PIX: {self._chave_pix}")
        print(f"Descrição: {self._descricao}\n")

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao, titular, cvv):
        super().__init__("Pagamento no Cartão")
        self._numero_cartao = numero_cartao
        self._titular = titular
        self._cvv = cvv
    
    @property
    def numero_cartao(self):
        return self._numero_cartao
    
    @property
    def titular(self):
        return self._titular
    
    def processar(self, valor):
        print(f"Pagamento de R$ {valor:.2f} realizado no Cartão.")
        print(f"Cartão: **** **** **** {self._numero_cartao[-4:]}")
        print(f"Titular: {self._titular}")
        print(f"Descrição: {self._descricao}\n")

class SistemaDelivery:
    def __init__(self):
        self.restaurantes = {}
        self._pre_cadastrar_exemplos()

    def _pre_cadastrar_exemplos(self):
        pizza_place = Restaurante("pizza do zé", "pizzaria")
        pizza_place.adicionar_item(ItemCardapio("Pizza Margherita", 45.90))
        pizza_place.adicionar_item(ItemCardapio("Pizza Calabresa", 52.50))
        pizza_place.adicionar_item(ItemCardapio("Pizza Quatro Queijos", 58.00))
        self.restaurantes["pizza do zé"] = pizza_place
        
        burger_kingdom = Restaurante("burger kingdom", "hamburgueria")
        burger_kingdom.adicionar_item(ItemCardapio("X-Burger", 22.90))
        burger_kingdom.adicionar_item(ItemCardapio("X-Bacon", 28.50))
        burger_kingdom.adicionar_item(ItemCardapio("X-Tudo", 35.00))
        self.restaurantes["burger kingdom"] = burger_kingdom
        
        sushi_house = Restaurante("sushi house", "japonesa")
        sushi_house.adicionar_item(ItemCardapio("Temaki", 18.90))
        sushi_house.adicionar_item(ItemCardapio("Sashimi", 32.00))
        sushi_house.adicionar_item(ItemCardapio("Combo Sushi", 45.50))
        self.restaurantes["sushi house"] = sushi_house
        
        feijoada_do_joao = Restaurante("feijoada do joão", "brasileira")
        feijoada_do_joao.adicionar_item(ItemCardapio("Feijoada Completa", 35.90))
        feijoada_do_joao.adicionar_item(ItemCardapio("Prato Executivo", 22.50))
        feijoada_do_joao.adicionar_item(ItemCardapio("Sobremesa do Dia", 12.00))
        self.restaurantes["feijoada do joão"] = feijoada_do_joao

    def cadastrar_restaurante(self, nome, categoria):
        nome = nome.lower().strip()
        if nome in self.restaurantes:
            print("Já existe um restaurante com esse nome!\n")
            return
        self.restaurantes[nome] = Restaurante(nome, categoria)
        print(f"{nome.capitalize()} cadastrado com sucesso!\n")

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

    def remover_restaurante(self, nome):
        if nome.lower() in self.restaurantes:
            del self.restaurantes[nome.lower()]
            print(f"Restaurante '{nome}' removido.\n")
        else:
            print("Restaurante não encontrado.\n")

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

    def fazer_pedido(self):
        if not self.restaurantes:
            print("Nenhum restaurante disponível.\n")
            return
        self.listar_restaurantes()
        nome = input("Digite o nome do restaurante: ").strip().lower()
        restaurante = self.buscar_restaurante(nome)
        if not restaurante:
            print("Restaurante não encontrado.\n")
            return
        if not restaurante._cardapio:
            print("Este restaurante não possui itens.\n")
            return

        pedido = Pedido(restaurante)
        while True:
            restaurante.exibir_cardapio()
            escolha = input("Escolha o item pelo nome (ou 'fim'): ").strip().lower()
            if escolha == "fim":
                break
            item = next((i for i in restaurante._cardapio if i.nome.lower() == escolha), None)
            if item:
                pedido.adicionar_item(item)
            else:
                print("Item não encontrado.\n")

        if not pedido.itens:
            print("Pedido cancelado.\n")
            return

        total = pedido.resumo()
        metodo = input("Escolha método de pagamento (pix/cartao): ").strip().lower()
        
        if metodo == "pix":
            chave = input("Digite sua chave PIX: ").strip()
            PagamentoPix(chave).processar(total)
        elif metodo == "cartao":
            numero = input("Número do cartão: ").strip()
            titular = input("Titular do cartão: ").strip()
            cvv = input("CVV: ").strip()
            PagamentoCartao(numero, titular, cvv).processar(total)
        else:
            print("Método inválido, pedido cancelado.\n")
            return
            
        self.simular_entrega(restaurante)

def menu():
    sistema = SistemaDelivery()
    while True:
        print("\n======= Otavio's Food Service =======")
        print("1 - Cadastrar restaurante")
        print("2 - Ver restaurantes")
        print("3 - Adicionar item ao cardápio")
        print("4 - Consultar cardápio")
        print("5 - Remover restaurante")
        print("6 - Remover item do cardápio")
        print("7 - Ver detalhes do restaurante")
        print("8 - Filtrar restaurantes por categoria")
        print("9 - Fazer pedido")
        print("10 - Sair")

        opcao = input("Opção: ").strip()
        if opcao == "1":
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            sistema.cadastrar_restaurante(nome, categoria)
        elif opcao == "2":
            sistema.listar_restaurantes()
        elif opcao == "3":
            nome_rest = input("Restaurante: ").strip().lower()
            rest = sistema.buscar_restaurante(nome_rest)
            if not rest:
                print("Restaurante não encontrado.\n")
                continue
            item = input("Nome do item: ")
            try:
                preco = float(input("Preço: "))
                rest.adicionar_item(ItemCardapio(item, preco))
            except ValueError:
                print("Preço inválido.\n")
        elif opcao == "4":
            nome_rest = input("Restaurante: ").strip().lower()
            rest = sistema.buscar_restaurante(nome_rest)
            if rest:
                rest.exibir_cardapio()
            else:
                print("Restaurante não encontrado.\n")
        elif opcao == "5":
            nome = input("Nome do restaurante: ")
            sistema.remover_restaurante(nome)
        elif opcao == "6":
            nome_rest = input("Restaurante: ").strip().lower()
            rest = sistema.buscar_restaurante(nome_rest)
            if not rest:
                print("Restaurante não encontrado.\n")
                continue
            item = input("Nome do item: ").strip()
            rest.remover_item(item)
        elif opcao == "7":
            nome = input("Restaurante: ").strip().lower()
            rest = sistema.buscar_restaurante(nome)
            if rest:
                rest.detalhes()
            else:
                print("Restaurante não encontrado.\n")
        elif opcao == "8":
            categoria = input("Categoria: ")
            sistema.filtrar_por_categoria(categoria)
        elif opcao == "9":
            sistema.fazer_pedido()
        elif opcao == "10":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()