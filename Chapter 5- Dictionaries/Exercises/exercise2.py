#Exercise 2: Glossary
'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

#Creating a dictionary with 5 words 
glossary = {
    'Comment': 'It is identified with a hash symbol(#) that are ignored by the interpreter during the execution of the program.',
    'Concatenation': 'The process of joining two or more text strings into one string.',
    'Function': "A piece of prewritten code that performs an operation.",
    'Garbage Collection': 'The process of removing values that are no longer referenced by variables',
    'Variable': 'A reserved memory location to store values',
    }

#Displaying each word with its definition
word = 'Comment'
print("\n" + word.title() + ": " + glossary[word])

word = 'Concatenation'
print("\n" + word.title() + ": " + glossary[word])

word = 'Function'
print("\n" + word.title() + ": " + glossary[word])

word = 'Garbage Collection'
print("\n" + word.title() + ": " + glossary[word])

word = 'Variable'
print("\n" + word.title() + ": " + glossary[word])