

# defining the encoder
def encoder(password):
    encoded_pass = ''
    for digit in password:
        if digit.isdigit():
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_pass += encoded_digit
        else:
            encoded_pass += digit
        return encoded_pass
# defining decoder
def decoder(password):
    decoded_pass = ''
    for i in password:
        i = int(i) - 3
        decoded_pass += str(i)
    return decoded_pass

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


if __name__ == '__main__':
    option = 0
    run = True
    while True:
        menu()
        print()
        option = input('Please enter an option: ')
        if option == '1':
            password = input('Please enter your password to encode: ')
            encoded_pass = encoder(password)
            print('Your password has been encoded and stored!')
            print()
        elif option == '2':
            password = input('Please enter your password to decode: ')
            decoded_pass = decoder(password)
            print('Your decoded password', print(decoded_pass))
            print('')


        elif option == '3':
            run = False
            break
        else:
            print("Invalid choice. Please select a valid option.")

