IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'

# Returns gcd(x,y) using Euclidean algorithm
# Uses fact that (1) m = nq + r where 0 <= r < n ( for m,n,q,r in Z )
#                (2) gcd(m,n) = gcd(n,r)    
def gcd(x,y):
    # slight performance optimization ( x > 0 added to account neg num)
    if y > x and x > 0 :
        return gcd(y,x)
    elif x % y == 0:
        return abs(y)
    else:
        return abs(gcd( y , x % y ))

# Problem Driver
def main():
    args = open(IN_FILE).read().splitlines()
    gcd_euc = gcd( int(args[0]), int(args[1]) )
    print( "gcd(", int(args[0]), ",", int(args[1]), ") = ", gcd_euc )
    open('OUT_FILE', 'w').write( str(gcd_euc) )

if  __name__ =='__main__':
    main()
