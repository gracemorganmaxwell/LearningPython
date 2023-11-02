# a TV remote is composed of buttons, each one has a built-in function and purpose
# to mute the audio, to change channel, to increase or decrease sound.
# String methods, each one is built into Python and has a specific function or purpose.
# After a string variable is defined ( assigned a value) via dot notation
# you can use various built in methods, which allow you to perform operations
# on the string, i.e. converting to Uppercase

# Converting to Uppercase
# To convert a string to uppercase, you can use the .upper() method.
my_string = "hello"
uppercase_string = my_string.upper()
print(uppercase_string)  # Output: "HELLO"

# Finding a Substring
# The .find() method returns the index of the first occurrence of a substring.
# If the substring is not found, it returns -1.
my_string = "hello world"
index = my_string.find("world")
print(index)  # Output: 6

# Replacing a Substring
# The .replace() method replaces occurrences of a substring within the string.
my_string = "hello world"
new_string = my_string.replace("world", "everyone")
print(new_string)  # Output: "hello everyone"

# Checking if a String Starts with a Substring
# The .startswith() method returns a Boolean value
# indicating whether the string starts with a given substring.
my_string = "hello"
result = my_string.startswith("he")
print(result)  # Output: True


