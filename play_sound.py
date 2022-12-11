import pysine
import time


class PlaySound:
    def __init__(self, morse_code):
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
