# Implementação de uma estrutura de dados Treap (Tree + Heap)
# Autor: Matheus Cerqueira de Jesus
import random

class TreapNode:
    """Nó da Treap que armazena chave, prioridade e referências para filhos"""
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority if priority is not None else random.random()
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"({self.key}, {self.priority:.3f})"

class Treap:
    """
    Implementação de Treap (Tree + Heap)
    - Propriedade BST: chaves seguem ordenação de árvore binária de busca
    - Propriedade Heap: prioridades seguem propriedade de max-heap
    """
    
    def __init__(self):
        self.root = None
    
    def _rotate_right(self, node):
        """Rotação à direita para manter propriedade do heap"""
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        return left_child
    
    def _rotate_left(self, node):
        """Rotação à esquerda para manter propriedade do heap"""
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        return right_child
    
    def insert(self, key, priority=None):
        """Insere uma chave na Treap"""
        self.root = self._insert_recursive(self.root, key, priority)
    
    def _insert_recursive(self, node, key, priority):
        """Inserção recursiva mantendo propriedades BST e Heap"""
        # Caso base: inserir novo nó
        if node is None:
            return TreapNode(key, priority)
        
        # Inserção seguindo propriedade BST
        if key < node.key:
            node.left = self._insert_recursive(node.left, key, priority)
            # Verificar violação da propriedade heap e corrigir com rotação
            if node.left.priority > node.priority:
                node = self._rotate_right(node)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key, priority)
            # Verificar violação da propriedade heap e corrigir com rotação
            if node.right.priority > node.priority:
                node = self._rotate_left(node)
        # Se key == node.key, não inserimos (chaves duplicadas não permitidas)
        
        return node
    
    def search(self, key):
        """Busca uma chave na Treap"""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Busca recursiva seguindo propriedade BST"""
        if node is None:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def delete(self, key):
        """Remove uma chave da Treap"""
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        """Remoção recursiva mantendo propriedades BST e Heap"""
        if node is None:
            return None
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Nó encontrado - realizar remoção
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Nó tem dois filhos - rotacionar para baixo baseado nas prioridades
                if node.left.priority > node.right.priority:
                    node = self._rotate_right(node)
                    node.right = self._delete_recursive(node.right, key)
                else:
                    node = self._rotate_left(node)
                    node.left = self._delete_recursive(node.left, key)
        
        return node
    
    def inorder_traversal(self):
        """Percurso em ordem (retorna chaves ordenadas)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Percurso em ordem recursivo"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Percurso em pré-ordem (mostra estrutura da árvore)"""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Percurso em pré-ordem recursivo"""
        if node is not None:
            result.append((node.key, node.priority))
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def is_empty(self):
        """Verifica se a Treap está vazia"""
        return self.root is None
    
    def height(self):
        """Calcula a altura da Treap"""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Cálculo recursivo da altura"""
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                      self._height_recursive(node.right))
    
    def size(self):
        """Conta o número de nós na Treap"""
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node):
        """Contagem recursiva de nós"""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def print_tree(self, node=None, level=0, prefix="Root: "):
        """Imprime a estrutura da árvore de forma visual"""
        if node is None:
            node = self.root
        
        if node is not None:
            print(" " * (level * 4) + prefix + str(node))
            if node.left is not None or node.right is not None:
                if node.left:
                    self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

def main():
    """Função de demonstração das operações da Treap"""
    print("=== Demonstração da Treap ===\n")
    
    # Criar uma nova Treap
    treap = Treap()
    
    # Inserir elementos
    elements = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]
    print("Inserindo elementos:", elements)
    for elem in elements:
        treap.insert(elem)
    
    print(f"\nTamanho da Treap: {treap.size()}")
    print(f"Altura da Treap: {treap.height()}")
    
    # Mostrar estrutura da árvore
    print("\nEstrutura da árvore:")
    treap.print_tree()
    
    # Percurso em ordem (elementos ordenados)
    print("\nPercurso em ordem (BST):", treap.inorder_traversal())
    
    # Percurso em pré-ordem (mostra prioridades)
    print("Percurso em pré-ordem (chave, prioridade):")
    for key, priority in treap.preorder_traversal():
        print(f"  {key}: {priority:.3f}")
    
    # Testar busca
    print("\n=== Testes de Busca ===")
    test_keys = [7, 20, 1, 25, 15]
    for key in test_keys:
        found = treap.search(key)
        print(f"Buscar {key}: {'Encontrado' if found else 'Não encontrado'}")
    
    # Testar remoção
    print("\n=== Testes de Remoção ===")
    remove_keys = [1, 15, 10]
    for key in remove_keys:
        print(f"\nRemoção de {key}:")
        treap.delete(key)
        print(f"Elementos após remoção: {treap.inorder_traversal()}")
        print(f"Tamanho: {treap.size()}")
    
    print("\nEstrutura final da árvore:")
    treap.print_tree()

if __name__ == "__main__":
    main()

