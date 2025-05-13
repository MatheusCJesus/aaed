use std::process::Output;



fn max_elem(arr: & [usize]) -> usize {
    
    let mut max: usize = 0;
    
    for &elem in arr.iter() {
        if elem > max {
            max = elem;
        }
    }
    
    return max;
    
}

fn create_count_arr(arr: &[usize], size: usize, base: usize, div: usize) -> Vec<i32> {
    
    let mut count_arr = vec![0; size];

    for i in 0..size {

        let pos = (arr[i] / div) % base;
        
        count_arr[pos] += 1;

    }

    return count_arr;

}

fn calc_prefix_sum(arr: & [usize], size: usize) -> Vec<usize> {
    let mut prefix_sum = vec![0; size];
    prefix_sum[0] = arr[0];
    for i in 1..size {
        prefix_sum[i] = prefix_sum[i - 1] + arr[i];
    }

    return prefix_sum;
}

fn counting_sort(arr: &mut [usize], size: usize, base: usize, div: usize) {

    let max_value = max_elem(arr);
    let mut temp_arr = vec![0, size];
    
    let count_arr: Vec<i32> = create_count_arr(arr, size);

    let prefix_sum_arr = calc_prefix_sum(arr, size);

    let output_arr: Vec<usize> = vec![0; size];

    for i in 0..size {
        let pos = (arr[i] / div) % base;

        a
    }

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
