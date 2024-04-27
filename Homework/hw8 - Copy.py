def adler32var(input_string):
    MOD_ADLER = 65521
    a = 1
    b = 0

    for char in input_string:
        a = (a + ord(char)) % MOD_ADLER
        b = (b + a) % MOD_ADLER

    adler32_checksum = (b << 16) | a
    return adler32_checksum

def main():
    input_string = input("Enter a string: ")
    checksum = adler32var(input_string)
    print(checksum)
    
main()
    