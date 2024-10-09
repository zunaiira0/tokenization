
Instructions to run the file
1. Open 'tokens.py' in a Python compiler
2. Store 'sampleCode.txt' in the same folder in which 'tokens.py' is stored.
3. Run 'tokens.py' in compiler
4. The output will display tokens in their respective categories.

Final output should look like the following:

Example 1:
# Simple Python function
------------------------------------------------------------
Category (Tokens)    | Lexemes
------------------------------------------------------------
Keywords             | def, print
Identifiers          | greet, greet
Separators           | (, ), :, (, ), (, )
Literals             | "Hello, World!"
Comments             | # Simple Python function, #Greet user
------------------------------------------------------------
Total tokens: 12
************************************************************
Example 2:
"""
Python example with variables and a loop
"""
------------------------------------------------------------
Category (Tokens)    | Lexemes
------------------------------------------------------------
Keywords             | for, print
Identifiers          | count, 5, i, in, range, count, i
Operators            | =
Separators           | (, ), :, (, )
Comments             | """Python example with variables and a loop"""
------------------------------------------------------------
Total tokens: 15
