from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    string = ""
    if (direction == "decode"):
        shift = shift * -1

    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_letter = alphabet[position + shift]
            string += new_letter
        else:
            string += i

    print(f"The {direction}d code is: {string}")


while (True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(text, shift, direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if (choice == "yes"):
        continue
    else:
        print("Ended")
        break

# Shivani Verma