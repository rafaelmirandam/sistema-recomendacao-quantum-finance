# Guia de Desenvolvimento - Sistema de Recomendação Quantum Finance

## 📋 Pré-requisitos

- Python 3.11 ou superior
- Git instalado
- Editor de código (VS Code recomendado)

## 🚀 Como executar o projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd trabalho
   ```

2. **Execute o sistema:**
   ```bash
   python sistema_recomendacao_quantum_finance.py
   ```

## 📁 Estrutura do Projeto

```
trabalho/
├── .gitignore                              # Arquivos ignorados pelo Git
├── README.md                               # Documentação principal
├── DEVELOPMENT.md                          # Este arquivo
├── proposta_trabalho_final.md              # Proposta completa do trabalho
└── sistema_recomendacao_quantum_finance.py # Código-fonte da PoC
```

## 🔄 Fluxo de Desenvolvimento

### Convenções de Commit

Seguimos o padrão [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `refactor:` - Refatoração de código
- `test:` - Adição ou modificação de testes
- `chore:` - Tarefas de manutenção

### Exemplo de Commits:
```bash
git commit -m "feat: adiciona novo algoritmo de recomendação"
git commit -m "fix: corrige cálculo de similaridade"
git commit -m "docs: atualiza documentação da API"
```

## 🧪 Testes

Para executar testes manuais:

1. Execute o sistema principal:
   ```bash
   python sistema_recomendacao_quantum_finance.py
   ```

2. Verifique se todas as recomendações são geradas corretamente
3. Teste casos de erro (usuário inexistente)

## 📊 Melhorias Futuras

### Curto Prazo
- [ ] Implementar métricas de avaliação (RMSE, MAE)
- [ ] Adicionar mais algoritmos de similaridade
- [ ] Criar interface web básica

### Médio Prazo
- [ ] Integração com dados reais via APIs
- [ ] Implementar filtro baseado em conteúdo
- [ ] Sistema de A/B testing

### Longo Prazo
- [ ] Deploy em cloud (AWS/Azure)
- [ ] Implementar deep learning
- [ ] Sistema de monitoramento em tempo real

## 🐛 Reportando Bugs

Para reportar bugs ou sugerir melhorias:

1. Verifique se o issue já existe
2. Crie um novo issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)

## 📚 Recursos Adicionais

- [Documentação Python](https://docs.python.org/3/)
- [Git Documentation](https://git-scm.com/doc)
- [Sistemas de Recomendação - Bibliografia](https://www.amazon.com/Recommender-Systems-Textbook-Charu-Aggarwal/dp/3319296574)

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como trabalho final para a disciplina "Sistemas de Recomendação" da FIAP, sob orientação do professor José Luiz Maturana Pagnossim.

**Objetivo Educacional:** Demonstrar a aplicação prática de conceitos de filtro colaborativo no contexto do Open Finance brasileiro.

---

**Nota:** Este é um projeto educacional e não deve ser usado em ambiente de produção sem as devidas adaptações de segurança, escalabilidade e conformidade regulatória.
