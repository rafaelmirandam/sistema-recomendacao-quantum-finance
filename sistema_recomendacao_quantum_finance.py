"""
Sistema de Recomendação Quantum Finance
Disciplina: Sistemas de Recomendação - FIAP
Professor: José Luiz Maturana Pagnossim
Autores: Rafael de Miranda / Wilson Roberto de Melo
Data: Setembro 2025

Sistema de recomendação para produtos financeiros utilizando algoritmo 
de filtro colaborativo baseado em similaridade entre clientes.
"""

import math
from typing import Dict, List, Tuple

# BASE DE DADOS DOS CLIENTES
# Clientes da Quantum Finance e seus produtos contratados
# Produtos: CC, CartaoCredito, Investimento, Seguro, Emprestimo, Financiamento

clientes_produtos = {
    "Ana": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0
    },
    "Bruno": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 0
    },
    "Carlos": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 1,
        "Financiamento": 0
    },
    "Diana": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 1
    },
    "Eduardo": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0
    },
    "Fernanda": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 1,
        "Emprestimo": 1,
        "Financiamento": 0
    },
    "Gabriel": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 1
    },
    "Helena": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 1,
        "Financiamento": 1
    },
    "Igor": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0
    },
    "Julia": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 0
    },
    "Kevin": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 1,
        "Financiamento": 1
    },
    "Laura": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 0     # Perfil investidor conservador
    },
    "Miguel": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0     # Perfil similar ao Eduardo
    },
    "Natalia": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 0,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 1     # Perfil cauteloso
    },
    "Otavio": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 0     # Perfil similar ao Bruno
    },
    "Patricia": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 1,
        "Financiamento": 0     # Cliente básico com empréstimo
    },
    "Quincy": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 1     # Perfil jovem urbano
    },
    "Rafael": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 1,
        "Financiamento": 0     # Perfil misto
    },
    "Sabrina": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 1     # Perfil similar à Diana
    },
    "Tiago": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0     # Cliente minimalista - só CC
    },
    "Ursula": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 1,
        "Emprestimo": 1,
        "Financiamento": 0     # Perfil similar à Fernanda
    },
    "Vitor": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 1,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 1     # Perfil investidor com financiamento
    },
    "Wanda": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 1,
        "Seguro": 1,
        "Emprestimo": 0,
        "Financiamento": 1     # Cliente quase premium
    },
    "Xavier": {
        "CC": 1,
        "CartaoCredito": 0,
        "Investimento": 0,
        "Seguro": 1,
        "Emprestimo": 1,
        "Financiamento": 0     # Perfil proteção com empréstimo
    },
    "João": {
        "CC": 1,
        "CartaoCredito": 1,
        "Investimento": 0,
        "Seguro": 0,
        "Emprestimo": 0,
        "Financiamento": 0     # Perfil jovem urbano - CC + Cartão
    }
}

# Informações dos produtos para exibição mais rica das recomendações
produtos_info = {
    "CartaoCredito": {
        "nome": "Cartão Quantum Finance Premium",
        "descricao": "Cartão de crédito com cashback e anuidade grátis no primeiro ano",
        "beneficios": ["Cashback de 2%", "Anuidade grátis 1º ano", "Limite pré-aprovado"]
    },
    "Investimento": {
        "nome": "Quantum Finance Investimentos",
        "descricao": "Plataforma completa de investimentos com taxa zero",
        "beneficios": ["Taxa zero", "Assessoria gratuita", "Diversificação automática"]
    },
    "Seguro": {
        "nome": "Seguro Quantum Finance Vida",
        "descricao": "Proteção completa para você e sua família",
        "beneficios": ["Cobertura ampla", "Assistência 24h", "Preço competitivo"]
    },
    "Emprestimo": {
        "nome": "Empréstimo Quantum Finance",
        "descricao": "Crédito rápido com juros baixos",
        "beneficios": ["Juros baixos", "Aprovação rápida", "Sem burocracia"]
    },
    "Financiamento": {
        "nome": "Financiamento Quantum Finance",
        "descricao": "Realize seus sonhos com nosso financiamento",
        "beneficios": ["Parcelas fixas", "Prazo longo", "Taxa competitiva"]
    }
}

