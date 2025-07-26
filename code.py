def count_set_bits(n):
    count = 0
    while n > 0:
        if n & 1:  # check last bit
            count += 1
        n = n >> 1  # right shift to check next bit
    return count
