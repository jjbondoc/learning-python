alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    encoded_text = ''
    for character in plain_text:
        if character in alphabet:
            shifted_index = alphabet.index(character) + shift_amount
            while shifted_index > 25: # * We want to account for shifting letters at the end back to the start (index out-of-range)
                shifted_index -= 26
            encoded_text += alphabet[shifted_index]
        else:
            encoded_text += character # * Characters outside the alphabet are left as-is
    print(f"Here's the encoded result: {encoded_text}")

def decrypt(encoded_text, shift_amount):
    decoded_text = ''
    for character in encoded_text:
        if character in alphabet:
            shifted_index = alphabet.index(character) - shift_amount
            while shifted_index < 0: # * We want to account for shifting letters at the start to the end
                shifted_index += 26
            decoded_text += alphabet[shifted_index]
        else:
            decoded_text += character # * Characters outside the alphabet are left as-is
    print(f"Here's the decoded result: {decoded_text}")

#* Combining the 
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for character in start_text:
        if character in alphabet:
            if cipher_direction == 'encode':
                shifted_index = alphabet.index(character) + shift_amount
                while shifted_index > 25:
                    shifted_index -= 26
            elif cipher_direction == 'decode':
                shifted_index = alphabet.index(character) - shift_amount
                while shifted_index < 0:
                    shifted_index += 26
            end_text += alphabet[shifted_index]
        else:
            end_text += character
    print(f"Here's the result of your {cipher_direction}d text: {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)