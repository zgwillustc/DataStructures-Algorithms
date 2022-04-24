def factorial_iteration(n: int) -> int:
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

def factorial_recursion(n: int) -> int:
    if n == 0 # Base condition - terminate the recursion
        return 1
    return n * factorial_recursion(n-1)

def main():
    print('Iteration:')
    print(factorial_iteration(1))
    print(factorial_iteration(3))
    print('Recursion:')
    print(factorial_recursion(1))
    print(factorial_recursion(3))

if __name__ == '__main__':
    main()
