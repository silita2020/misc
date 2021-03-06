
def main():
    n = int(input("How many fibonacci numbers would you like? "))
    print(f"fib seq starting from f(1)       {fibonacciSequence(n)}")
    print(f"fib recursive starting from f(1) {fibonacciSequenceRecursive(n, [])}")
    print(f"fib seq starting from f(0)       {fibonacciSequence2(n)}")
    print(f"fib recursive starting from f(0) {fibonacciSequenceRecursive2(n, [])}")


def fibonacciSequence(n):
    """ F(n) = F(n-2) + F(n-1) for n > 2 and F(1) = F(2) = 1 """
    fib_seq = []
    for n in range(n):
        # base cases for F(1) and F(2) starting at index zero in the list
        if n < 2:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[n-2] + fib_seq[n-1])
    return fib_seq


def fibonacciSequenceRecursive(n, fib_seq):
    """ F(n) = F(n-2) + F(n-1) for n > 2 and F(1) = F(2) = 1 """

    if n == 0:
        return
    fibonacciSequenceRecursive(n - 1, fib_seq)

    # base cases for F(1) and F(2) starting at index zero in the list
    if n < 3:
        fib_seq.append(1)
    else:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    return fib_seq


def fibonacciSequence2(n):
    """F(0) = 0, F(1) = 1  and F(n) = F(n-2) + F(n-1) for n > 1"""
    fib_seq = []
    for n in range(n):
        # base cases for F(0) and F(1) starting at index zero in the list
        if n == 0:
            fib_seq.append(0)
        elif n == 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[n-2] + fib_seq[n-1])
    return fib_seq


def fibonacciSequenceRecursive2(n, fib_seq):
    """F(0) = 0, F(1) = 1  and F(n) = F(n-2) + F(n-1) for n > 1"""
    if n == 0:
        return
    fibonacciSequenceRecursive2(n - 1, fib_seq)
    # base cases for F(0) and F(1) starting at index zero in the list
    if n == 1:
        fib_seq.append(0)
    elif n == 2:
        fib_seq.append(1)
    else:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
    return fib_seq

main()