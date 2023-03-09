# Ismael Maura
# Aidan Wood

def encoder(password):
    """
    Encode an 8-digit password by shifting each digit up by 3 numbers.
    """
    encoded_password = ""
    for digit in password:
        # Shift each digit up by 3 numbers and add to the encoded password
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


def decoder(encoded_password):
    """
    Decode an encoded password by shifting each digit down by 3 numbers.
    """
    password = ""
    for digit in encoded_password:
        # Shift each digit down by 3 numbers and add to the original password
        original_digit = str((int(digit) - 3) % 10)
        password += original_digit
    return password


if __name__ == "__main__":

    password = '12345555'
    print(encoder(password))
    print(decoder(encoder(password)))

