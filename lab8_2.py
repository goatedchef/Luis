# Function to convert a binary number (input as a string)
# into a decimal number
def bin_to_decimal(binary):
    # Initialize accumulator
    decimal = 0
    high_power = len(binary) - 1
    i = high_power
    # Loop for the length of the string
    while i>= 0:
        # Compute the power of 2 for the position in the binary number
        
        # Add the power of 2 to the decimal if there is a 1 in the position
        if binary[i] == '1':
            power = high_power - i
            decimal = decimal + 2**power
        i = i-1
    return decimal

# Function to look up the ASCII representation of a capital letter
# Note: This function only considers capital letters and a space character
def ascii_lookup(ch):
    if ch == 'A':
        return "01000001"
    elif ch == 'B':
        return "01000010"
    elif ch == 'C':
        return "01000011"
    elif ch == 'D':
        return "01000100"
    elif ch == 'E':
        return "01000101"
    elif ch == 'F':
        return "01000110"
    elif ch == 'G':
        return "01000111"
    elif ch == 'H':
        return "01001000"
    elif ch == 'I':
        return "01001001"
    elif ch == 'J':
        return "01001010"
    elif ch == 'K':
        return "01001011"
    elif ch == 'L':
        return "01001100"
    elif ch == 'M':
        return "01001101"
    elif ch == 'N':
        return "01001110"
    elif ch == 'O':
        return "01001111"
    elif ch == 'P':
        return "01010000"
    elif ch == 'Q':
        return "01010001"
    elif ch == 'R':
        return "01010010"
    elif ch == 'S':
        return "01010011"
    elif ch == 'T':
        return "01010100"
    elif ch == 'U':
        return "01010101"
    elif ch == 'V':
        return "01010110"
    elif ch == 'W':
        return "01010111"
    elif ch == 'X':
        return "01011000"
    elif ch == 'Y':
        return "01011001"
    elif ch == 'Z':
        return "01011010"
    elif ch == ' ':
        return "00100000"
    else:
        return ''


def rotateRight(string):
    lastchar = string[len(string)- 1]
    string2 = lastchar + string[0:len(string)-1]
    return string2

# Function to compute the 8-bit checksum of a string
def checksumR(inString):
    # Initialize accumulator
    chksm = 0
    # For each character in the string
    #if len(inString)% 2 == 1:
        #inString = inString + ' '
        
    i = 0
    while i < len(inString) -1:
        bin1 = ascii_lookup(inString[i])
        bin2 = ascii_lookup(inString[i + 1])
        if bin1 == "" or bin2 == "":
            return -1
        bin3 = bin1 + bin2
        bin3 = rotateRight(bin3)
        dec = bin_to_decimal(bin3)
        chksm = chksm + dec
        i = i + 1

    # Make sure the checksum fits into 8 bits 
    chksm = chksm % 2**16
    #chksm = chksm % 65536

    
    
    return chksm

