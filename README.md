Sistema de Delivery - Projeto de Software OO
Descrição do Projeto
O sistema permite gerenciar restaurantes, cardápios, processar pedidos e realizar pagamentos de forma integrada.

Funcionalidades Implementadas
Cadastro e gestão de restaurantes por categoria

Gerenciamento completo de cardápios (adicionar, remover, consultar itens)

Sistema de pedidos com carrinho de compras

Processamento de pagamentos (PIX e Cartão)

Simulação de entrega de pedidos

Estrutura de Classes
1. ItemCardapio
Representa um item do cardápio com nome e preço.

Atributos: _nome, _preco (protegidos)

Métodos: Properties para acesso controlado

2. Restaurante
Gerencia restaurantes e seus cardápios.

Atributos: _nome, _categoria, _cardapio[]

Métodos: adicionar_item(), remover_item(), exibir_cardapio()

3. Pedido
Controla o processo de compra.

Atributos: restaurante, itens[]

Métodos: adicionar_item(), resumo(), cálculo de total

4. Sistema de Pagamento (Hierarquia de Herança)
Pagamento (Classe Abstrata)
Método abstrato: processar()

PagamentoPix
Atributos específicos: _chave_pix

Implementação específica do processamento

PagamentoCartao
Atributos específicos: _numero_cartao, _titular, _cvv

Implementação específica do processamento

5. SistemaDelivery
Classe principal que orquestra todo o sistema.

Atributos: restaurantes (dicionário)

Métodos: cadastrar_restaurante(), fazer_pedido(), listar_restaurantes()
