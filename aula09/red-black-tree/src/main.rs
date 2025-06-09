// Implementação de uma arvore vermelha e preta caída para a esquerda em Rust
// Autor: Matheus Cerqueira de Jesus
// Links para estudo: https://www.youtube.com/watch?v=DaWNuijRRFY&list=PL8iN9FQ7_jt6H5m4Gm0H89sybzR9yaaka&index=105&ab_channel=Programa%C3%A7%C3%A3oDescomplicada%7CLinguagemC


// Struct para representar um nó da árvore
#[derive(Debug)]
struct Node {
    value: u32,
    color: u8, // 0 para vermelho, 1 para preto
    left: Option<Box<Node>>,
    right: Option<Box<Node>>,
}


fn main() {
    println!("Hello, world!");
}
