# Sistema de Recomendação Quantum Finance

> **Trabalho Final - Disciplina: Sistemas de Recomendação**  
> **FIAP - Pós-graduação**  
> **Professor:** José Luiz Maturana Pagnossim  
> **Autores:** Rafael de Miranda / Wilson Roberto de Melo  
> **Data:** Setembro 2025

## 📋 Sobre o Projeto

Sistema completo de recomendação desenvolvido para a fintech **Quantum Finance**, focado em produtos financeiros personalizados. O projeto utiliza dados do Open Finance para oferecer recomendações inteligentes baseadas em perfis similares de clientes.

## 🏢 Quantum Finance - A Fintech

A Quantum Finance é uma fintech que utiliza dados do Open Finance para oferecer recomendações personalizadas de produtos financeiros aos seus clientes, aumentando o engajamento e realizando vendas cruzadas (cross-sell).

## 📁 Estrutura do Projeto

```
trabalho/
├── proposta_trabalho_final.md      # Documentação completa do projeto
├── sistema_recomendacao_quantum_finance.py  # Implementação do sistema
└── README.md                       # Documentação do projeto
```

## 🎯 Objetivo

Recomendar o produto financeiro mais adequado (cartão de crédito, investimento, seguro, empréstimo, financiamento) para novos clientes com base no perfil de usuários similares, utilizando dados do Open Finance para enriquecer o perfil inicial.

## 🏗️ Arquitetura do Sistema

A arquitetura do sistema inclui:

- **Fontes de Dados:** Dados internos + APIs Open Finance
- **Processo de Integração:** ETL Pipeline e Data Quality
- **Motor de Recomendação:** Filtro Colaborativo + Modelos Híbridos
- **Exposição via APIs:** REST API para diferentes canais

## 🖥️ Implementação Técnica

### Tecnologias Utilizadas
- **Python 3.11+**
- **Algoritmo:** Filtro Colaborativo com Distância Euclidiana
- **Dataset:** Base com 25 clientes e 6 produtos financeiros

### Como Executar

1. **Clone ou baixe os arquivos**
2. **Execute o sistema:**
   ```powershell
   python sistema_recomendacao_quantum_finance.py
   ```

### Funcionalidades Implementadas

✅ **Base de Dados Expandida** - 25 clientes com perfis diversos  
✅ **Análise de Similaridade** - Cálculo de distância euclidiana entre usuários  
✅ **Ranking de Similares** - Identificação dos usuários mais próximos  
✅ **Recomendações Personalizadas** - Baseadas em filtro colaborativo  
✅ **Interface Detalhada** - Explicações claras das recomendações  
✅ **Validação de Dados** - Tratamento de erros e casos especiais  
✅ **Análise Estatística** - Métricas por produto e perfil de cliente  
✅ **Consulta Individual** - Busca específica por cliente  
✅ **Análise de Cross-sell** - Identificação de oportunidades comerciais  

## 📊 Exemplos de Execução

O sistema gera recomendações para diferentes perfis de cliente:

- **Tiago** (Perfil minimalista - apenas CC) → Recomenda **Investimentos**
- **Carlos** (CC + Cartão + Empréstimo) → Recomenda **Seguro**  
- **Gabriel** (Jovem - CC + Financiamento) → Recomenda **Seguro**
- **João** (CC + Cartão) → Recomenda **Empréstimo**
- **Helena** (Perfil premium - todos produtos) → Base completa, sem recomendações adicionais

### 📈 Estatísticas da Base de Clientes
- **25 clientes** com perfis diversificados
- **Minimalista** (1-2 produtos): 24% dos clientes
- **Moderado** (3-4 produtos): 68% dos clientes  
- **Premium** (5-6 produtos): 8% dos clientes

## 🔍 Protótipo de Interface

O protótipo descreve uma interface mobile com:
- Card destacado "Produtos que combinam com você"
- Explicação da recomendação baseada em usuários similares
- Indicadores de compatibilidade e personalização
- Feedback do usuário para melhoria contínua

## ⚠️ Limitações Atuais

O sistema possui algumas limitações técnicas:
- Base de dados com escopo reduzido (25 clientes)
- Algoritmo básico de filtro colaborativo
- Não considera fatores temporais ou contextuais
- Ausência de métricas de performance quantitativas
- Recomendações limitadas ao primeiro usuário similar identificado

## 🚀 Roadmap de Melhorias

Para implementação em ambiente corporativo seria necessário:
- **Escalabilidade:** Integração com Big Data (Spark, Hadoop)
- **Algoritmos Avançados:** Matrix Factorization, Deep Learning
- **Processamento Real-time:** Recomendações instantâneas
- **Testes A/B:** Validação contínua da qualidade das recomendações
- **Cold Start Solution:** Tratamento especializado para novos usuários
- **Explicabilidade Avançada:** Justificativas mais detalhadas
- **Compliance:** Conformidade total com LGPD e regulamentações financeiras

## 📈 Impacto Esperado

- ↗️ **15-25%** aumento na conversão de produtos
- 😊 Melhoria na satisfação do cliente
- 📉 Redução de churn
- 🎯 Otimização de campanhas de marketing
- 💡 **Oportunidades identificadas:**
  - Empréstimo: 17 clientes potenciais (68% da base)
  - Financiamento: 16 clientes potenciais (64% da base)
  - Seguro: 13 clientes potenciais (52% da base)

## 📚 Documentação Completa

Para detalhes completos sobre contextualização, arquitetura, protótipo e implementação, consulte o arquivo `proposta_trabalho_final.md`.

---

**Nota:** Este projeto foi desenvolvido como trabalho final da disciplina "Sistemas de Recomendação" da FIAP, aplicando conceitos teóricos em um cenário prático do mercado financeiro brasileiro.
