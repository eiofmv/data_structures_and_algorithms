# python3
from sys import stdin


def is_k_optimal(k, reads):
    kmers = set()
    for cur_read in reads:
        for i in range(0, len(cur_read) - k + 1):
            kmers.add(cur_read[i:i + k])

    prefixes = set()
    suffixes = set()

    for cur_kmer in kmers:
        prefixes.add(cur_kmer[:-1])
        suffixes.add(cur_kmer[1:])

    return prefixes == suffixes


if __name__ == '__main__':
    reads = stdin.read().split()
    k = len(reads[0]) - 1

    while not is_k_optimal(k, reads) and k:
        k -= 1

    print(k)