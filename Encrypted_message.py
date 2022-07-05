from base64 import decode
from itertools import count
from turtle import position


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','0','1', '2', '3', '4', '5','6','7','8','9']

alphabet = []
for i in range (97,123):
  alphabet+= chr(i)
alpha = [' ', '0', '1', '2', '3', '4', '5','6','7','8','9']
alphabet += alpha

alphabets = ['த', 'ࢯ', '6', 'आ', 'এ', 'য', 'ף', '0', '1', 'ꝺ', '北', 'r', 'k', '方', 'q', '見', 'u', 'e', 'l', 'る', 'ᵹ', 'ব', 'ख', 'ਖ', 'ব', 'ழ','^',',','.','"','!','@','$',')','*','%','&']

from art import logo
print(logo)


def code(direction,message):
  end_txt =""
  if direction == "encode":
    for letter in message:
      if letter in alphabet:
       position = alphabet.index(letter)
       letter_ = alphabets[position] 
       end_txt += letter_
      else:
        end_txt+=letter
  else:
    for letter in message:
      if letter in alphabets:
       position = alphabets.index(letter)
       letter_ = alphabet[position] 
       end_txt += letter_
      else:
        end_txt+=letter
  print(end_txt)


should_continue = True
while should_continue:
  position = input('Type "encode" for encryption and "decode" for decryption:\n')
  message = input('Enter your message here:\n').lower()
  code(position,message)

  result = input('You want to run the code again type "yes" or "no" ').lower()
  if result == "no":
    should_continue = False
    print('Goodbye Good boy')
  elif result == "yes":
    should_continue = True


