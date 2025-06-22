# Comparação entre Treap e Árvore AVL
# Autor: Matheus Cerqueira de Jesus

import time
import random
import sys
from treap import Treap
from avl_tree import AVLTree

class PerformanceAnalyzer:
    """Classe para análise de performance entre Treap e AVL"""
    
    def __init__(self):
        self.results = {}
    
    def measure_time(self, func, *args):
        """Mede o tempo de execução de uma função"""
        import time
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        return end_time - start_time, result
    
    def test_insertions(self, data_sizes, datasets):
        """Testa performance de inserções"""
        print("=== Teste de Inserções ===")
        print(f"{'Teste':<10} {'Treap (s)':<12} {'AVL (s)':<12} {'Razão T/A':<12}")
        print("-" * 50)
        
        treap_times = []
        avl_times = []
        
        for i, (key, data) in enumerate(datasets.items()):
            treap = Treap()
            avl = AVLTree()
            
            # Treap
            treap_time, _ = self.measure_time(
                lambda: [treap.insert(x) for x in data]
            )
            
            # AVL
            avl_time, _ = self.measure_time(
                lambda: [avl.insert(x) for x in data]
            )
            
            treap_times.append(treap_time)
            avl_times.append(avl_time)
            
            ratio = treap_time / avl_time if avl_time > 0 else float('inf')
            print(f"{key:<10} {treap_time:<12.6f} {avl_time:<12.6f} {ratio:<12.2f}")
        
        # Calcular e exibir médias
        avg_treap = sum(treap_times) / len(treap_times)
        avg_avl = sum(avl_times) / len(avl_times)
        avg_ratio = avg_treap / avg_avl if avg_avl > 0 else float('inf')
        
        print("-" * 50)
        print(f"{'MÉDIA':<10} {avg_treap:<12.6f} {avg_avl:<12.6f} {avg_ratio:<12.2f}")
    
    def test_searches(self, data_sizes, datasets):
        """Testa performance de buscas"""
        print("\n=== Teste de Buscas ===")
        print(f"{'Teste':<10} {'Treap (s)':<12} {'AVL (s)':<12} {'Razão T/A':<12}")
        print("-" * 50)
        
        treap_times = []
        avl_times = []
        
        for i, (key, data) in enumerate(datasets.items()):
            # Construir estruturas
            treap = Treap()
            avl = AVLTree()
            
            for x in data:
                treap.insert(x)
                avl.insert(x)
            
            # Buscar todos os elementos 
            search_keys = data
            
            # Treap
            treap_time, _ = self.measure_time(
                lambda: [treap.search(x) for x in search_keys]
            )
            
            # AVL
            avl_time, _ = self.measure_time(
                lambda: [avl.search(x) for x in search_keys]
            )
            
            treap_times.append(treap_time)
            avl_times.append(avl_time)
            
            ratio = treap_time / avl_time if avl_time > 0 else float('inf')
            print(f"{key:<10} {treap_time:<12.6f} {avl_time:<12.6f} {ratio:<12.2f}")
        
        # Calcular e exibir médias
        avg_treap = sum(treap_times) / len(treap_times)
        avg_avl = sum(avl_times) / len(avl_times)
        avg_ratio = avg_treap / avg_avl if avg_avl > 0 else float('inf')
        
        print("-" * 50)
        print(f"{'MÉDIA':<10} {avg_treap:<12.6f} {avg_avl:<12.6f} {avg_ratio:<12.2f}")
    
    def test_deletions(self, data_sizes, datasets):
        """Testa performance de remoções"""
        print("\n=== Teste de Remoções ===")
        print(f"{'Teste':<10} {'Treap (s)':<12} {'AVL (s)':<12} {'Razão T/A':<12}")
        print("-" * 50)
        
        treap_times = []
        avl_times = []
        
        for i, (key, data) in enumerate(datasets.items()):
            # Construir estruturas
            treap = Treap()
            avl = AVLTree()
            
            for x in data:
                treap.insert(x)
                avl.insert(x)
            
            # Deletar metade dos elementos
            delete_keys = data[:len(data)//2]
            
            # Treap
            treap_time, _ = self.measure_time(
                lambda: [treap.delete(x) for x in delete_keys]
            )
            
            # Reconstruir AVL para teste justo
            avl = AVLTree()
            for x in data:
                avl.insert(x)
            
            # AVL
            avl_time, _ = self.measure_time(
                lambda: [avl.delete(x) for x in delete_keys]
            )
            
            treap_times.append(treap_time)
            avl_times.append(avl_time)
            
            ratio = treap_time / avl_time if avl_time > 0 else float('inf')
            print(f"{key:<10} {treap_time:<12.6f} {avl_time:<12.6f} {ratio:<12.2f}")
        
        # Calcular e exibir médias
        avg_treap = sum(treap_times) / len(treap_times)
        avg_avl = sum(avl_times) / len(avl_times)
        avg_ratio = avg_treap / avg_avl if avg_avl > 0 else float('inf')
        
        print("-" * 50)
        print(f"{'MÉDIA':<10} {avg_treap:<12.6f} {avg_avl:<12.6f} {avg_ratio:<12.2f}")

def compare_properties():
    """Compara propriedades estruturais das duas árvores"""
    print("=== Comparação de Propriedades Estruturais ===\n")
    
    # Teste com conjunto específico de dados
    test_data = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 20, 25, 30]
    
    treap = Treap()
    avl = AVLTree()
    
    # Inserir dados
    for x in test_data:
        treap.insert(x)
        avl.insert(x)
    
    print(f"Dados inseridos: {sorted(test_data)}\n")
    
    # Comparar propriedades
    print("Propriedades:")
    print(f"{'Propriedade':<20} {'Treap':<15} {'AVL':<15}")
    print("-" * 50)
    print(f"{'Tamanho':<20} {treap.size():<15} {avl.size():<15}")
    print(f"{'Altura':<20} {treap.height():<15} {avl.height():<15}")
    print(f"{'Balanceamento':<20} {'Probabilístico':<15} {'Garantido':<15}")
    print(f"{'Complexidade pior':<20} {'O(n)':<15} {'O(log n)':<15}")
    print(f"{'Complexidade média':<20} {'O(log n)':<15} {'O(log n)':<15}")
    
    print(f"\nPercurso em ordem (Treap): {treap.inorder_traversal()}")
    print(f"Percurso em ordem (AVL):   {avl.inorder_traversal()}")
    
    # Verificar se ambas mantêm ordem BST
    treap_sorted = treap.inorder_traversal()
    avl_sorted = avl.inorder_traversal()
    
    print(f"\nAmbas mantêm ordem BST: {treap_sorted == avl_sorted == sorted(test_data)}")

