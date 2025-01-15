# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)  # int() converts a binary string to a decimal number

# Example usage
binary_str = "1010"
decimal_num = binary_to_decimal(binary_str)
print(f"Binary: {binary_str} => Decimal: {decimal_num}")
