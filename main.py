# Ismael Maura
# Aidan Wood
# Lab6


def encoder(password):
    # Encode an 8-digit password by shifting each digit up by 3 numbers.
    encoded_password = ""
    for digit in password:
        # Shift each digit up by 3 numbers and add to the encoded password
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decoder(encoded_password):
    # decode an 8-digit password by shifting each digit down by 3 numbers
    decoded_password = ""
    for digit in encoded_password:  # subtracts 3 from each digit, makes it positive if
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password



def menu():
    # Display a menu and prompt the user for an option.
    print("\nMenu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")
    option = input("Please enter an option: ")
    return option


if __name__ == "__main__":
    encoded_password = None
    while True:
        option = menu()
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password is None:
                encoded_password = input("Please enter the encoded password: ")
                password = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            else:
                password = decoder(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {password}.")
                encoded_password = None
        elif option == "3":
            exit()
