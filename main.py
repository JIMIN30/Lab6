def print_menu():   # It prints menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

def encode(original_password):  # It encodes the input password
    encoded_password = ''
    for digit in original_password:
        encoded_password += str((int(digit) + 3) % 10)
    return encoded_password
    print("Your password has been encoded and stored!")
def decode(data): # Decodes the input password
    decode_data = ''
    for char in str(data):
        decode_data += str((int(char) - 3) % 10)
    return decode_data


print_menu()
user_selection = input("Please enter an option: ")

while user_selection != '3':

    if user_selection == '1':
        original_password = input("Please enter your password to encode: ")
        encoded_password = encode(original_password)
        print(encoded_password)

    #if user_selection == '2': decode

    #if user_selection == '3': Quit



