from __future__ import division
from math import factorial
import sys
import os
import math
import numpy as np
import re
import enchant

# computes g^x using fast exponentiation
def fast_exponentiation(g, x):
    if x == 0:
        return 1
    elif x % 2 == 1:
        return g * fast_exponentiation( g, x-1 )
    else:
        exp = fast_exponentiation( g, x/2)
        return exp * exp

# Computes a inverse mod p 
# using Euclidean Algorithm and fact that 
def inverse_mod_p( a, p ):
    inv = u_v_gcd(a,p)['u']
   
    if inv < 0 :
        #print( "Negative inverse : ", inv, " Normalizing to postive inverse : " , inv % p, " p = ", p)
        inv = inv % p
    
    return inv

# TODO: current does not handle b = 0 . fix it
# given a and b, returns gcd and u,v inc Integer st au + bv = gcd(a,b)
def u_v_gcd(a, b):
    u = 1; gcd = a; x = 0; y = b
    while True:
        if y == 0:
            v = ( gcd - ( a * u ) ) // b
            ret = {}
            ret['u'] = u ; ret['v'] = v ; ret['gcd'] = gcd
            return ret
        q = gcd // y 
        r = gcd % y
        s = u - ( q * x )
        u = x ; x = s; gcd = y ; y = r
    
# Encrypts plaintext using elgamal encription
# returns ( c1, c2 )
# where c1 = ( g ^ k ) mod p
#       c2 = ( m * A ^ k ) mod p
#            where A = (g ^ a ) 
def elgamal_encryption(p, g, m, g_pow_a):
    y = np.random.randint( 1, p )
    print("y : ", y)
    c1 = fast_exponentiation( g_pow_a, y)
    c2 = c1 * inverse_mod_p( m, p)
    return ( c1, c2 )

def main():
    args = open('input.txt').read().splitlines()
    p = int(args[0]); g = int(args[1]) ; m = int(args[2]) ; g_pow_a = int(args[3]) 
    result = elgamal_encryption( p, g, m, g_pow_a )
    print( "Elgamal Encryption with p = ", p, ", g = ", g, ", m = ", m, ", g_pow_a = ", g_pow_a, " :\n \t e(m) = ", result)
    open('output.txt', 'w').write( str(result) )
    
if  __name__ =='__main__':
    main()
