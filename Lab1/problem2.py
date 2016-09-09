IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'

def addition_multiplication_ring(m, op, x, y):
    if op == "*":
        result = ( x * y) % m
    else:
        result = ( x + y) % m
    return result

# Problem Driver
def main():
	args = open(IN_FILE).read().splitlines()
	#print(args)
	result = addition_multiplication_ring( int(args[0]), args[1], int(args[2]), int(args[3]) )    
	#print( "result: ", result)
	open(OUT_FILE, 'w').write( str(result) )

if  __name__ =='__main__':
    main()
