# Blake McGahee
# Change Revision 1: Removed decoder function

# encoder function
def encoder(password):
    result = ''
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


# decoder function
def decoder(encoded_password):
    if len(encoded_password) != 8:
        return "Encoded password must be exactly 8 digits long."

    decoded_password = ""
    for digit in encoded_password:
        if digit.isdigit():
            shifted_digit = (int(digit) - 3) % 10
            decoded_password += str(shifted_digit)
        else:
            return "Encoded password should contain only integers."

    return decoded_password


# define main function
def main():
    # set variable to store input value
    global value
    # true loop for menu options
    while True:
        # print menu options
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print("The encoded password is " + encoder(value) + ", and the original password is " + decoder(value))
        elif choice == "3":
            break
        # error catching for invalid selection
        else:
            print("Invalid selection")
        print()


# name loop to call main function
if __name__ == '__main__':
    main()
