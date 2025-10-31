# Sistema de Otimização de Consumo de Insumos

Nas **unidades de diagnóstico**, o consumo diário de insumos (reagentes e descartáveis) **não é registrado com precisão**, o que dificulta o **controle de estoque** e a **previsão de reposição**.

Este projeto modela esse problema usando **Programação Dinâmica**, propondo uma solução que **melhora a visibilidade do consumo** e **reduz desperdícios** ao otimizar o uso dos recursos disponíveis.

---

##  Objetivo

Maximizar o **benefício total** obtido com o uso dos insumos, respeitando os limites de reagentes e descartáveis disponíveis.
Isso representa, na prática, o melhor aproveitamento possível dos materiais do laboratório sem exceder o estoque.

---

##  Sistema de Pontuação/Benefícios

Cada operação no laboratório gera um benefício (pontos) diferente:
- Os pontos representam o valor/importância de cada tipo de procedimento
- Números maiores indicam operações mais valiosas/prioritárias
- Exemplo: Uma operação que gera 60 pontos é mais importante que uma de 25 pontos

Exemplos práticos:
- Operação básica: 10 pontos (exames simples)
- Operação média: 25-40 pontos (exames intermediários)
- Operação complexa: 50-60 pontos (exames especializados)

O sistema busca maximizar estes pontos considerando as limitações de:
- Reagentes disponíveis
- Materiais descartáveis em estoque

---

##  Estruturas e Algoritmos Usados

###  Versão 1 — Recursiva com Memorização (Top-Down)

- Implementada em `get_max_consumo_recursivo()` e `aux()`.
- Utiliza **chamadas recursivas** e um **cache global** para armazenar resultados já computados.
- Garante eficiência evitando recomputar subproblemas repetidos.
- Representa a **abordagem teórica** da Programação Dinâmica.

| Complexidade | Tempo | Espaço |
| :------------ | :----- | :------ |
| **Descrição** | $O(n \times R \times D)$ (n = insumos, R = reagente, D = descartáveis) | $O(R \times D)$ |

---

###  Versão 2 — Iterativa (Bottom-Up)

- Implementada em `get_max_consumo_iterativo()`.
- Cria uma tabela bidimensional (`dp`) onde cada célula representa o melhor resultado possível com uma certa quantidade de insumos.
- Constrói a solução **de forma incremental**, sem usar recursão.
- É a **abordagem prática e eficiente** para grandes volumes de dados.

| Complexidade | Tempo | Espaço |
| :------------ | :----- | :------ |
| **Descrição** | $O(n \times R \times D)$ | $O(R \times D)$ |

---

##  Contexto do Problema

| Elemento | Descrição |
| :--------- | :----------- |
| **Entradas** | Lista de benefícios por tipo de insumo, insumos usados por cada operação e estoque total disponível |
| **Processamento** | Aplicação dos algoritmos de Programação Dinâmica (Top-Down e Bottom-Up) |
| **Saída** | Benefício máximo total possível com os recursos disponíveis |

---

##  Como Executar

1. Clone este repositório:
    ```bash
    git clone [https://github.com/ViniMata/PD_ConsumoInsumos](https://github.com/ViniMata/PD_ConsumoInsumos)
    cd PD_ConsumoInsumos
    ```
2. Execute o programa:
    ```bash
    python main.py
    ```
    O script exibirá:
    * Resultados obtidos pelas versões recursiva e iterativa.
    * Testes automáticos (`assert`) garantindo que ambas produzem o mesmo resultado.

###  Interpretação dos Resultados

Cada valor retornado representa o **máximo benefício possível** obtido a partir dos insumos disponíveis.
Ambas as versões devem retornar o mesmo valor, comprovando a consistência da modelagem por Programação Dinâmica.

###  Conclusão

A aplicação da Programação Dinâmica neste contexto permite:

* Otimizar o uso de insumos e reagentes;
* Reduzir desperdícios e custos de reposição;
* Fornecer visibilidade e previsibilidade ao consumo das unidades de diagnóstico.

Essa abordagem é um exemplo direto de como técnicas de otimização algorítmica podem ser aplicadas para **melhorar a gestão de recursos reais**.

