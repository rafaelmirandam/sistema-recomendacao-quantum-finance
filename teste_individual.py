"""
Teste Individual - Recomendação para João
Sistema de Recomendação Quantum Finance
"""

# Importar as funções do sistema principal
import sys
sys.path.append('.')

from sistema_recomendacao_quantum_finance import consultar_recomendacao_individual

if __name__ == "__main__":
    # Consulta individual para João
    consultar_recomendacao_individual("João")
