#Hex to binary converter 

def hexToBinary(hexInput):
    try:
        #convert hex to integer 
        decimal = int(hexInput, 16)

        #convert decimal to eight bit binary ('08b')
        binary = format(decimal, '08b')

