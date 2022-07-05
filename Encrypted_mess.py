
from turtle import position


#logo import from another .py file
import art
print(art.logo)


#Alphabets joki kaam krte hn
alphabet = []
for i in range (97,123):
    alphabet.append(chr(i))
alphabet.append(" ")
for i in range (97,123):
    alphabet.append(chr(i))
alphabet.append(" ")
# print(alphabet)


#Function Jo Decode aur Encode krta hai
def ceaser(start_text, shift_amount,cipher_direction):
    end_text=""
    if cipher_direction == 'decode':
        shift_amount = shift_amount*(-1)
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter

    print(f'The {cipher_direction} text is {end_text}')


#code main, input values 
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 27
    ceaser(text,shift,direction)

#re-run the code
    result = input('You want to run the code again type "yes" or "no" ')
    if result == "no":
     should_continue = False
     print('Goodbye Good boy')
    elif result == "yes":
     should_continue = True

