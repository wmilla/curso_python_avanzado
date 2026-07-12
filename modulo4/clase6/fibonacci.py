def fibonacci(n):
    fib_series = [1, 2]
    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series


if __name__ == "__main__":
    n = int(input("Ingrese nros de la serie fibonacci: "))
    print(fibonacci(n))
