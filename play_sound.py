import pysine
import time


class PlaySound:
    """
    Class to play Morse code as sound.

    Attributes
    ----------
    morse_code : str
        A string of Morse code to be played as sound.
    dot_time_interval : float
        The time interval for a dot sound in seconds.
    dash_time_interval : float
        The time interval for a dash sound in seconds.
    gap_between_symbols_of_one_letter : float
        The time interval for a gap between symbols of one letter in seconds.
    gap_between_letters : float
        The time interval for a gap between letters in seconds.
    gap_between_words : float
        The time interval for a gap between words in seconds.
    frequency : int
        The frequency of the sound in Hz.

    Methods
    -------
    play() -> None:
        Play sound associated with every symbol from morse code.
    """
    def __init__(self, morse_code: str) -> None:
        self.morse_code = morse_code
        self.dot_time_interval = 0.1
        self.dash_time_interval = 3 * self.dot_time_interval
        self.gap_between_simbols_of_one_letter = self.dot_time_interval
        self.gap_between_letters = 3 * self.dot_time_interval
        self.gap_between_words = 7 * self.dot_time_interval
        self.frequency = 500

    def play(self):
        index = 0
        while index < len(self.morse_code):
            if self.morse_code[index] == ".":
                pysine.sine(frequency=self.frequency, duration=self.dot_time_interval)
                print(".", end="")
                time.sleep(self.gap_between_simbols_of_one_letter)
            elif self.morse_code[index] == " ":
                if index < len(self.morse_code) - 1 and self.morse_code[index + 1] == " ":
                    time.sleep(self.gap_between_words)
                else:
                    time.sleep(self.gap_between_simbols_of_one_letter)
                print(" ", end="")
            elif self.morse_code[index] == "-":
                pysine.sine(frequency=self.frequency, duration=self.dash_time_interval)
                print("-", end="")
                time.sleep(self.gap_between_simbols_of_one_letter)
            index += 1
        print('')
