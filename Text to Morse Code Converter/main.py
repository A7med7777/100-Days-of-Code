import os
from pydub import AudioSegment
from logo import logo  # Ensure 'logo.py' exists with a variable 'logo'

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--', '-': '-....-', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

# Reverse dictionary for decoding Morse to text
ALPHABET_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def converter(to: str, text: str) -> str:
    """
    Converts text to Morse code or Morse code to text.

    :param to: "morse" for text-to-Morse conversion, "text" for Morse-to-text conversion
    :param text: The input text or Morse code
    :return: Converted Morse code or decoded text
    """
    res = ""

    try:
        if to == "morse":
            for char in text:
                res += f"{MORSE_CODE_DICT.get(char.upper(), '[?]')} "  # Handle unknown characters
        else:
            for code in text.split():
                if code in ALPHABET_DICT:
                    res += ALPHABET_DICT[code]
                else:
                    return f"Error: Unrecognized Morse code '{code}'"  # Handle invalid Morse input

        return res.strip()  # Remove trailing spaces
    except KeyError as ke:
        return f"Error in input. Cannot translate: {ke}"


def concatenate_audio(text: str) -> None:
    """
    Generates an audio file playing the Morse code sequence.

    :param text: Input text that has been converted to Morse code
    :return: None (Exports an audio file)
    """
    merged_audio = AudioSegment.silent(duration=0)  # Start with an empty audio segment

    for char in text:
        if char == " ":
            merged_audio += AudioSegment.silent(duration=500)  # Longer pause for space
            continue

        file_path = f"./morse_code/{char}_morse_code.ogg"

        if os.path.exists(file_path):  # Check if the audio file exists
            merged_audio += AudioSegment.from_file(file_path)
        else:
            print(f"Warning: No audio file found for '{char}'")

        merged_audio += AudioSegment.silent(duration=250)  # Short pause between characters

    # Export final merged audio
    merged_audio.export("merged_audio.wav", format="wav")
    print("Morse code audio saved as 'merged_audio.wav'")


def get_user_choice() -> bool:
    """
    Prompts the user to select conversion mode (Text to Morse or Morse to Text).

    :return: True for Text to Morse, False for Morse to Text
    """
    while True:
        try:
            choice = int(input("Select a number:\n0. Convert Morse to Text\n1. Convert Text to Morse\n"))
            if choice in (0, 1):
                return bool(choice)
            else:
                print("\nInvalid input. Please enter 0 or 1.")
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


def main():
    """
    Main function to run the Morse Code Converter.
    """
    print(logo)  # Display program logo

    # Get conversion mode from user
    convert_to_morse = get_user_choice()

    # Get user input text
    input_text = input("Type: ")

    # Convert and process accordingly
    converted_text = converter("morse" if convert_to_morse else "text", input_text)

    if "Error" in converted_text:
        print(converted_text)  # Print error message
    else:
        print(f"Converted Output:\n{converted_text}")

        if convert_to_morse:
            concatenate_audio(input_text.upper())  # Generate Morse audio


# Run the program
if __name__ == '__main__':
    main()
