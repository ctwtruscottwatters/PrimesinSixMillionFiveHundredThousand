# -*- coding: utf-8 -*-
"""
WHAT ARE THE FIRST OCCURING nTH PRIMES?
Charles Thomas Wallace Truscott

CSV to generate prime and the index in the number system at which they occur

Authored while sitting MIT Computational Thinking using Python  (MIT OCW 6.0001 and 6.0002) via edX.org

"""

def return_primes():
    fh = open("CSVPrimesCharlesTruscott.txt", "w+")
    fh.write("\nCharles Thomas Wallace Truscott Watters. CSV of prime indexes\n")
    primes = []
    count = 1
    fh.write("2, {}\n".format(count))
    primeFound = False
    for x in range(2, 10000001, 1):
        for y in range(2, x, 1):
            if x % y == 0:
                primeFound = False
                break
            else:
                primeFound = True
        if primeFound == True:
            count += 1
            print("{}, {}".format(x, count))
            fh.write("{}, {}\n".format(x, count))
        primeFound = False
#        print("upTo: {}".format(x))            
#    fh.close()
def main():
    return_primes()
    
if __name__ == "__main__": main()
