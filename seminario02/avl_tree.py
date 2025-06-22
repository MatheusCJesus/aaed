# Implementação de uma árvore AVL (Adelson-Velsky e Landis)
# Autor: Matheus Cerqueira de Jesus

class AVLNode:
    """Nó da árvore AVL que armazena chave, altura e referências para filhos"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
    
    def __str__(self):
        return f"({self.key}, h={self.height})"

class AVLTree:
    """
    Implementação de árvore AVL
    - Propriedade BST: chaves seguem ordenação de árvore binária de busca
    - Propriedade AVL: diferença de altura entre subárvores ≤ 1
    """
    
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        """Retorna a altura do nó (0 se None)"""
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        """Calcula o fator de balanceamento do nó"""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        """Atualiza a altura do nó baseada nas alturas dos filhos"""
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), 
                                 self._get_height(node.right))
    
    def _rotate_right(self, z):
        """Rotação à direita"""
        y = z.left
        T3 = y.right
        
        # Realizar rotação
        y.right = z
        z.left = T3
        
        # Atualizar alturas
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_left(self, z):
        """Rotação à esquerda"""
        y = z.right
        T2 = y.left
        
        # Realizar rotação
        y.left = z
        z.right = T2
        
        # Atualizar alturas
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def insert(self, key):
        """Insere uma chave na árvore AVL"""
        self.root = self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """Inserção recursiva mantendo propriedade AVL"""
        # Passo 1: Inserção normal BST
        if node is None:
            return AVLNode(key)
        
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            # Chaves duplicadas não são permitidas
            return node
        
        # Passo 2: Atualizar altura do nó atual
        self._update_height(node)
        
        # Passo 3: Obter fator de balanceamento
        balance = self._get_balance(node)
        
        # Passo 4: Se desbalanceado, há 4 casos possíveis
        
        # Caso Esquerda-Esquerda
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)
        
        # Caso Direita-Direita
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)
        
        # Caso Esquerda-Direita
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Caso Direita-Esquerda
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def search(self, key):
        """Busca uma chave na árvore AVL"""
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
    
    def _get_min_value_node(self, node):
        """Encontra o nó com menor valor (mais à esquerda)"""
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)
    
    def delete(self, key):
        """Remove uma chave da árvore AVL"""
        self.root = self._delete_recursive(self.root, key)
    
    def _delete_recursive(self, node, key):
        """Remoção recursiva mantendo propriedade AVL"""
        # Passo 1: Remoção normal BST
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # Nó a ser deletado encontrado
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Nó com dois filhos: obter sucessor em ordem
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        
        # Passo 2: Atualizar altura do nó atual
        self._update_height(node)
        
        # Passo 3: Obter fator de balanceamento
        balance = self._get_balance(node)
        
        # Passo 4: Se desbalanceado, há 4 casos possíveis
        
        # Caso Esquerda-Esquerda
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Caso Esquerda-Direita
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Caso Direita-Direita
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Caso Direita-Esquerda
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
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
            result.append((node.key, node.height))
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def is_empty(self):
        """Verifica se a árvore está vazia"""
        return self.root is None
    
    def height(self):
        """Retorna a altura da árvore"""
        return self._get_height(self.root)
    
    def size(self):
        """Conta o número de nós na árvore"""
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node):
        """Contagem recursiva de nós"""
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
    
    def is_balanced(self):
        """Verifica se a árvore está balanceada (propriedade AVL)"""
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node):
        """Verificação recursiva de balanceamento"""
        if node is None:
            return True
        
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return False
        
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))
    
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
    """Função de demonstração das operações da árvore AVL"""
    print("=== Demonstração da Árvore AVL ===\n")
    
    # Criar uma nova árvore AVL
    avl = AVLTree()
    
    # Inserir elementos
    elements = [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8]
    print("Inserindo elementos:", elements)
    for elem in elements:
        avl.insert(elem)
    
    print(f"\nTamanho da árvore: {avl.size()}")
    print(f"Altura da árvore: {avl.height()}")
    print(f"Árvore balanceada: {avl.is_balanced()}")
    
    # Mostrar estrutura da árvore
    print("\nEstrutura da árvore:")
    avl.print_tree()
    
    # Percurso em ordem (elementos ordenados)
    print("\nPercurso em ordem (BST):", avl.inorder_traversal())
    
    # Percurso em pré-ordem (mostra alturas)
    print("Percurso em pré-ordem (chave, altura):")
    for key, height in avl.preorder_traversal():
        print(f"  {key}: altura {height}")
    
    # Testar busca
    print("\n=== Testes de Busca ===")
    test_keys = [7, 20, 1, 25, 15]
    for key in test_keys:
        found = avl.search(key)
        print(f"Buscar {key}: {'Encontrado' if found else 'Não encontrado'}")
    
    # Testar remoção
    print("\n=== Testes de Remoção ===")
    remove_keys = [1, 15, 10]
    for key in remove_keys:
        print(f"\nRemoção de {key}:")
        avl.delete(key)
        print(f"Elementos após remoção: {avl.inorder_traversal()}")
        print(f"Tamanho: {avl.size()}")
        print(f"Altura: {avl.height()}")
        print(f"Balanceada: {avl.is_balanced()}")
    
    print("\nEstrutura final da árvore:")
    avl.print_tree()

if __name__ == "__main__":
    main()
