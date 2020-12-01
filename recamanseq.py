def main():
    n = int(input("Please enter a number "))
    print(recamanSequence(n))


def recamanSequence(a):
# Recaman Sequence Starting from zero, the n'th term a(n) is the previous term minus n 
# i.e a(n) = a(n-1) - n but only if this is both positive and has not been previousely generated. 
# If the conditions don't hold then a(n) = a(n-1) + n

    seq = [0]  # base case
    for n in range(1, a):
        x = seq[-1] - n
        if x >= 0 and x not in seq:
                seq.append(x)
        else:
            seq.append(seq[-1] + n)
    return seq


main()
