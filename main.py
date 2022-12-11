from art import logo
from morsecode import MorseCode
from play_sound import PlaySound

# print logo
print(logo)

code = MorseCode()

code_or_decode_again = True
while code_or_decode_again:
    welcome_message_check = False
    final_message_check = False
    while not welcome_message_check:
        welcome_message = input("Welcome to Morse Code! With this application you can code or decode with Morse code!\n"
                                "If you want to code type: code\n"
                                "If you want to decode type: decode\n"
                                "Type here: ")
        # Morse coding
        if welcome_message.lower() == 'code':
            code.enter_message_to_code()
            code.code_message()
            play_code_sound = PlaySound(code.return_coded_massage())
            play_code_sound.play()
            print("")
            code.reset()
            welcome_message_check = True

        # Morse decoding
        if welcome_message.lower() == 'decode':
            code.enter_message_to_decode()
            print(code.decode_message())
            code.reset()
            welcome_message_check = True
        # enter wrong option
        elif (welcome_message.lower() != "code") and (welcome_message.lower() != "decode"):
            print(f"You entered a wrong option! Please type again!")
    while not final_message_check:
        message_to_user = input("If you want to code or decode again please type Y!\n"
                                "If you want to finish type N!\n"
                                "Type here: ")
        if message_to_user.lower() == "y":
            final_message_check = True
        elif message_to_user.lower() == "n":
            code_or_decode_again = False
            final_message_check = True
        # enter wrong option
        else:
            print(f"You entered a wrong option! Please type again!")
