import pandas as pd

# Load the NATO phonetic alphabet CSV
nato_phonetic_alphabet = pd.read_csv("./nato_phonetic_alphabet.csv")

# Example student dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Create a DataFrame from the student dictionary
student_data_frame = pd.DataFrame(student_dict)

# Create a dictionary for the NATO phonetic alphabet
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

# Get user input and process each word
input_word = input("Enter a word: ").upper()

nato_phonetic = [nato_phonetic_alphabet_dict[letter] for letter in input_word if letter.isalpha()]

print(nato_phonetic)
