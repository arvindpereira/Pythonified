#!/usr/bin/env python
''' A few methods of producing permutations of a string '''

def getPermutation( str, i, n, perms ):
    ''' A recursive formulation to get all the permutations
    of a string '''
    if( i== n ):
        perms.append( bytearray(str) )
    else:
        for j in range( i, n ):
            str[i],str[j] = str[j],str[i] # Swap once
            getPermutation( str, i+1, n , perms ) # Permute
            str[i],str[j] = str[j],str[i] # Swap back
    return perms


def permutations(iterable, r=None):
    ''' Find permutations of an iterable (n choose r)
        This is essentially the code from 
        http://docs.python.org/2/library/itertools.html#itertools.permutations
    '''
    pool = tuple(iterable) # Get a tuple of the iterable
    n = len( pool )
    r = n if r is None else r # can this get any clearer (even better than ? : )
    if r > n:
        return
    indices = range( n ) # Create a list of indices which we will permute
    cycles  = range( n, n-r, -1 ) # Holds a list with # of indices we will cycle through
    yield tuple(pool[i] for i in indices[:r]) # Yield the first un-permuted sequence
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1 
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n-i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
        
def permsUsingItertools( iterable, r=None ):
    import itertools
    return itertools.permutations(iterable,r)
    
def __main__():
    # Find the permutations
    print 'Using our simple permutation method:'
    perms = getPermutation( bytearray("abcd"),0,4, [])
    for val in perms:
        print val
        
    print 'Using the generator (and nCr) i.e. 4 choose 3:'
    for perm_gen in permutations("abcd", 3):
        print bytearray(perm_gen)
        
    print 'Using itertools to get 4 choose 2:'
    import itertools
    for perm_gen in itertools.permutations("abcd", 2):
        print bytearray( perm_gen )

if __name__=='__main__':
    __main__()
    