def compare_theoretical_aspects():
    """Compara aspectos teóricos das estruturas"""
    print("\n=== Comparação Teórica ===\n")
    
    aspects = [
        ("Tipo de Balanceamento", "Probabilístico", "Determinístico"),
        ("Critério de Balanceamento", "Prioridades aleatórias", "Diferença de altura ≤ 1"),
        ("Rotações por Inserção", "0-1 (esperado)", "0-2 (garantido)"),
        ("Rotações por Remoção", "0-1 (esperado)", "0-2 (garantido)"),
        ("Memória Extra", "Prioridade por nó", "Altura por nó"),
        ("Implementação", "Mais simples", "Mais complexa"),
        ("Garantias de Altura", "Probabilísticas", "Determinísticas"),
        ("Pior Caso", "O(n) com prob. baixa", "O(log n) garantido"),
        ("Uso Prático", "Boa para casos gerais", "Boa para casos críticos")
    ]
    
    print(f"{'Aspecto':<25} {'Treap':<20} {'AVL':<20}")
    print("-" * 65)
    
    for aspect, treap_val, avl_val in aspects:
        print(f"{aspect:<25} {treap_val:<20} {avl_val:<20}")

def main():
    """Função principal de comparação"""
    import random
    print("COMPARAÇÃO ENTRE TREAP E ÁRVORE AVL")
    print("=" * 50)
    
    # Configurar tamanhos de teste
    data_sizes = [100000]  # Apenas um tamanho
    num_tests = 10  # Número de testes

    # Gerar datasets
    random.seed(42)
    datasets = {}

    for i in range(num_tests):
        key = f"test_{i}"  # Chaves diferentes
        datasets[key] = list(range(1, data_sizes[0] + 1))
        random.shuffle(datasets[key])
    
    # Executar testes de performance
    analyzer = PerformanceAnalyzer()
    
    print("\nTESTE DE PERFORMANCE")
    print("Dados inseridos em ordem aleatória")
    print("Tempos em segundos\n")
    
    analyzer.test_insertions(data_sizes, datasets)
    analyzer.test_searches(data_sizes, datasets)
    analyzer.test_deletions(data_sizes, datasets)
    
    # # Comparações estruturais
    # compare_properties()
    
    # # Comparações teóricas
    # compare_theoretical_aspects()
    
    # print("\n=== Análise e Conclusões ===")
    # print("""
# 1. PERFORMANCE:
#    - AVL geralmente é mais rápida para operações individuais
#    - Treap pode ser competitiva em cenários específicos
#    - Diferenças são pequenas para tamanhos moderados

# 2. BALANCEAMENTO:
#    - AVL garante altura O(log n) deterministicamente
#    - Treap oferece altura O(log n) probabilisticamente
#    - AVL é mais previsível para aplicações críticas

# 3. IMPLEMENTAÇÃO:
#    - Treap é conceitualmente mais simples
#    - AVL requer controle rigoroso de balanceamento
#    - Treap usa aleatoriedade para simplificar lógica

# 4. USO RECOMENDADO:
#    - AVL: Sistemas que exigem garantias rígidas de performance
#    - Treap: Aplicações gerais onde simplicidade é valorizada
#    - Ambas: Superiores a BST simples em termos de balanceamento
#     """)

if __name__ == "__main__":
    main()
