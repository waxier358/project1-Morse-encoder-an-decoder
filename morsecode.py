class MorseCode:
    def __init__(self):
        self.message_to_code = ""
        self.message_to_decode = ""

        self.coded_message = ""
        self.decoded_message = ""

    with open("characters.txt") as char_file:
        list_file = char_file.readlines()
    characters_list = []
    for character in list_file:
        characters_list.append(character.replace("\n", ""))

    with open("morse_characters.txt") as morse_file:
        morse_list_file = morse_file.readlines()
    morse_list = []
    for character in morse_list_file:
        morse_list.append(character.replace("\n", ""))

    def enter_message_to_code(self):
        self.message_to_code = input("Enter your message here! You can use letters a-z, A-Z, numbers 0-9, . , ? and ! ")

    def enter_message_to_decode(self):
        self.message_to_decode = input("Attention! You can decode text coded only with this application!\n Enter your "
                                       "Morse ceded text here: ")

    def code_message(self):
        for letter in self.message_to_code:
            if letter == " ":
                self.coded_message += " "
            else:
                try:
                    index = self.characters_list.index(letter.upper())
                except ValueError:
                    return f"ValueError character {letter} isn't in alfabet!"
                self.coded_message += self.morse_list[index] + " "
        # remove last " " and print coded message
        return f"Message {self.message_to_code.upper()} is coded: {self.coded_message[:-1]}"

    def return_coded_massage(self):
        return self.coded_message

    def decode_message(self):
        coded_words = self.message_to_decode.split("  ")
        for coded_word in coded_words:
            coded_chars = coded_word.split(" ")
            for coded_char in coded_chars:
                try:
                    index = self.morse_list.index(coded_char)
                except ValueError:
                    return f"ValueError character {coded_char} isn't in alfabet!"
                self.decoded_message += self.characters_list[index]
            self.decoded_message += " "
        return f"Message {self.message_to_decode.upper()} is decoded: {self.decoded_message[:-1]}"

    def print_message_to_code(self):
        print(self.message_to_code)

    def reset(self):
        self.message_to_code = ""
        self.message_to_decode = ""

        self.coded_message = ""
        self.decoded_message = ""

