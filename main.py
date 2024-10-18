# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

decoding_status = True

def caesar(original_text, shift_amount, new_direction):
    output_text = ""
    if new_direction == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {new_direction}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

while decoding_status:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text,shift_amount=shift,new_direction=direction)
    status = input('Type "yes" if you want to go again. Otherwise type "no".\n').lower()
    if status == "no":
        decoding_status = False
        print("Have a good day!")