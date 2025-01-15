import string

def remove_punctuation(input_string):
    # Create a translation table that maps punctuation to None
    translator = str.maketrans('', '', string.punctuation)
    # Use the translate() method to remove punctuation
    return input_string.translate(translator)

# Example usage
input_text = "Hello, world! This is a test... How are you?"
output_text = remove_punctuation(input_text)
print("Original:", input_text)
print("Without Punctuation:", output_text)
