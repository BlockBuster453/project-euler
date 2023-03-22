def next_fibonacci_number(previous_int, current_int):
    return previous_int + current_int

def sum_of_even_fibonacci_numbers():
    sum = 0
    fibonacci_numbers = [1, 1]
    while sum <= 4000000:
        last_index = len(fibonacci_numbers) - 1
        next_number = next_fibonacci_number(fibonacci_numbers[last_index], fibonacci_numbers[last_index - 1])
        if next_number % 2 == 0:
            sum += next_number
        fibonacci_numbers.append(next_number)
    return sum

if __name__ == '__main__':
    print(sum_of_even_fibonacci_numbers())
