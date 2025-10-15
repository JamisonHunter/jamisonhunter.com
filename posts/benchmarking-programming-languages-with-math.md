# Benchmarking Programming Languages With Math

*October 14, 2025*

One of my favorite ways to learn a new programming language is to write a simple math project! Well, it's going to sound complicated but it's really not that bad. What I like to do is write a progam that will calculate the Riemann Zeta function for a given value of s and a given number of summations.

Let's take a loook at this in Python in order to understand it better. 

```python
import time

def main():
    print("This program calculates an estimate of the Riemann Zeta function.")
    try: 
        s = int(input("Enter your s value: "))
    except ValueError:
            print("Please enter a number.")
            exit()

    try:
        sum = int(input("Enter the number of summations: "))
    except ValueError:
            print("Please enter a number.")
            exit()

    start = time.perf_counter()
    total = 0
    for i in range(sum):
        total += 1/((i + 1)**s)
    print(f"Value: {total}")
    end = time.perf_counter()
    elapsed_s = end - start

    if elapsed_s >= 1:
        print(f"Time elapsed: {elapsed_s:.3f} s")
    elif elapsed_s >= 0.001:
        print(f"Time elapsed: {elapsed_s * 1e3:.3f} ms")
    else:
        print(f"Time elapsed: {elapsed_s * 1e6:.3f} µs")

if __name__ == "__main__":
    main()
```

The main part of this that we want to focus on is the for loop. That's where the real project is actually happening!

The Riemann Zeta function is basically the sum of exponentials divided by one where the base of each exponential increases by one as it is summed to infinity. As can be seen, s is the exponent.

I don't know about your computer but mine can't run an infinite number of summations so I decided to make that an input variable! 

If you look at the code sandwiching the for loop, you'll see the lines that I used to get the amount of time that it took for the loop to execute. This is the most important part for actually benchmarking the different programs.

If the Reimann Zeta function is still a bit confusing, I'd encourage you to look it up. There are some really interesting videos about it! 

The other languages that I compared were Rust and C. Let's take a brief look at the Rust code! 

```rust
use std::io::{stdin, stdout, Write};
use std::time::Instant;

fn get_user_inputs(mut s: String, message: String) -> i128 {
    print!("Please enter your {} value: ", message);
    let _=stdout().flush();
    stdin().read_line(&mut s).expect("You did not enter a correct string");
    s = s.trim().to_owned();
    let return_int: i128;
    if let Ok(_n) = s.parse::<i128>() {
        return_int = s.parse::<i128>().unwrap();
        if return_int < 0 {
            eprintln!("You may not enter a negative number.");
            std::process::exit(0);
        }
        return return_int;
    }
    else {
        eprintln!("Please enter a valid number.");
        std::process::exit(0);
    }
}

fn main() {
    println!("This program calculates an estimate of the Riemann Zeta function.");
    let s = String::new();
    let summations = String::new();
    let s_message: String = "s".to_string();
    let summations_message: String = "summation".to_string();
    let int_s = get_user_inputs(s, s_message);
    let int_summations = get_user_inputs(summations, summations_message);
    let start = Instant::now();
    let mut total: f64 = 0.0;
    let mut i: i128 = 1;
    while i <= int_summations {
        total += 1 as f64/(i.pow(int_s.try_into().unwrap())) as f64;
        i += 1;
    }

    println!("Value: {}", total);
    let duration = start.elapsed();
    println!("Time elapsed: {:?}", duration);
}
```

Now for the C program!

```c
#include <stdio.h>
#include <math.h>
#include <time.h>

int main() {
    printf("This program calculates an estimate of the Riemann Zeta function.\n");
    int s;

    printf("Enter your s value: ");
    if (scanf("%d", &s) != 1 || s <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    int sum;
    printf("Enter your number of summations: ");
    if (scanf("%d", &sum) != 1 || sum <= 0) {
        printf("Please enter a positive integer.\n");
        return 1;
    }

    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    double total = 0.0; 
    for (int i = 0; i < sum; i++) {
        total += 1.0 / pow(i + 1, s); 
    }

    printf("Value: %f\n", total);
    clock_gettime(CLOCK_MONOTONIC, &end);
    double elapsed_s = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;
    
    if (elapsed_s >= 1.0) {
        printf("Time elapsed: %.3f s\n", elapsed_s);
    } else if (elapsed_s >= 0.001) {
        printf("Time elapsed: %.3f ms\n", elapsed_s * 1e3);
    } else {
        printf("Time elapsed: %.3f µs\n", elapsed_s * 1e6);
    }
    return 0;
}
```

For these programs, I set s equal to three and I set the number of summations to one billion when benchmarking. 

On my system, Rust was by far the fastest to execute with C being a close second. It's not shocking to say that Python ended up in last by a huge margin. Here are the values. 

## Execution Time

- **Rust: 4.4 Seconds**
- **C: 7.2 Seconds**
- **Python: 144.5 Seconds**
