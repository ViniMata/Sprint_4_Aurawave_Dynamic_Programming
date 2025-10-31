from pprint import pprint

# VERSÃO ITERATIVA (BOTTOM-UP)

def calcular_maximo_consumo_iterativo(beneficios, insumos_usados, insumos_disponiveis):
    maximo_reagente, maximo_descartavel = insumos_disponiveis

    # Tabela de programação dinâmica
    tabela_dp = [[0] * (maximo_descartavel + 1) for _ in range(maximo_reagente + 1)]

    for quantidade_reagente in range(maximo_reagente + 1):
        for quantidade_descartavel in range(maximo_descartavel + 1):
            for indice in range(len(beneficios)):
                quantidade_reagente_usada, quantidade_descartavel_usada = insumos_usados[indice]
                ganho = beneficios[indice]

                if quantidade_reagente >= quantidade_reagente_usada and quantidade_descartavel >= quantidade_descartavel_usada:
                    restante_reagente = quantidade_reagente - quantidade_reagente_usada
                    restante_descartavel = quantidade_descartavel - quantidade_descartavel_usada

                    novo_total = tabela_dp[restante_reagente][restante_descartavel] + ganho
                    if novo_total > tabela_dp[quantidade_reagente][quantidade_descartavel]:
                        tabela_dp[quantidade_reagente][quantidade_descartavel] = novo_total

    return tabela_dp[maximo_reagente][maximo_descartavel]


# VERSÃO RECURSIVA COM MEMOIZAÇÃO (TOP-DOWN)

cache_global = {}

def calcular_maximo_consumo_recursivo(beneficios, insumos_usados, insumos_disponiveis):
    global cache_global
    cache_global = {}
    quantidade_reagente, quantidade_descartavel = insumos_disponiveis
    return auxiliar(beneficios, insumos_usados, quantidade_reagente, quantidade_descartavel)


def auxiliar(beneficios, insumos_usados, quantidade_reagente, quantidade_descartavel):
    chave_cache = f"r:{quantidade_reagente}-d:{quantidade_descartavel}"
    if chave_cache in cache_global:
        return cache_global[chave_cache]

    resposta_maxima = 0
    for indice in range(len(beneficios)):
        quantidade_reagente_usada, quantidade_descartavel_usada = insumos_usados[indice]
        ganho = beneficios[indice]

        if quantidade_reagente >= quantidade_reagente_usada and quantidade_descartavel >= quantidade_descartavel_usada:
            restante_reagente = quantidade_reagente - quantidade_reagente_usada
            restante_descartavel = quantidade_descartavel - quantidade_descartavel_usada

            novo_total = auxiliar(beneficios, insumos_usados, restante_reagente, restante_descartavel) + ganho
            if novo_total > resposta_maxima:
                resposta_maxima = novo_total

    cache_global[chave_cache] = resposta_maxima
    return resposta_maxima


# TESTES (saída mais visível)

def executar_testes():
    casos_de_teste = [
        ("Caso principal - Mix completo de operações",
         [25, 40, 60],
         [[1, 2], [2, 3], [3, 4]],
         [5, 6],
         85,
         "Utilizando todos os tipos de operações, conseguimos maximizar o benefício em 85 pontos. " 
         "Isso representa o melhor uso possível dos recursos disponíveis no laboratório."),
        
        ("Caso único - Operação básica",
         [10],
         [[1, 1]],
         [3, 3],
         30,
         "Com apenas um tipo de operação básica, alcançamos 30 pontos de benefício. "
         "Demonstra a importância de manter estoques mesmo para procedimentos simples."),
        
        ("Caso dois tipos - Operações complementares",
         [20, 50],
         [[2, 3], [3, 4]],
         [5, 6],
         50,
         "Combinando dois tipos de operações, atingimos 50 pontos de benefício. "
         "Evidencia como a diversificação de procedimentos otimiza o uso dos recursos.")
    ]

    total_de_testes = len(casos_de_teste)
    testes_passados = 0

    print("RESULTADOS DOS TESTES E INSIGHTS DE NEGÓCIO")
    for i, (descricao, beneficios, insumos, estoque_disponivel, resultado_esperado, insight) in enumerate(casos_de_teste, 1):
        resultado_iterativo = calcular_maximo_consumo_iterativo(beneficios, insumos, estoque_disponivel)
        resultado_recursivo = calcular_maximo_consumo_recursivo(beneficios, insumos, estoque_disponivel)

        teste_iterativo_ok = resultado_iterativo == resultado_esperado
        teste_recursivo_ok = resultado_recursivo == resultado_esperado

        status_teste = "OK" if (teste_iterativo_ok and teste_recursivo_ok) else "FAIL"
        if teste_iterativo_ok and teste_recursivo_ok:
            testes_passados += 1

        print(f"\nTeste {i}: {descricao}")
        print(f"  Esperado : {resultado_esperado}")
        print(f"  Iterativo: {resultado_iterativo} -> {'OK' if teste_iterativo_ok else 'FAIL'}")
        print(f"  Recursivo: {resultado_recursivo} -> {'OK' if teste_recursivo_ok else 'FAIL'}")
        print(f"  Resultado: {status_teste}")
        print(f"\n  Insight de negócio:")
        print(f"  {insight}")

    print("RESUMO GERAL")
    print(f"Total de testes passados: {testes_passados} de {total_de_testes}")
    if testes_passados == total_de_testes:
        print(" Todos os testes passaram!")
        print(" O sistema está pronto para otimizar o uso de insumos no laboratório.")
    else:
        print(" Alguns testes falharam - revisão necessária.")
    print("\n")

if __name__ == '__main__':
    executar_testes()

print("Programa concluído com sucesso.")
