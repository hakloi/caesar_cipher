import argparse

def cipher(s, shift):
    if not s:
        return ""
    
    new_s = ""
    for el in s:
        if el.isalpha():
            start = ord('A') if el.isupper() else ord('a')
            new_s += chr(start + (ord(el) - start + shift) % 26)
        else:
            new_s += el
        
            
    return new_s

def main():
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption")
    parser.add_argument('message', type=str, help="The message to encrypt")
    parser.add_argument('shift', type=int, help="The number of positions to shift in the cipher")
    
    args = parser.parse_args()

    encrypted_message = cipher(args.message, args.shift)
    print("Encrypted Message:", encrypted_message)

if __name__ == "__main__":
    main()