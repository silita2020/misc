
def main():
    a = [778, 783, 788, 793, 2460, 5794, 5799, 5804, 5600]
    #a = [778]
    #a = []
    d = 5
    print(maxConsecutiveSeq(a, d))


def maxConsecutiveSeq(a, d):
    seq_num = 1
    seq_grp = {}
    for n in range(len(a)-1, -1, -1):
        
        # base case
        if n == len(a)-1:
            seq_grp[seq_num] = 1
        
        if a[n] == a[n - 1] + d:
            # Increment number of sequences for this group
            if seq_num in seq_grp:
                seq_grp[seq_num] = seq_grp[seq_num] + 1
            else:
                seq_grp[seq_num] = 1
        else:
            # Start a new sequence grouping
            seq_num += 1
            seq_grp[seq_num] = 1
    return 0 if len(seq_grp) == 0 else max(seq_grp.values())


main()