def calcular_distancia_euclidiana(cliente1: Dict[str, int], cliente2: Dict[str, int]) -> float:
    """
    Calcula a distância euclidiana entre dois clientes com base nos produtos que possuem.
    
    A distância euclidiana é uma medida de similaridade onde valores menores indicam
    maior similaridade entre os usuários. É calculada como a raiz quadrada da soma
    dos quadrados das diferenças entre as características de cada usuário.
    
    Args:
        cliente1: Dicionário com produtos do primeiro cliente (0 ou 1)
        cliente2: Dicionário com produtos do segundo cliente (0 ou 1)
        
    Returns:
        float: Distância euclidiana entre os dois clientes
    """
    
    # Soma dos quadrados das diferenças para cada produto
    soma_quadrados = 0
    
    # Itera sobre todos os produtos disponíveis
    for produto in cliente1.keys():
        diferenca = cliente1[produto] - cliente2[produto]
        soma_quadrados += diferenca ** 2
    
    # Retorna a raiz quadrada da soma dos quadrados (distância euclidiana)
    distancia = math.sqrt(soma_quadrados)
    
    return distancia

def encontrar_usuarios_similares(usuario_alvo: str, base_clientes: Dict[str, Dict[str, int]]) -> List[Tuple[str, float]]:
    """
    Encontra todos os usuários similares ao usuário alvo, ordenados por similaridade.
    
    Esta função implementa a parte central do filtro colaborativo: identificar usuários
    com perfis similares com base nos produtos que possuem.
    
    Args:
        usuario_alvo: Nome do cliente para o qual queremos encontrar similares
        base_clientes: Base completa de clientes e seus produtos
        
    Returns:
        List[Tuple[str, float]]: Lista de tuplas (nome_cliente, distancia) ordenada por similaridade
    """
    
    # Verifica se o usuário alvo existe na base
    if usuario_alvo not in base_clientes:
        print(f"Erro: Usuário '{usuario_alvo}' não encontrado na base de dados.")
        return []
    
    # Lista para armazenar as similaridades
    similaridades = []
    
    # Perfil do usuário alvo
    perfil_alvo = base_clientes[usuario_alvo]
    
    # Calcula a distância para todos os outros usuários
    for cliente, perfil in base_clientes.items():
        if cliente != usuario_alvo:  # Não compara o usuário consigo mesmo
            distancia = calcular_distancia_euclidiana(perfil_alvo, perfil)
            similaridades.append((cliente, distancia))
    
    # Ordena por distância (menor distância = maior similaridade)
    similaridades.sort(key=lambda x: x[1])
    
    return similaridades

