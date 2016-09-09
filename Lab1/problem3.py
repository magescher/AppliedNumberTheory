IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'

# computes g^x using fast exponentiation
def fast_exponentiation(g, x):
    if x == 0:
        return 1
    elif x % 2 == 1:
        return g * fast_exponentiation( g, x-1 )
    else:
        exp = fast_exponentiation( g, x/2)
        return exp * exp


def main():
    args = open(IN_FILE).read().splitlines()
    exp = fast_exponentiation( int(args[1]),int(args[2]) )  
    result = exp % int(args[0])
    #print( "result: ", result)
    open(OUT_FILE, 'w').write( str(result) )
    
if  __name__ =='__main__':
    main()
