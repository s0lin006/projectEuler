'''
Problem 21
Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
'''

def isEven(n):
    if ( n%2 == 0):
        return n
    else:
        return 0

def f(n):
    i = 1
    j = 2
    temp = 0
    sum = 0
    
    while( i < n ):
        #print(i)
        sum = sum + isEven(i)
        temp = i+j
        i = j
        j = temp

    print(sum)
    return

#i = 4000000
f(4000000)