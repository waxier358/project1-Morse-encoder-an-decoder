class MorseCode:
    """
        A class to encode and decode Morse code.

        Attributes
        ----------
        message_to_code : str
            A message to be converted to Morse code.
        message_to_decode : str
            A Morse code message to be converted to English.
        coded_message : str
            The message after being encoded to Morse code.
        decoded_message : str
            The Morse code message after being decoded to English.
        characters_list : list
            A list of valid characters for Morse code.
        morse_list : list
            A list of Morse code equivalents for the characters.

        Methods
        -------
        create_list_from_file(file_name: str) -> list:
            Read a file and return a list of its lines after removing trailing new lines.

        set_message_to_code(code_user_input: str) -> None:
            Set a message to be encoded to Morse code.

        set_message_to_decode(decode_user_input: str) -> None:
            Set a Morse code message to be decoded.

        code_message() -> str:
            Encode the input message to Morse code and return the coded message.

        return_coded_message() -> str:
            Return the coded message.

        decode_message() -> str:
            Decode the input Morse code message and return the decoded message.

        reset_messages() -> None
            Reset all the messages and codes to an empty string.

        reset() -> None:
            Call method reset_message().
        """

    def __init__(self):
        self.message_to_code = str()
        self.message_to_decode = str()
        self.coded_message = str()
        self.decoded_message = str()
        self.characters_list = self.create_list_from_file('characters.txt')
        self.morse_list = self.create_list_from_file('morse_characters.txt')

    @staticmethod
    def create_list_from_file(file_name: str) -> list:
        try:
            with open(file_name) as char_file:
                return [character.replace("\n", "") for character in char_file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError(f'The file {file_name} was not found.')

    def set_message_to_code(self, code_user_input: str) -> None:
        self.message_to_code = code_user_input

    def set_message_to_decode(self, decode_user_input: str) -> None:
        self.message_to_decode = decode_user_input

    def code_message(self) -> str:
        # eliminate leading and trailing ' '
        self.message_to_code = self.message_to_code.strip(' ')
        # check if string is empty
        if self.message_to_code == '':
            raise ValueError(f'You enter an empty string or a string only with " ".')
        self.coded_message = ""
        for letter in self.message_to_code:
            if letter == " ":
                self.coded_message += " "
            else:
                try:
                    index = self.characters_list.index(letter.upper())
                except ValueError:
                    raise ValueError(f"ValueError character {letter} isn't in the alfabet!")
                self.coded_message += self.morse_list[index] + " "
        # remove last " " and print coded message
        return f"Message {self.message_to_code} is coded: {self.coded_message[:-1]}"

    def return_coded_message(self) -> str:
        return self.coded_message

    def decode_message(self) -> str:
        # eliminate leading and trailing ' '
        self.message_to_decode = self.message_to_decode.strip(' ')
        # check if string is empty
        if self.message_to_decode == '':
            raise ValueError(f'You enter an empty string or a string only with " ".')
        self.decoded_message = ""
        coded_words = self.message_to_decode.split("  ")
        for coded_word in coded_words:
            coded_chars = coded_word.split(" ")
            for coded_char in coded_chars:
                try:
                    index = self.morse_list.index(coded_char)
                except ValueError:
                    raise ValueError(f"ValueError character {coded_char} isn't in Morse Code!")
                self.decoded_message += self.characters_list[index]
            self.decoded_message += " "
        return f"Message {self.message_to_decode.upper()} is decoded: {self.decoded_message[:-1]}"

    def reset_messages(self):
        self.message_to_code = ""
        self.message_to_decode = ""
        self.coded_message = ""
        self.decoded_message = ""

    def reset(self) -> None:
        self.reset_messages()
