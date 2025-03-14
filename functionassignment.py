def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_vowel_consonant(letter):
    vowels = "aeiouAEIOU"
    if letter.isalpha():
        return "Vowel" if letter in vowels else "Consonant"
    else:
        return "Invalid input"

def check_special_character(char):
    if char.isalnum():
        return "Not a special character"
    else:
        return "Special character"

def combined_function():
    value = input("Enter a value (number, letter, or character): ")
    if value.isdigit():
        print(f"Number {value} is {check_odd_even(int(value))}.")
    elif len(value) == 1 and value.isalpha():
        print(f"Letter {value} is a {check_vowel_consonant(value)}.")
    elif len(value) == 1:
        print(f"Character {value} is a {check_special_character(value)}.")
    else:
        print("Invalid input.")

def main():
    while True:
        print("\nMENU:")
        print("1. Check if it is an Odd or Even Number")
        print("2. Check if its a Vowel or Consonant")
        print("3. Check if it ia a Special Character or not")
        print("4. Combined Function")
        print("Type 'STOP' to exit.")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num = int(input("Enter a number: "))
            print(f"The number {num} is {check_odd_even(num)}.")
        elif choice == "2":
            letter = input("Enter a letter: ")
            print(f"The letter {letter} is a {check_vowel_consonant(letter)}.")
        elif choice == "3":
            char = input("Enter a character: ")
            print(f"The character {char} is {check_special_character(char)}.")
        elif choice == "4":
            combined_function()
        elif choice.lower() == "stop":
            print("Program stopped.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
