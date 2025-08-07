# """
# 20 Python String Manipulation Coding Questions
# 1Reverse a String
# Write a program that takes a string and prints it in reverse order.

# 2Count Vowels in a String
# Write code to count the number of vowels in a user-provided string.

# 3.Check for Palindrome
# Ask the user to input a word and check if it is a palindrome.

# 4.Remove All Whitespaces
# Take a string and remove all the whitespace characters using a string method.

# 5.Capitalize Each Word
# Given a sentence, convert the first letter of each word to uppercase using .title().

# Find and Replace
# Write code to replace all occurrences of the word "bad" with "good" in a sentence.

# 6.Character Frequency
# Take a string input and print how many times each character appears using .count().

# 7.Extract Domain from Email
# Given an email like user@example.com, extract and print just the domain part.

# 8.Check String Start and End
# Ask for a string and check if it starts with "Hello" and ends with "World".

# 9.Convert to Leetspeak
# Replace letters in a word with numbers (e.g., A=4, E=3, I=1, O=0, S=5, T=7).

# 10.Word Count
# Split a sentence into words and print the number of words.

# 11.Print Every Second Character
# Write a program that prints every second character from a string using slicing.

# 12.Remove Punctuation
# Remove all punctuation from a sentence using .replace() or string functions.

# 13.Get Initials from Full Name
# Given a full name, extract and print the initials (e.g., “John Doe” → “J.D.”).

# 14.Find Longest Word
# Take a sentence input and print the longest word.

# 15.Swap Case
# Use .swapcase() to convert uppercase to lowercase and vice versa in a string.

# 16.Check if All Characters are Digits
# Ask for input and check if the entire string contains only digits using .isdigit().

# 17.Print Unique Characters
# Print all characters that appear only once in a given string.

# 18.Center Align a String
# Ask the user for a word and print it center-aligned in a 30-character wide field using .center().

# 19.Custom String Formatter
# Create a string template and insert variables using f-strings (e.g., "Hello, {name}. You are {age} years old.").
# """

# # Tougher ones
# """
# 20 Obfuscated & Critical Thinking String Manipulation Challenges (Anti-AI-Paste Edition)
# Redesign a String Alteration Utility
# You're not allowed to use the built-in method for substring substitution. Develop an alternative strategy that will swap every occurrence of a given mini-pattern with a replacement one.

# Reorder Detection Mechanism
# Design a check system that confirms if two textual inputs can be transformed into each other by simple character shuffling.

# Simulate a Word Breaker
# Build a manual version of a space-based separator that doesn`t rely on the usual splitting shortcut functions.

# Construct a Word Frequency Analyzer
# Given a text blob, tally how often each unique word appears (ignoring letter case). No third-party tools.

# Digit-to-Pattern Translator
# Design a text formatter that rearranges any numeric string (11 digits) into a structured sequence with visual separators mimicking a phone format.

# Run-Length Simplifier
# Invent a system that compresses repeated characters in a sequence into a simplified coded form showing repetition counts.

# Filter Out the Noise
# You’re given a mixed-input string with letters and symbols. Write logic that extracts only the valid readable content, in order.

# Reveal Internal Symmetries
# Identify all inner fragments of a string (at least 2 characters long) that can be read the same forward and backward.

# Sensitive Data Masker
# Design an anonymizer that obscures all but the final segment of a numerical ID while maintaining readability.

# Naming Style Converter
# Translate any name convention from the format where every new word starts with a capital into one that uses underscores and lowercase throughout.

# Measure Lexical Units
# Build a program that breaks a sentence into components and records how long each component is, storing them in a key-value structure.

# Whitespace Trimming Simulator
# Without relying on trimming functions, remove unneeded characters from both ends of a user-submitted input.

# First-Time Letter Keeper
# Only keep the earliest instance of each letter that appears in a sequence. Remove all subsequent duplicates.

# Dominant Symbol Identifier
# From any block of text, determine which single character appears most frequently (ignoring character case).

# Language Re-Encoder
# Redefine a sentence by shifting the start of each word to the end and appending a common suffix.

# Credential Strength Auditor
# Formulate a validator that checks if a passphrase meets specific rules: length, symbol inclusion, capital presence, etc.

# Primitive Substring Examiner
# Craft a function that discovers if a certain character combination exists inside a larger string without using the obvious built-in lookup techniques.

# Multi-Spot Detector
# Given a string and a symbol, list every exact position that the symbol appears at. Use index logic only.

# Lexical Reorganizer by Length
# Reorder a group of words so that shorter ones appear first, preserving original order among equal lengths.

# Alphabet Completeness Inspector
# Write code that verifies if a passage includes every letter of the alphabet at least once. If not, list the missing ones.
# """



# #Answers

# print("1.Reverse a String")
# string = input("Enter a string: ")
# print(string[::-1])

# print("\n2.Count Vowels in a String")
# vowels = "aeiou"or"AEIOU"
# string = input("Enter a string: ")
# count = 0
# for vow in string:
#     if vow in vowels:
#         count += 1
# print(f"The number of vowels in the string is: {count}")

# print("\n3.Check for Palindrome")
# word = input("Enter a word: ")
# if word=="palindrome".capitalize():
#     print("The word is a palindrome")
# else:
#     print("The word is not a palindrome")

# print("\n4.Remove All Whitespaces")
# string = input("Enter a string: ")
# print(string.replace(" ", ""))

# print("\n5.Capitalize Each Word")
# sentence=input("enter a sentence: ")
# sentence=sentence.title()
# print(f"the new sentence is:{sentence}")

# print("\n6.find and replace")
# sentence=input("enter a sentence with bad in it:")
# sentence=sentence.replace("bad","good")
# print(f"the new sentence is:{sentence} ")




# print("\n7..Character Frequency")
# sentence=input("enter a sentence: ")
# sentence=sentence.count('',++1)
# print(f"the new sentence is:{sentence} ")

# print('\n8.email domain')
# # user@examole.com
# # user - alias or username
# # @example.com - domain
# email = input('Enter your email to extract the domain: ')
# for e in email:
#     if "@" in email:
#         print( email.split('@'))
#         break




import email


print("\n9.startswith and endswith")
sentence=input("Ente a sentence: ") 
sentence=sentence.startswith("Hello") and sentence.endswith("World")
print(sentence)

# print("\n10.Convert to Leetspeak")
# A=4, E=3, I=1, O=0, S=5, T=7



