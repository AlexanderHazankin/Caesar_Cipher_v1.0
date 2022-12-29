from replit import clear


def encode(text, shift, alphabet):
    """
    Encodes the given text using a Caesar cipher with the given shift.
    """
    encoded_text = ""
    for char in text:
        if char in alphabet:

            # Shift the index of the character
            index_shift = (alphabet.index(char) + shift) % len(alphabet)
            encoded_char = alphabet[index_shift]

            # Append the encoded character to the encoded_text string
            encoded_text += encoded_char
    return encoded_text


def decode(text, shift, alphabet):
    """
    Decodes the given text using a Caesar cipher with the given shift.
    """
    decoded_text = ""
    for char in text:
        if char in alphabet:

            # Shift the index of the character
            index_shift = (alphabet.index(char) - shift) % len(alphabet)
            decoded_char = alphabet[index_shift]

            # Append the decoded character to the decoded_text string
            decoded_text += decoded_char
    return decoded_text


def main():

    # Set the play again flag to True
    play_again = True
    while play_again:

        # Clear the console
        clear()

        # Define the alphabet
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$',
                    '%', '^', '&', '*', '(', ')', ' ']

        # Get the direction from the user
        direction = input("Type '\033[31;1mencode\033[31;0m' to encrypt, type '\033[31;1mdecode\033[31;0m' to decrypt:\n")
        while direction != 'encode' and direction != 'decode':
            direction = input("Invalid direction. Please type '\033[31;1mencode\033[31;0m' or '\033[31;1mdecode\033[31;0m':\n")

        # Get the text from the user
        text = input("Type your '\033[31;1mmessage\033[31;0m':\n").lower()

        # Get the shift from the user
        while True:
            try:
                shift = int(input("Type the shift '\033[31;1mnumber\033[31;0m':\n"))
                break
            except ValueError:
                print("Invalid direction. Must to be a '\033[31;1mdigit\033[31;0m':\n")

        # Call the appropriate function based on the direction
        if direction == "encode":
            result = encode(text, shift, alphabet)
            print(f"Here's the encoded result:\n\033[31;1m{result}\033[31;0m")
        elif direction == "decode":
            result = decode(text, shift, alphabet)
            print(f"Here's the decoded result:\n\033[31;1m{result}\033[31;0m")

        # Get input from user to determine if they want to run the program again
        play_again = input("Type '\033[31;1mYes\033[31;0m' if you want to go again. Otherwise type '\033[31;1mNo\033[31;0m':\n")

        # Validate the input, prompting for correct input if necessary
        while play_again != 'yes' and play_again != 'no':
            play_again = input("Invalid direction. Please type '\033[31;1mYes\033[31;0m' or '\033[31;1mNo\033[31;0m':\n")

        # If the user does not want to run the program again, set play_again to 'False' to exit the loop
        if play_again == "no":
            play_again = False


main()
