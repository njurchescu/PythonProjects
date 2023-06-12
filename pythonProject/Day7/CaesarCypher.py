from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#
# def encrypt (plain_text, shift_amount):
#     encrypted_text = ''
#     encrypted_text_list = []
#     for letter in plain_text:
#       position = alphabet.index(letter)
#       new_index = position + shift_amount
#       if new_index > 25:
#           left_in_alphabet = 25 - position
#           new_index = shift_amount - left_in_alphabet
#           encrypted_text += alphabet[new_index - 1]
#       # encrypted_text_list.append(alphabet[position+shift_amount])
#       else:
#          encrypted_text += alphabet[new_index]
#     # encrypted_text = ''.join(encrypted_text_list)
#     print(f"The encoded text is {encrypted_text}")
# ----------------------------------------------------------------------------------------------------------
# def decrypt (cypher_text, shift_amount):
#     decrypted_text = ''
#     for letter in cypher_text:
#        position = alphabet.index(letter)
#        new_index = position - shift_amount
#        if new_index < 0:
#            new_index = 25 + new_index
#            # new_index = shift_amount + left_in_alphabet
#            decrypted_text += alphabet[new_index+1]
#        else:
#            decrypted_text += alphabet[new_index]
#
#     print(f"The decoded text is {decrypted_text}")

def caesar(text, shift, direction):
    if direction != "decode" and direction  != "encode":
        print("You have entered invalid direction. Try again.")
    end_text = ''
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position < 0:
                new_position = 25 + new_position
                end_text += alphabet[new_position + 1]
            elif new_position > 25:
                left_in_alphabet = 25 - position
                new_position = shift - left_in_alphabet
                end_text += alphabet[new_position - 1]
            else:
                end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {direction} text is {end_text}.")


run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > len(alphabet):
        shift = shift % len(alphabet)
    caesar(text,shift,direction)
    ask_user = input("Would you like to go again? 'Yes' 'No' \n").lower()
    if ask_user == "yes":
        run_again = True
    elif ask_user == "no":
        print(f" Thank you for {direction} !\n")
        run_again = False
    else:
        print(f" Thank you for {direction} !")
        run_again = False

