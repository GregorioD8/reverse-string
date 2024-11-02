def reverse_string(string):
    """
    Reverses the given string without using built in reverse methods

    Parameters: 
    string (str): The string to be reversed

    Returns:
    str: The reversed string.
    """

    # Initialize empty string to hold reversed characters
    reversed_string = ""
    # Iterate over the input string from the last character to the first
    for i in range(len(string) - 1, -1, -1):
        # Append each character from the end of the input string to the reversed string
        reversed_string += string[i]
    # Return the final reversed string
    return reversed_string

print("Expecting: 'ih'")
print(reverse_string("hi"))

print("")

print("Expecting: 'ybabtac'")
print(reverse_string("catbaby"))

print("")

print("Expecting: 'a'")
print(reverse_string("a"))

print("")

print("Expecting: '' (empty string)")
print(reverse_string(""))