def recomendar_produto(usuario_alvo: str, base_clientes: Dict[str, Dict[str, int]]) -> Dict:
    """
    Função principal de recomendação que implementa a lógica do filtro colaborativo.
    
    Esta função encontra o usuário mais similar ao usuário alvo e recomenda um produto
    que o usuário similar possui, mas o usuário alvo ainda não possui.
    
    Args:
        usuario_alvo: Nome do cliente para quem fazer a recomendação
        base_clientes: Base completa de clientes e seus produtos
        
    Returns:
        Dict: Dicionário com informações da recomendação ou mensagem de erro
    """
    
    print(f"\n{'='*60}")
    print(f"SISTEMA DE RECOMENDAÇÃO QUANTUM FINANCE")
    print(f"Gerando recomendação para: {usuario_alvo}")
    print(f"{'='*60}")
    
    # Verifica se o usuário existe na base
    if usuario_alvo not in base_clientes:
        return {
            "erro": f"Usuário '{usuario_alvo}' não encontrado na base de dados.",
            "sucesso": False
        }
    
    # 1. Exibe o perfil atual do usuário alvo
    perfil_alvo = base_clientes[usuario_alvo]
    print(f"\n📊 PERFIL ATUAL DE {usuario_alvo.upper()}:")
    produtos_possui = [produto for produto, tem in perfil_alvo.items() if tem == 1]
    produtos_nao_possui = [produto for produto, tem in perfil_alvo.items() if tem == 0]
    
    print(f"   ✅ Produtos que possui: {', '.join(produtos_possui)}")
    print(f"   ❌ Produtos que não possui: {', '.join(produtos_nao_possui)}")
    
    # 2. Encontra usuários similares
    print(f"\n🔍 ANALISANDO USUÁRIOS SIMILARES:")
    usuarios_similares = encontrar_usuarios_similares(usuario_alvo, base_clientes)
    
    # Exibe os 3 usuários mais similares
    print("   Top 3 usuários mais similares:")
    for i, (cliente, distancia) in enumerate(usuarios_similares[:3]):
        similaridade_percentual = max(0, (1 - distancia/10) * 100)  # Conversão para percentual
        print(f"   {i+1}. {cliente} (similaridade: {similaridade_percentual:.1f}%)")
    
    # 3. Busca recomendação com base no usuário mais similar
    if not usuarios_similares:
        return {
            "erro": "Não foi possível encontrar usuários similares.",
            "sucesso": False
        }
    
    # Usuário mais similar (primeira posição na lista ordenada)
    usuario_mais_similar, distancia = usuarios_similares[0]
    perfil_similar = base_clientes[usuario_mais_similar]
    
    print(f"\n👥 USUÁRIO MAIS SIMILAR: {usuario_mais_similar}")
    produtos_similar = [produto for produto, tem in perfil_similar.items() if tem == 1]
    print(f"   Produtos que {usuario_mais_similar} possui: {', '.join(produtos_similar)}")
    
    # 4. Identifica produtos para recomendar
    # Produtos que o usuário similar possui, mas o usuário alvo não possui
    produtos_para_recomendar = []
    for produto, tem_produto in perfil_similar.items():
        if tem_produto == 1 and perfil_alvo[produto] == 0:
            produtos_para_recomendar.append(produto)
    
    # 5. Retorna a recomendação
    if not produtos_para_recomendar:
        return {
            "erro": f"Não há produtos para recomendar. {usuario_alvo} já possui todos os produtos que {usuario_mais_similar} possui.",
            "sucesso": False,
            "usuario_similar": usuario_mais_similar,
            "distancia": distancia
        }
    
    # Seleciona o primeiro produto da lista (em um sistema real, seria mais sofisticado)
    produto_recomendado = produtos_para_recomendar[0]
    info_produto = produtos_info.get(produto_recomendado, {})
    
    print(f"\n🎯 RECOMENDAÇÃO GERADA:")
    print(f"   Produto: {info_produto.get('nome', produto_recomendado)}")
    print(f"   Motivo: Usuários similares a você também contrataram este produto")
    print(f"   Baseado em: Perfil de {usuario_mais_similar}")
    
    return {
        "sucesso": True,
        "produto_recomendado": produto_recomendado,
        "nome_produto": info_produto.get('nome', produto_recomendado),
        "descricao": info_produto.get('descricao', ''),
        "beneficios": info_produto.get('beneficios', []),
        "usuario_similar": usuario_mais_similar,
        "distancia": distancia,
        "motivo": f"Baseado no perfil de {usuario_mais_similar}, que possui características similares às suas",
        "todos_produtos_similares": produtos_para_recomendar
    }

def exibir_recomendacao_detalhada(resultado_recomendacao: Dict):
    """
    Exibe a recomendação de forma detalhada e amigável ao usuário.
    
    Args:
        resultado_recomendacao: Resultado retornado pela função recomendar_produto
    """
    
    if not resultado_recomendacao["sucesso"]:
        print(f"\n❌ {resultado_recomendacao['erro']}")
        return
    
    print(f"\n{'='*60}")
    print(f"✨ RECOMENDAÇÃO PERSONALIZADA QUANTUM FINANCE")
    print(f"{'='*60}")
    
    print(f"\n🏆 PRODUTO RECOMENDADO:")
    print(f"   {resultado_recomendacao['nome_produto']}")
    print(f"   {resultado_recomendacao['descricao']}")
    
    if resultado_recomendacao['beneficios']:
        print(f"\n💎 PRINCIPAIS BENEFÍCIOS:")
        for beneficio in resultado_recomendacao['beneficios']:
            print(f"   • {beneficio}")
    
    print(f"\n🧠 POR QUE ESTA RECOMENDAÇÃO?")
    print(f"   {resultado_recomendacao['motivo']}")
    
    similaridade_percentual = max(0, (1 - resultado_recomendacao['distancia']/10) * 100)
    print(f"   Nível de compatibilidade: {similaridade_percentual:.1f}%")
    
    if len(resultado_recomendacao['todos_produtos_similares']) > 1:
        outros_produtos = resultado_recomendacao['todos_produtos_similares'][1:]
        print(f"\n📋 OUTROS PRODUTOS QUE PODEM INTERESSAR:")
        for produto in outros_produtos:
            nome_produto = produtos_info.get(produto, {}).get('nome', produto)
            print(f"   • {nome_produto}")

