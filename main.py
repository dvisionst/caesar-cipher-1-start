alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(start_text,shift_amount,cipher_direction):
    encrypted_text = ''
    for char in start_text:
        letter_position = alphabet.index(char)
        if cipher_direction == "encode":
            if letter_position >= 25:
                adjusted_position = letter_position + shift -26
                encrypted_text +=alphabet[adjusted_position]
            elif letter_position < 25:
                letter_position +=shift
                encrypted_text += alphabet[letter_position]
        elif cipher_direction == "decode":
            if letter_position < 0:
                adjusted_position = letter_position -shift + 26 
                encrypted_text += alphabet[adjusted_position]
            elif letter_position >= 0:
                letter_position -= shift
                encrypted_text += alphabet[letter_position]           
    print(encrypted_text)
    
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)

