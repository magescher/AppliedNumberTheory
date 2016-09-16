from __future__ import division
from math import factorial
import sys
import os
import math
import numpy as np
import re

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

# Input: A cyclic group G of order p, having a generator g and an element h.
# Output: A value x st g^x congr h modulo p
# Run-time : O( n^(1/2) )
def baby_step_giant_step(p, g, h):

    # 1. Compute limits
    m = math.ceil( math.sqrt(p) )
    
    # 2. Giant Step
    giant_step = {}
    for i in range ( 0, m ):
        giant_step[ fast_exponentiation( g , i) % p ] = i
    
    # 3. Baby Step / Intersection detection
    g_inv = inverse_mod_p( g, p )
    u = g_inv ** m 
    for i in range ( 0, m ):
        baby_step = ( ( u ** i ) * h ) % p 
        if baby_step in giant_step:
            x = m * i + giant_step[ baby_step ]
            return x

#print(baby_step_giant_step(17,3,1))    
#print(baby_step_giant_step(31,3,6))

# Test file : p = 5, g = 2 , h = 1
def main():
    args = open('input.txt').read().splitlines()
    p = int(args[0]) ; g = int(args[1]) ; h = int(args[2])  
    result = baby_step_giant_step( p, g, h )
    print( "Result of Babystep Giantstep ( p = ", p, " g = ", g, " h = ", h, ") :\n ", result)
    open('output.txt', 'w').write( str(result) )
    
if  __name__ =='__main__':
    main()

