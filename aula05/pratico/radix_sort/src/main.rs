

fn max_elem(arr: & [usize]) -> usize {
    
    let mut max: usize = 0;
    
    for &elem in arr.iter() {
        if elem > max {
            max = elem;
        }
    }
    
    return max;
    
}

fn create_count_arr(arr: &[usize], size: usize) -> Vec<i32> {
    
    let mut count_arr = vec![0; size];

    for i in 0..size {
        
        count_arr[arr[i]] += 1;

    }

    return count_arr;

}

fn calc_prefix_sum()

fn counting_sort(arr: &mut [usize], size: usize, base: u32) {

    let max_value = max_elem(arr);
    let mut temp_arr = vec![0, size];
    
    let count_arr: Vec<i32> = create_count_arr(arr, size);


}

// fn radix_sort(arr: &mut [u32], size: u32) {
//     let mut max: u32;
//     let temp_arr: [u32; size] = [0, size];
// }

fn main() {
    println!("Hello, world!");

    let array: [usize; 5] = [10, 100, 1000, 500, 200];
    println!("Max element is {}", max_elem(&array));
}
