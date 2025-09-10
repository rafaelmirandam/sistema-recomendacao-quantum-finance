# Sistema de Recomendação Quantum Finance

> **Trabalho Final - Disciplina: Sistemas de Recomendação**  
> **FIAP - Pós-graduação**  
> **Professor:** José Luiz Maturana Pagnossim  
> **Data:** Setembro 2025

## 📋 Sobre o Projeto

Este repositório contém a proposta completa para o trabalho final da disciplina "Sistemas de Recomendação", incluindo a implementação de um sistema de recomendação para a fintech fictícia **Quantum Finance**, inspirado no estudo de caso do banco Santander com Open Finance.

## 🏢 Quantum Finance - A Fintech

A Quantum Finance é uma fintech que utiliza dados do Open Finance para oferecer recomendações personalizadas de produtos financeiros aos seus clientes, aumentando o engajamento e realizando vendas cruzadas (cross-sell).

## 📁 Estrutura do Projeto

```
trabalho/
├── proposta_trabalho_final.md      # Proposta completa do trabalho
├── sistema_recomendacao_quantum_finance.py  # Código-fonte da PoC
└── README.md                       # Este arquivo
```

## 🎯 Objetivo

Recomendar o produto financeiro mais adequado (cartão de crédito, investimento, seguro, empréstimo, financiamento) para novos clientes com base no perfil de usuários similares, utilizando dados do Open Finance para enriquecer o perfil inicial.

## 🏗️ Arquitetura do Sistema

O sistema proposto inclui:

- **Fontes de Dados:** Dados internos + APIs Open Finance
- **Processo de Integração:** ETL Pipeline e Data Quality
- **Motor de Recomendação:** Filtro Colaborativo + Modelos Híbridos
- **Exposição via APIs:** REST API para diferentes canais

## 🖥️ Prova de Conceito (PoC)

### Tecnologias Utilizadas
- **Python 3.11+**
- **Algoritmo:** Filtro Colaborativo com Distância Euclidiana
- **Dataset:** Simulado com 6 clientes e 6 produtos financeiros

### Como Executar

1. **Clone ou baixe os arquivos**
2. **Execute o sistema:**
   ```powershell
   python sistema_recomendacao_quantum_finance.py
   ```

### Funcionalidades Implementadas

✅ **Dataset Simulado** - Base de clientes com produtos financeiros  
✅ **Cálculo de Similaridade** - Distância Euclidiana entre usuários  
✅ **Identificação de Similares** - Ranking de usuários similares  
✅ **Geração de Recomendações** - Baseada em filtro colaborativo  
✅ **Interface Amigável** - Explicações detalhadas das recomendações  
✅ **Tratamento de Erros** - Validações e casos extremos  
✅ **Estatísticas** - Análise da base de clientes  

## 📊 Exemplo de Execução

O sistema demonstra recomendações para diferentes perfis:

- **Ana** (CC + Investimento) → Recomenda **Cartão de Crédito**
- **Carlos** (CC + Cartão + Empréstimo) → Recomenda **Seguro**

## 🔍 Protótipo de Interface

O protótipo descreve uma interface mobile com:
- Card destacado "Produtos que combinam com você"
- Explicação da recomendação baseada em usuários similares
- Indicadores de compatibilidade e personalização
- Feedback do usuário para melhoria contínua

## ⚠️ Limitações da PoC

Esta é uma **demonstração educacional** com limitações intencionais:
- Base de dados pequena e simplificada
- Algoritmo básico de filtro colaborativo
- Ausência de fatores temporais/contextuais
- Sem métricas de avaliação de qualidade

## 🚀 Evoluções para Produção

Para implementação real seria necessário:
- **Escalabilidade:** Big Data (Spark, Hadoop)
- **Algoritmos Sofisticados:** Matrix Factorization, Deep Learning
- **Real-time Processing:** Recomendações em tempo real
- **A/B Testing:** Validação contínua da qualidade
- **Cold Start:** Tratamento de novos usuários
- **Explicabilidade:** Justificativas mais robustas
- **Privacidade:** Conformidade com LGPD

## 📈 Impacto Esperado

- ↗️ **15-25%** aumento na conversão de produtos
- 😊 Melhoria na satisfação do cliente
- 📉 Redução de churn
- 🎯 Otimização de campanhas de marketing

## 📚 Documentação Completa

Para detalhes completos sobre contextualização, arquitetura, protótipo e implementação, consulte o arquivo `proposta_trabalho_final.md`.

---

**Nota:** Este projeto foi desenvolvido exclusivamente para fins educacionais como parte do trabalho final da disciplina "Sistemas de Recomendação" da FIAP.
