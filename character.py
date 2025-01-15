# Function to count characters and print them
def count_characters_and_print(s):
    count = len(s)  # Counting the number of characters in the string
    print(f"Number of characters: {count}")
    
    # Printing each character
    print("Characters in the string:")
    for char in s:
        print(char)

# Example usage
string = "Hello"
count_characters_and_print(string)
