'''
The following iterative sequence is defined for the set of positive integers:

    n => n/2 (n is even)
    n => 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 => 40 => 20 => 10 => 5 => 16 => 8 => 4 => 2 => 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
'''
chain_lengths = {1:1}
lengths_found = 1
max_length = 1
def find_chain_length(i):
    global lengths_found, max_length, max_index
    if i in chain_lengths:
        return
    # print("find_chain_length( ", i , " ) \t", lengths_found)
    chain = [i]
    while True:
        # print("check( ", i, ")")
        if i % 2 == 0: # even
            i /= 2
        else:
            i = 3 * i + 1
        if i not in chain_lengths:
            chain.append(i)
        else:
            break
    length  = chain_lengths[i] + 1
    for i in chain[::-1]:
        if i < 100000:
            lengths_found += 1
            if length > max_length:
                max_length = length
                max_index = i
            chain_lengths[i] = length
            length += 1
    print(chain)

# index =  1
# while(lengths_found < 99999):
    # index += 1
    # find_chain_length(index)
# find_chain_length(10)
# print(chain_lengths.items())
# find_chain_length(13)
find_chain_length(81906)
print(chain_lengths.items())
print(max_length)
print(max(chain_lengths.values()))
print(max_index)
