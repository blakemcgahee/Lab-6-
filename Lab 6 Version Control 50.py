# Blake McGahee

def encoder(password):
    result = ''
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


def decoder(password):
    result = ''

    for digit in password:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result


def main():
    global value
    while True:
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        if choice == "1":
            value = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif choice == "2":
            print("The encoded password is " + encoder(value) + ", and the original password is " + value)
        elif choice == "3":
            break
        else:
            print("Invalid selection")
        print()


if __name__ == '__main__':
    main()
