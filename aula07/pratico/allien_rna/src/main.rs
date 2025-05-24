
fn calc_rnaa_connections(rnaa: &str) -> u32 {

    let mut connections = 0;
    
    fn get_base_complement(base: char) -> &'static char {

        match base {
            'B' => &'S',
            'S' => &'B',
            'C' => &'F',
            'F' => &'C',
            _ => panic!("Invalid base"),
        } 
    }
    

    let mut stack: Vec<char> = vec![];

    for base in rnaa.chars() {
        
        if stack.is_empty() {
            stack.push(base);
        }
        else {
            if stack.last().unwrap() == get_base_complement(base) {
                stack.pop();
                connections += 1;
            }
            else {
                stack.push(base);
            }
        }

    }
    return connections;
}

fn main() {
    

    let rnaa = "BSCFSCB";
    let connections = calc_rnaa_connections(rnaa);
    println!("Number of connections: {}", connections);
    
    // Test cases
    assert_eq!(calc_rnaa_connections("BSCFSCB"), 2);
    assert_eq!(calc_rnaa_connections("BSCF"), 2);
    assert_eq!(calc_rnaa_connections("BS"), 1);
    assert_eq!(calc_rnaa_connections("BCF"), 1);
}