#Hex to binary converter 
hexadecimal = input("Enter Hex: ")
def hexToBinary(hexInput):
    try:
        #convert hex to integer 
        decimal = int(hexInput, 16)

        #convert decimal to eight bit binary ('08b')
        binary = format(decimal, '08b')

        print(binary)
        #return
        return binary
    except ValueError:
        return "Invalid Hex"

    
hexToBinary(hexadecimal)