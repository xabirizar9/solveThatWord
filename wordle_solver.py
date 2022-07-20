# Project for automatic wordle

from typing import final
import pandas as pd

def main():
    words = pd.read_csv("dictionary.csv", header=None)
    alphabet = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    mask = words[0].str.len() == 5
    filtered_words = words[0].loc[mask]
    five_letters = filtered_words.to_list()
    counter = 6
    most_likely_words = []
    final_word = "_ _ _ _ _".split(" ")
    while(counter > 0):
        print("Number of tries left: ", counter)
        guess = input("Enter your guess: ")
        print("Did you guess any letter correctly?")
        correct_letters = input("Correct letters: " )
        print("What about their position?")
        correct_letter_position = input("Correct position: ")
        
        guess_set = set(guess)
        correct_letters = set(correct_letters)
        wrong_letters = guess_set - correct_letters
        alphabet = set(alphabet)
        alphabet -= wrong_letters
        alphabet = list(alphabet)

        for word in five_letters:
            checker = 0
            for letter in word:
                if letter not in alphabet:
                    five_letters.remove(word)
                    checker = 1
                    break
            if checker:
                continue
            for correct, position in zip(correct_letters, correct_letter_position):
                if word[position] != correct:
                    five_letters.remove(word)
                    break
            most_likely_words.append(word)
        
        
        if correct_letter_position:
            correct_letter_position = correct_letter_position.split(" ")

            for letter, position in zip(correct_letters, correct_letter_position):
                final_word[int(position)] = letter

        print("Remaining letters: ")
        print(alphabet)
        print("Guess: ", final_word)

        counter -= 1

if __name__ == "__main__":
    main()
