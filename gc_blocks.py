"""Slice the sequence into blocks of defined sizes"""
def block_slice(seq, block_size):
    for i in range(0, len(seq), block_size):
        return seq[i:i+block_size]
            print((seq.count(G) + seq.count(C)) / (block_size))

"""Determine the GC content of each block"""
