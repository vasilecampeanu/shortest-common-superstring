import sys

from CalculateElapsedTime import *

def get_reads_overlap(read1, read2):
    """Returns the length of the overlap between two strings and the resulting concatenated string.

    Args:
        read1 (string): DNA read 1
        read2 (string): DNA read 2

    Returns:
        overlap_len (int): Teh overlap length
        overlap (string): The overlaped strings
    """

    overlap = ""
    overlap_len = -sys.maxsize
    read1_len = len(read1)
    read2_len = len(read2)

    for i in range(1, min(len(read1), len(read2)) + 1):
        if read1[read1_len - i:] == read2[:i]:
            if overlap_len < i:
                overlap_len = i
                overlap = read1 + read2[i:]

        if read1[:i] == read2[read2_len - i:]:
            if overlap_len < i:
                overlap_len = i
                overlap = read2 + read1[i:]

    return overlap_len, overlap

def find_shortest_superstring(reads_arr):
    """ Computes SCSP

    Args:
        reads_arr (list): Input array that contains the DNA reads

    Returns:
        reads_arr(string): Returns the shortest string that contains all the strings in the input array of DNA reads.
    """

    n = len(reads_arr)

    while n != 1:
        max_overlap_len = -sys.maxsize
        l, r = 0, 0
        reads_overlap = ""
    
        for i in range(n):
            for j in range(i + 1, n):
                overlap_len, overlap = get_reads_overlap(reads_arr[i], reads_arr[j])

                if max_overlap_len < overlap_len:
                    max_overlap_len = overlap_len
                    reads_overlap = overlap
                    l, r = i, j

        n -= 1

        if max_overlap_len == -sys.maxsize:
            reads_arr[0] += reads_arr[n]
        else:
            reads_arr[l] = reads_overlap
            reads_arr[r] = reads_arr[n]
    
    return reads_arr[0]

if __name__ == "__main__":
    elapsed_times = time_function(find_shortest_superstring,  num_runs=10)
    plot_elapsed_times(elapsed_times, title="Elapsed Time for My Function")
