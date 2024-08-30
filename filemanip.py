import re
from spellchecker import SpellChecker

# Lab 1.2

def file_reading_and_writing():
    try:
        # Read the contents of the file
        with open('example.txt', 'r') as file:
            content = file.read()
        print("Original Content:")
        print(content)

        # Append text to the file
        with open('example.txt', 'a') as file:
            append_text = input("Enter the text to append: ")
            file.write(append_text + '\n')

        # Read the updated content
        with open('example.txt', 'r') as file:
            updated_content = file.read()
        print("\nUpdated Content:")
        print(updated_content)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read or write to file.")

def text_manipulation():
    try:
        # Read the content
        with open('example.txt', 'r') as file:
            content = file.read()

        print("\nSelect a text manipulation option:")
        print("1. Word Count")
        print("2. Character Frequency")
        print("3. Text Replacement")
        print("4. Line Modification")
        print("5. Spell Check")
        option = input("Enter your choice: ")

        if option == '1':
            # Word Count
            words = content.split()
            word_count = len(words)
            print(f'\nThe file contains {word_count} words.')
        elif option == '2':
            # Character Frequency
            print("\nSelect a character frequency option:")
            print("1. Display all character frequencies")
            print("2. Search for a specific character frequency")
            char_freq_option = input("Enter your choice: ")

            if char_freq_option == '1':
                content = content.lower()
                char_freq = {}
                for char in content:
                    if char in char_freq:
                        char_freq[char] += 1
                    else:
                        char_freq[char] = 1
                print("\nCharacter Frequencies:")
                for char, freq in char_freq.items():
                    print(f"{char}: {freq}")
            elif char_freq_option == '2':
                char_to_display = input('\nEnter the character to display its frequency: ')
                content = content.lower()
                char_freq = {}
                for char in content:
                    if char in char_freq:
                        char_freq[char] += 1
                    else:
                        char_freq[char] = 1
                if char_to_display in char_freq:
                    print(f'\nThe frequency of "{char_to_display}" is {char_freq[char_to_display]}.')
                else:
                    print(f'\nThe character "{char_to_display}" is not found in the content.')
            else:
                print("Invalid option. Please try again.")
        elif option == '3':
            # Text Replacement
            print("\nSelect a text replacement option:")
            print("1. Replace a specific text")
            print("2. Replace all occurrences of a text")
            replace_option = input("Enter your choice: ")

            if replace_option == '1':
                search_text = input('\nEnter the text to search for: ')
                replace_text = input('Enter the text to replace it with: ')
                updated_content = content.replace(search_text, replace_text, 1)
                print('\nUpdated Content after Replacement:')
                print(updated_content)
            elif replace_option == '2':
                search_text = input('\nEnter the text to search for: ')
                replace_text = input('Enter the text to replace it with: ')
                updated_content = content.replace(search_text, replace_text)
                print('\nUpdated Content after Replacement:')
                print(updated_content)
            else:
                print("Invalid option. Please try again.")
        elif option == '4':
            # Line Modification
            lines = content.splitlines()
            print("\nSelect a line modification option:")
            print("1. Insert a new line")
            print("2. Delete a line")
            print("3. Replace a line")
            line_mod_option = input("Enter your choice: ")

            if line_mod_option == '1':
                line_num = int(input('\nEnter the line number: '))
                new_line = input('Enter the new line: ')
                lines.insert(line_num - 1, new_line)
                updated_content = '\n'.join(lines)
                print('\nUpdated Content after Line Modification:')
                print(updated_content)
            elif line_mod_option == '2':
                line_num = int(input('\nEnter the line number: '))
                del lines[line_num - 1]
                updated_content = '\n'.join(lines)
                print('\nUpdated Content after Line Modification:')
                print(updated_content)
            elif line_mod_option == '3':
                line_num = int(input('\nEnter the line number: '))
                new_line = input('Enter the new line: ')
                lines[line_num - 1] = new_line
                updated_content = '\n'.join(lines)
                print('\nUpdated Content after Line Modification:')
                print(updated_content)
            else:
                print("Invalid option. Please try again.")
        elif option == '5':
            # Spell Check
            spell = SpellChecker()
            words = re.sub(r'[^\w\s]', '', content).split()
            misspelled = spell.unknown(words)
            for word in misspelled:
                print(f"Misspelled word: {word}")
                print(f"Possible corrections: {spell.candidates(word)}")
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid line number.")
    except IndexError:
        print("Error: Line number out of range.")

def regular_expression_tasks():
    try:
        # Read the content
        with open('example.txt', 'r') as file:
            content = file.read()

        print("\nSelect a regular expression task:")
        print("1. Pattern Matching")
        print("2. Text Extraction")
        option = input("Enter your choice: ")

        if option == '1':
            # Pattern Matching
            print("\nSelect a pattern matching option:")
            print("1. Search for a specific pattern")
            print("2. Search for all occurrences of a pattern")
            pattern_match_option = input("Enter your choice: ")

            if pattern_match_option == '1':
                pattern = input('\nEnter the pattern to search for: ')
                matches = re.findall(pattern, content)
                print(f'\nFound {len(matches)} matches for the pattern "{pattern}"')
                print(matches)
            elif pattern_match_option == '2':
                pattern = input('\nEnter the pattern to search for: ')
                matches = re.findall(pattern, content)
                print(f'\nFound {len(matches)} matches for the pattern "{pattern}"')
                print(matches)
            else:
                print("Invalid option. Please try again.")
        elif option == '2':
            # Text Extraction
            print("\nSelect a text extraction option:")
            print("1. Extract dates in the format DD MMM YYYY")
            print("2. Extract custom text")
            text_extract_option = input("Enter your choice: ")

            if text_extract_option == '1':
                dates = re.findall(r'\d{1,2} [A-Za-z]+ \d{4}', content)
                print(f'\nFound {len(dates)} dates in the content:')
                print(dates)
            elif text_extract_option == '2':
                pattern = input('\nEnter the pattern to extract: ')
                matches = re.findall(pattern, content)
                print(f'\nFound {len(matches)} matches for the pattern "{pattern}"')
                print(matches)
            else:
                print("Invalid option. Please try again.")
        else:
            print("Invalid option. Please try again.")
    except re.error:
        print("Error: Invalid regular expression pattern.")

def main():
    while True:
        print("\nSelect an option:")
        print("1. File Reading and Writing")
        print("2. Text Manipulation")
        print("3. Regular Expression Tasks")
        print("4. Quit")
        option = input("Enter your choice: ")

        if option == '1':
            file_reading_and_writing()
        elif option == '2':
            text_manipulation()
        elif option == '3':
            regular_expression_tasks()
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
