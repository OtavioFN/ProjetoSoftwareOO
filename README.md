# ProjetoSoftwareOO
Repositório da disciplina de Projeto de Software (com Orientação a Objetos)

# Sistema de Delivery Online (Versão Inicial com POO)

Este projeto é uma simulação de um sistema de delivery de comida, desenvolvido com foco em Programação Orientada a Objetos (POO). O sistema permite o cadastro de restaurantes, adição de itens ao cardápio e consulta dos cardápios disponíveis.

A estrutura atual foca na modelagem básica das entidades `Restaurante` e `Prato`, com previsão de expansão para usuários, pedidos, pagamentos e entregas.

## Estrutura de Classes

### 1. Classe: Restaurante

Representa um restaurante cadastrado no sistema.

**Atributos:**
- `nome`: nome do restaurante
- `categoria`: tipo de comida ou serviço oferecido (ex: "Japonesa", "Lanchonete")
- `cardapio`: lista de objetos do tipo `Prato`

**Métodos:**
- `adicionar_prato(nome, preco)`: adiciona um novo prato ao cardápio do restaurante
- `exibir_cardapio()`: mostra todos os pratos disponíveis no restaurante

---

### 2. Classe: Prato

Representa um item do cardápio de um restaurante.

**Atributos:**
- `nome`: nome do prato
- `preco`: valor em reais do prato

---

## Possíveis Classes Futuras

### Usuario
Simula um cliente do sistema. Poderá realizar pedidos e consultar seu histórico.

**Atributos esperados:** nome, email, senha, endereço  
**Métodos esperados:** fazer_pedido(), consultar_pedidos()

### Pedido
Representa o pedido feito por um usuário.

**Atributos esperados:** usuário, restaurante, lista de pratos, status, valor total  
**Métodos esperados:** calcular_total(), atualizar_status()

### Pagamento
Gerencia o pagamento de um pedido.

**Atributos esperados:** valor, método, status  
**Métodos esperados:** processar_pagamento()

### Entrega
Responsável pela entrega de pedidos.

**Atributos esperados:** pedido, status, tempo estimado  
**Métodos esperados:** atualizar_status()

---
