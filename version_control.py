# Andrei Rauta

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


def encoder(password):
    encoded_pass = ""

    for char in password:
        encoded_char = int(char) + 3
        if encoded_char > 9:
            encoded_char -= 10
        encoded_pass += str(encoded_char)

    return encoded_pass


def decoder(password):
    decoded_num = ''
    for i in str(password):
        decoded_i = str((int(i) - 3) % 10)
        decoded_num += decoded_i
    return decoded_num


def main():
    encoded_pass = ""

    while True:
        menu()

        user_opt = int(input("Please enter an option: "))

        if user_opt == 3:
            break
        elif user_opt == 1:
            pass_encode = input("Please enter your password to encode: ")
            encoded_pass = encoder(pass_encode)
            print("Your password has been encoded and stored!\n")

        else:
            print(f"The encoded password is {encoded_pass}, and the original password is {decoder(encoded_pass)}.\n")


if __name__ == "__main__":
    main()
