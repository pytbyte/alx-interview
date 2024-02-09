#!/usr/bin/python3
'''Utf8 valodator.
'''
def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes of the data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    Notes:
        - A character in UTF-8 can be 1 to 4 bytes long.
        - The data set can contain multiple characters.
        - Each integer represents 1 byte of data; therefore, only the 8 least significant bits are considered.

    """
    # Variable to store the number of expected bytes for the current character
    expected_bytes = 0

    for byte in data:
        # Check if the current byte is the start of a new character
        if expected_bytes == 0:
            if byte >> 7 == 0b0:
                # Single-byte character
                expected_bytes = 0
            elif byte >> 5 == 0b110:
                # Two-byte character
                expected_bytes = 1
            elif byte >> 4 == 0b1110:
                # Three-byte character
                expected_bytes = 2
            elif byte >> 3 == 0b11110:
                # Four-byte character
                expected_bytes = 3
            else:
                # Invalid start of a character
                return False
        else:
            # Check if the current byte is a continuation byte
            if byte >> 6 == 0b10:
                expected_bytes -= 1
            else:
                # Invalid continuation byte
                return False

    # Check if there are any remaining expected bytes
    return expected_bytes == 0