# EXECUÇÃO DO SISTEMA
if __name__ == "__main__":
    """
    Execução principal do sistema de recomendação.
    Análise completa da base de clientes e geração de recomendações.
    """
    
    print("SISTEMA DE RECOMENDAÇÃO QUANTUM FINANCE")
    print("Desenvolvido para análise de produtos financeiros")
    
    # Exemplo 1: Recomendação para Ana
    print("\n" + "="*80)
    print("EXEMPLO 1: RECOMENDAÇÃO PARA ANA")
    print("="*80)
    
    resultado_ana = recomendar_produto("Ana", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_ana)
    
    # Exemplo 2: Recomendação para Carlos
    print("\n" + "="*80)
    print("EXEMPLO 2: RECOMENDAÇÃO PARA CARLOS")
    print("="*80)
    
    resultado_carlos = recomendar_produto("Carlos", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_carlos)
    
    # Exemplo 3: Recomendação para cliente minimalista (Tiago)
    print("\n" + "="*80)
    print("EXEMPLO 3: RECOMENDAÇÃO PARA CLIENTE MINIMALISTA (TIAGO)")
    print("="*80)
    
    resultado_tiago = recomendar_produto("Tiago", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_tiago)
    
    # Exemplo 4: Recomendação para cliente premium (Helena)
    print("\n" + "="*80)
    print("EXEMPLO 4: CLIENTE PREMIUM - HELENA (JÁ POSSUI TODOS PRODUTOS)")
    print("="*80)
    
    resultado_helena = recomendar_produto("Helena", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_helena)
    
    # Exemplo 5: Recomendação para cliente com perfil específico (Gabriel)
    print("\n" + "="*80)
    print("EXEMPLO 5: RECOMENDAÇÃO PARA GABRIEL (PERFIL JOVEM)")
    print("="*80)
    
    resultado_gabriel = recomendar_produto("Gabriel", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_gabriel)
    
    # Exemplo 6: Recomendação para João (investidor iniciante)
    print("\n" + "="*80)
    print("EXEMPLO 6: RECOMENDAÇÃO PARA JOÃO (INVESTIDOR INICIANTE)")
    print("="*80)
    
    resultado_joao = recomendar_produto("João", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_joao)
    
    # Exemplo 7: Tratamento de erro - usuário inexistente
    print("\n" + "="*80)
    print("EXEMPLO 7: TRATAMENTO DE ERRO - USUÁRIO INEXISTENTE")
    print("="*80)
    
    resultado_erro = recomendar_produto("Maria", clientes_produtos)
    exibir_recomendacao_detalhada(resultado_erro)
    
    # Exemplo 8: Análise geral da base expandida
    print("\n" + "="*80)
    print("EXEMPLO 8: ANÁLISE GERAL DA BASE DE CLIENTES EXPANDIDA")
    print("="*80)
    
    print("\n📊 RESUMO DA BASE DE CLIENTES:")
    for cliente, produtos in clientes_produtos.items():
        total_produtos = sum(produtos.values())
        produtos_lista = [prod for prod, tem in produtos.items() if tem == 1]
        print(f"   {cliente}: {total_produtos} produtos ({', '.join(produtos_lista)})")
    
    print(f"\n📈 ESTATÍSTICAS:")
    print(f"   Total de clientes: {len(clientes_produtos)}")
    print(f"   Total de produtos disponíveis: {len(list(clientes_produtos.values())[0])}")
    
    # Produto mais popular
    produtos_count = {}
    for cliente_produtos_dict in clientes_produtos.values():
        for produto, tem in cliente_produtos_dict.items():
            if tem == 1:
                produtos_count[produto] = produtos_count.get(produto, 0) + 1
    
    produto_mais_popular = max(produtos_count.items(), key=lambda x: x[1])
    print(f"   Produto mais popular: {produto_mais_popular[0]} ({produto_mais_popular[1]} clientes)")
    
    # Estatísticas detalhadas por produto
    print(f"\n📊 DISTRIBUIÇÃO POR PRODUTO:")
    for produto, count in sorted(produtos_count.items(), key=lambda x: x[1], reverse=True):
        percentual = (count / len(clientes_produtos)) * 100
        nome_produto = produtos_info.get(produto, {}).get('nome', produto)
        print(f"   {nome_produto}: {count} clientes ({percentual:.1f}%)")
    
    # Análise de perfis de cliente
    print(f"\n🎯 ANÁLISE DE PERFIS:")
    perfis = {
        "Minimalista (1-2 produtos)": 0,
        "Moderado (3-4 produtos)": 0,
        "Premium (5-6 produtos)": 0
    }
    
    for cliente, produtos in clientes_produtos.items():
        total_produtos = sum(produtos.values())
        if total_produtos <= 2:
            perfis["Minimalista (1-2 produtos)"] += 1
        elif total_produtos <= 4:
            perfis["Moderado (3-4 produtos)"] += 1
        else:
            perfis["Premium (5-6 produtos)"] += 1
    
    for perfil, count in perfis.items():
        percentual = (count / len(clientes_produtos)) * 100
        print(f"   {perfil}: {count} clientes ({percentual:.1f}%)")
    
    # Oportunidades de cross-sell
    print(f"\n💡 OPORTUNIDADES DE CROSS-SELL:")
    produtos_menos_penetrados = sorted(produtos_count.items(), key=lambda x: x[1])[:3]
    for produto, count in produtos_menos_penetrados:
        potencial = len(clientes_produtos) - count
        nome_produto = produtos_info.get(produto, {}).get('nome', produto)
        print(f"   {nome_produto}: {potencial} clientes potenciais")
    
    print(f"\n✅ EXECUÇÃO CONCLUÍDA!")
    print("Sistema analisou base de 25 clientes com sucesso.")
    print("A base diversificada permite:")
    print("• Identificação precisa de similaridades entre usuários")
    print("• Recomendações personalizadas para diferentes perfis")
    print("• Análise robusta de padrões de consumo")
    print("• Mapeamento de oportunidades de cross-sell")
    print("")
    print("Melhorias para ambiente corporativo:")
    print("• Implementação de algoritmos avançados (matrix factorization, deep learning)")
    print("• Tratamento de dados em larga escala")
    print("• Avaliação de qualidade das recomendações")
    print("• Integração com sistemas de produção")
    print("• Tratamento de cold start problem")
    print("• Explicabilidade das recomendações")

def consultar_recomendacao_individual(nome_cliente: str):
    """
    Função para consultar recomendação individual de um cliente específico.
    Útil para testes pontuais e demonstrações interativas.
    
    Args:
        nome_cliente: Nome do cliente para consultar recomendação
    """
    print(f"\n{'='*80}")
    print(f"CONSULTA INDIVIDUAL - SISTEMA QUANTUM FINANCE")
    print(f"{'='*80}")
    
    if nome_cliente not in clientes_produtos:
        print(f"\n❌ Cliente '{nome_cliente}' não encontrado na base.")
        print("📋 Clientes disponíveis:")
        clientes_disponiveis = list(clientes_produtos.keys())
        for i, cliente in enumerate(clientes_disponiveis, 1):
            print(f"   {i:2d}. {cliente}")
        return
    
    resultado = recomendar_produto(nome_cliente, clientes_produtos)
    exibir_recomendacao_detalhada(resultado)
    
# Exemplo de uso da função de consulta individual:
# Para testar um cliente específico, descomente a linha abaixo:
# consultar_recomendacao_individual("João")
