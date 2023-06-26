from art import logo
from morsecode import MorseCode
from play_sound import PlaySound


def morse_code_and_decoder():
    """
        morse_code_and_decoder function run the Morse code application.

        This function initializes the MorseCode class, then enters a loop where the user can choose to code or decode a
        message. After coding or decoding, the user can choose to continue or exit the program.
    """

    # print logo
    print(logo)

    try:
        code = MorseCode()
    except FileNotFoundError as e:
        print(f"An error occurred: {str(e)}")
        return

    code_or_decode_again = True
    while code_or_decode_again:
        welcome_message_check = False
        final_message_check = False
        while not welcome_message_check:
            welcome_message = input("Welcome to Morse Code! With this application you can code or decode with Morse "
                                    "code!\n"
                                    "If you want to code type: code\n"
                                    "If you want to decode type: decode\n"
                                    "Type here: ").lower()
            # Morse coding
            if welcome_message == 'code':
                code_user_input = input("Enter your message here! You can use letters a-z, A-Z, numbers 0-9, . , ? "
                                        "and ! ")
                code.set_message_to_code(code_user_input)
                try:
                    print(code.code_message())
                    play_code_sound = PlaySound(code.return_coded_message())
                    play_code_sound.play()
                except ValueError as e:
                    print(f"An error occurred: {str(e)}")
                code.reset()
                welcome_message_check = True

            # Morse decoding
            if welcome_message == 'decode':
                decode_user_input = input("Attention! You can decode text coded only with this application!\n"
                                          "Enter your Morse ceded text here: ")
                code.set_message_to_decode(decode_user_input)
                try:
                    print(code.decode_message())
                except ValueError as e:
                    print(f"An error occurred: {str(e)}")
                code.reset()
                welcome_message_check = True
            # enter wrong option
            elif (welcome_message != "code") and (welcome_message != "decode"):
                print(f"You entered a wrong option! Please type again!")
        while not final_message_check:
            message_to_user = input("If you want to code or decode again please type Y!\n"
                                    "If you want to finish type N!\n"
                                    "Type here: ").lower()
            if message_to_user == "y":
                final_message_check = True
            elif message_to_user == "n":
                code_or_decode_again = False
                final_message_check = True
            # enter wrong option
            else:
                print(f"You entered a wrong option! Please type again!")


if __name__ == "__main__":
    morse_code_and_decoder()
