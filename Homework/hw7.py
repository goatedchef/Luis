def ord0(char):
    
    return ord(char) - 32

def chr0(num):
    
    return chr(num + 32)

def caesar95(text, shift):
    
    cipher_text = ''
    for char in text:
        
            cipher_text += char
    return cipher_text

def main():
        encypted = input("Enter a string to be encrypted (Done to finish): ")
        while encypted != "done":
            shift = int(input("Enter a shift value: "))
            cipher_text = caesar95(user_input, shift)
            print("Cipher text:", cipher_text)
    
