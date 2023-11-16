Projeto Final Disciplina Banco de Dados 2 - Laboratório

## Ideia

- Criar um sistema baseado em grafos que armazene as informações de diversas peças
de veículos automotivos produzida por diversos empresas, bem como os existentes 
distribuidores e preços dessas peças. A partir disso, desenvolver uma interface que permita
que dados dos seguintes temas:

* Qual fabricante possui melhor preço para uma determinada peça?
* Quantos fabricantes fabricam determinada peça?
* Qual é o preço médio de venda em cada peça dado um determinado 
conjunto de lojas?
* Qual centro de distribuição possui melhor qualidade na entrega? 
e qual é a pior?

## Quais as entidades?

- As seguintes entidades farão parte do sistema:

* Peça (nome, preço, peso, volume)
* Fabricante (nome, cidade, ano de fundação, telefone)
* Centro de distribuição (nome, cidade, tempo médio de entrega em dias)
* Loja de peças (nome, cidade, faz entregas, avaliação média)

## Relacionamentos

Fabricante -[PRODUZ]-> Peça
CentroDeDistribuição -[ARMAZENA]-> Peça
Loja -[COMPRA_DE]-> CentroDeDistribuição
Loja -[VENDE]-> Peça

## Interação

- Criar:

* CRUD Peça, Fabricante, CentroDeDistribuição, Loja
* Em cada CRUD, inserir também os relacionamentos entre as entidades
* Menu que permita utilizar deste crud no projeto.
