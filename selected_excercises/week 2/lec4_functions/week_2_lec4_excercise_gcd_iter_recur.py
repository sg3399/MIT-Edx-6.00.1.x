#interative code
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test= min(a,b)
    while test>0:
        if a%test==0 and b%test==0:
            break
        else:
            test-=1
    return test  

gcdIter(2,12)
gcdIter(6,12)
gcdIter(9,12)
gcdIter(17, 12)

#recursive code
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)


gcdRecur(2,12)
gcdRecur(6,12)
gcdRecur(9,12)
gcdRecur(17, 12)