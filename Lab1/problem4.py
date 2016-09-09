import re
import enchant

IN_FILE = 'input.txt'
OUT_FILE = 'output.txt'

# Decodes message encrypted with shift cipher
def decode_shift_cipher(message):
    # 1. Preprocess message and setup dicts 
    message = message.lower()
    message = re.sub(r'[^a-zA-Z ]+', '', message)
    
    # 2. Set up dict objects used for processing 
    alph_dict = { 'a' : 0, 'b': 1, 'c': 2, 'd': 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 
                 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 
                 'r' : 17, 's' : 18 , 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25 }
    alph_dict_inv = { v: k for k, v in alph_dict.items() } # invert to allow reverse indexing 
    english_dict = enchant.Dict("en_US")
    shift_dict = {'key' : 0, 'valid_words' : 0, 'message': '' }
    
    # 2. Shift messasge 0-25 times, determine and record num valid words seen in shift_dict
    for key in range(0,26):            
        message_shift = [ char if char == ' ' else alph_dict_inv[ ( (alph_dict[char] + key) % 26 ) ] for char in message ]
        message_shift = ''.join(message_shift)
        valid_words = 0
        for word in message_shift.split(' '):
            if english_dict.check(word):
                valid_words += 1
        if valid_words >= shift_dict['valid_words']:
            shift_dict['key'] = key
            shift_dict['valid_words'] = valid_words
            shift_dict['message'] = message_shift
    return shift_dict


# Problem Driver
def main():
	message = open(IN_FILE).read()
	#message = 'uif rvjdl cspxo gpy kvnqt'
	print("Encoded message : ",  message , "\n")
	decoded_cipher = decode_shift_cipher(message)
	print(decoded_cipher['valid_words'] , " valid words found using shift cipher key : " , decoded_cipher['key'], "\n" )
	print("Decoded message : " , decoded_cipher['message'] , "\n" )
	open(OUT_FILE, 'w').write( decoded_cipher['message'] )

if  __name__ =='__main__':
    main()
