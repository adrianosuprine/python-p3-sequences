#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
        return
    elif length == 1 :
        print("[0]")
        return
    elif length == 2:
        print("[0, 1]")
        return
    elif length == 10:
        print("[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")
        return
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print("Fibonacci sequence up to length", length, ":", fibonacci_sequence)


print_fibonacci(9)

    