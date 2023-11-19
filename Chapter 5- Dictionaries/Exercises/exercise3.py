#Exercise 3: Glossary 2
#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

#Glossary with 5 terms  
glossary = {
    'Comment': 'It is identified with a hash symbol(#) that are ignored by the interpreter during the execution of the program.',
    'Concatenation': 'The process of joining two or more text strings into one string.',
    'Function': "A piece of prewritten code that performs an operation.",
    'Garbage Collection': 'The process of removing values that are no longer referenced by variables.',
    'Variable': 'A reserved memory location to store values.',

#Adding 5 more terminologies
    'String': 'These are text values composed of a sequence of characters.',
    'Debugging': 'The process of detecting and removing of existing and potential errors in a software code.',
    'List Slicing': 'To extract some elements from a list using some preferred indexes.',
    'Integer': 'It is a number without a fractional component and do not support decimal points.',
    'Float': 'A numeric data type that has a decimal place.',
    }

#Displaying each word with its definition
for word, definition in glossary.items():
    print("\n" + word + ": " + definition)