'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
word = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

def maxProduct(word, maxProd):
    prod = 1
    maxProd = 0
    sel_length = 0
    for i in range(len(word)):
        print(word[i - sel_length: i], "\t", prod, "\t", maxProd)
        if word [i] == '0':
            if len(word) > i + 25:
                maxProduct(word[i+13:], 0)
        else:
            prod *= int(word[i])
            sel_length += 1
            print ("MUL ", sel_length, end=" ")
            if sel_length == 14:
                prod /= int(word[i-13])
                sel_length -= 1
                print ("DIV ", sel_length, end = " ")
            if sel_length == 13:
                if maxProd < prod:
                    maxProd = prod
                    
maxProduct(word, 0)








# # word = "1111111111111" + word
# prod = 1
# sel_length = 0
# # last_zero_index_plus13 = -1
# maxProd = 0
# index = 0
# while(index < len(word) - 12):
    # print(word[index - sel_length: index], "\t", prod, "\t", maxProd)
    # if word[index] == '0':
        # sel_length = 0
        # prod = 1
        # index += 13
        # continue
    # prod *= int(word[index])
    # sel_length += 1
    # print ("MUL ", sel_length, end=" ")

    # if sel_length == 14:
        # prod /= int(word[index - 13])
        # sel_length -= 1
        # print ("DIV ", sel_length, end = " ")

    # if sel_length == 13:
        # if maxProd < prod:
            # maxProd = prod
    # index += 1
# print(maxProd)
