use std::collections::{linked_list};
use rand::Rng;
use std::time;

// Implementação de uma tabela hash simples com função hash da divisão e endereçamento por sondagem linear em Rust
// Autor: Matheus Cerqueira de Jesus
// Links: https://www.geeksforgeeks.org/dsa/c-program-hashing-chaining/, https://www.youtube.com/watch?v=BDYiADxBqXA&list=PL8iN9FQ7_jt6H5m4Gm0H89sybzR9yaaka&index=97&ab_channel=Programa%C3%A7%C3%A3oDescomplicada%7CLinguagemC

// Lista encadeada:
// - https://doc.rust-lang.org/std/collections/struct.LinkedList.html


#[derive(Debug)]
struct LinkedListHashTable {
    table: Vec<linked_list::LinkedList<usize>>,
    size: usize,
}

impl LinkedListHashTable {
    fn new(size: usize) -> Self {
        LinkedListHashTable {
            table: vec![linked_list::LinkedList::new(); size],
            size,
        }
    }
    
    fn insert(&mut self, key: usize) -> usize {
        
        let index = Self::hash_division(key, self.size);
        
        self.table[index].push_back(key);
        
        index
    }
    
    fn search(&self, key: usize) -> Option<usize> {
        
        let index = Self::hash_division(key, self.size);
        
        for &item in self.table[index].iter() {
            
            if item == key {
                return Some(index);
            }
            
        }
        
        None // Chave não encontrar
    }
    
    // Função hash da divisão
    fn hash_division(key: usize, size: usize) -> usize {
        key % size
    }
}

struct OpenAddressingHashTable {
    table: Vec<Option<usize>>,
    size: usize,
}
impl OpenAddressingHashTable {
    fn new(size: usize) -> Self {
        OpenAddressingHashTable {
            table: vec![None; size],
            size,
        }
    }

    fn insert(&mut self, key: usize) -> usize {
        let mut i: usize = 0; // Start with the first attempt
        let mut index = Self::hash_division(key, i, self.size);

        while self.table[index].is_some() {
            i += 1; // Increment the probe attempt
            index = Self::hash_division(key, i, self.size); // Calculate next position
            
            // Impedir loop infinito - se já verificamos todas as posições, sair
            if i >= self.size {
                panic!("Hash table is full");
            }
        }

        self.table[index] = Some(key);
        index
    }

    fn search(&self, key: usize) -> Option<usize> {
        let mut i: usize = 0;
        let mut index = Self::hash_division(key, i, self.size);

        while let Some(item) = self.table[index] {
            if item == key {
                return Some(index);
            }
            
            i += 1;
            index = Self::hash_division(key, i, self.size);

            // Impedir loop infinito - se já verificamos todas as posições, sair
            if i >= self.size {
                break;
            }
        }

        None // Chave não encontrada
    }

    fn hash_division(key: usize, attempt: usize, size: usize) -> usize {
        (key % size + attempt) % size
    }
}

fn main() {

    // Função para gerar numeros aleatórios
    fn ramdom_number(max_number: usize) -> usize {
        let mut rng = rand::rng();
        rng.random_range(0..max_number)
    }

    // Inserindo 100.000 números aleatórios na tabela hash por encadeamento
    let mut hash_table = LinkedListHashTable::new(50_000);
    let mut start = time::Instant::now();
    for _ in 0..100_000 {
        let number = ramdom_number(100_000);
        hash_table.insert(number);
    }
    let mut duration = start.elapsed();

    println!("Tempo de inserção: {:?}", duration);

    start = time::Instant::now();
    let searched = hash_table.search(10_000);
    duration = start.elapsed();
    println!("Tempo de busca: {:?}", duration);
    if searched != None {
        println!("Chave 10.000 encontrada");
    }
    else {
        println!("Chave 10.000 não encontrada");
    }

    // Inserindo 100.000 números aleatórios na tabela hash por endereçamento aberto
    let mut open_addressing_table = OpenAddressingHashTable::new(100_000);
    start = time::Instant::now();
    for _ in 0..100_000 {
        let number = ramdom_number(100_000);
        open_addressing_table.insert(number);
    }
    duration = start.elapsed();
    println!("Tempo de inserção: {:?}", duration);

    start = time::Instant::now();
    let searched = open_addressing_table.search(10_000);
    duration = start.elapsed();
    println!("Tempo de busca: {:?}", duration);
    if searched != None {
        println!("Chave 10.000 encontrada");
    }
    else {
        println!("Chave 10.000 não encontrada");
    }
}
