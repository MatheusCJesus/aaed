// Implementação de uma arvore vermelha e preta caída para a esquerda em Rust
// Autor: Matheus Cerqueira de Jesus
// Links para estudo: https://www.youtube.com/watch?v=DaWNuijRRFY&list=PL8iN9FQ7_jt6H5m4Gm0H89sybzR9yaaka&index=105&ab_channel=Programa%C3%A7%C3%A3oDescomplicada%7CLinguagemC


// Definição de cores
#[derive(Debug, Clone, Copy, PartialEq)]
enum Color {
    Red,
    Black
}

// Struct para representar um nó da árvore
#[derive(Debug)]
struct Node {
    value: u32,
    color: Color,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}

// Funções auxiliares para criar e manipular nós
impl Node {
    // Construtor básico
    fn new(value: u32) -> Self {
        Node {
            value,
            color: Color::Red, // Inicialmente vermelho
            left: None,
            right: None,
        }
    }
    
    // Contrutor com filhos
    fn with_children(value: u32, left: Option<Box<Node>>, right: Option<Box<Node>>) -> Self {
        Node {
            value,
            color: Color::Red, // Inicialmente vermelho
            left,
            right,
        }
    }

    fn get_color(&self) -> Color {
        self.color
    }

    fn invert_color(&mut self) {
        self.color = match self.color {
            Color::Red => Color::Black,
            Color::Black => Color::Red,
        };
    }

    fn invert_children_colors(&mut self) {
        if let Some(left) = &mut self.left {
            left.invert_color();
        }
        if let Some(right) = &mut self.right {
            right.invert_color();
        }
    }

    fn set_color(&mut self, color: Color) {
        self.color = color;
    }

    fn set_left(&mut self, left: Option<Box<Node>>) {
        self.left = left;
    }

    fn set_right(&mut self, right: Option<Box<Node>>) {
        self.right = right;
    }

    fn get_left(&self) -> &Option<Box<Node>> {
        &self.left
    }

    fn get_right(&self) -> &Option<Box<Node>> {
        &self.right
    }

    fn get_value(&self) -> u32 {
        self.value
    }

    fn is_red(&self) -> bool {
        self.color == Color::Red
    }

    fn is_black(&self) -> bool {
        self.color == Color::Black
    }

    fn is_leaf(&self) -> bool {
        self.left.is_none() && self.right.is_none()
    }

    fn rotate_left(&mut self) -> Option<Box<Node>> {
        if self.right.is_none() {
            return None;
        }

        let mut new_root = self.right.take().unwrap();
        
        self.right = new_root.left.take();
        
        // Create a replacement node to avoid ownership issues
        let mut temp = Node::new(self.value);
        std::mem::swap(&mut temp, self);
        
        new_root.left = Some(Box::new(temp));
        
        // Set colors appropriately
        new_root.color = self.color;
        if let Some(left_child) = &mut new_root.left {
            left_child.set_color(Color::Red);
        }

        Some(new_root)
    }

    
}

fn main() {
    println!("Hello, world!");
}
