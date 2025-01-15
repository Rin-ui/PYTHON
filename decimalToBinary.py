# Function to convert decimal to binary
def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]  # bin() returns a string starting with '0b', so we slice it to remove '0b'

# Example usage
decimal_num = 10
binary_num = decimal_to_binary(decimal_num)
print(f"Decimal: {decimal_num} => Binary: {binary_num}")
