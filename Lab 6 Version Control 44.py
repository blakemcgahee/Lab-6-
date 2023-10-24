# Blake McGahee
# Change Revision 1 - Removed dropped line on line 14.


# Encoder function
def encoder(password):
    result = ''
    # 
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result

# Decoder function

# Main function
def main():
    # Global variable to store value entered
    global value
    # While loop for menu options
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        # Menu options 1 - 3
        if choice == "1":
            value = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print("The encoded password is " + encoder(value) + ", and the original password is " + value)
        elif choice == "3":
            break
            # Error catching for invalid input
        else:
            print("Invalid input, please select 1 - 3")
        print()

# Name function to call main function 
if __name__ == '__main__':
    main()
