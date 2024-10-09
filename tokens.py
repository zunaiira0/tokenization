import re

def remove_block_comments(code):
    # Manual removal of block comments, & storing them to categorize later
    lines = code.splitlines()
    cleaned_lines = []
    comments = []
    comment_continuation = ""
    in_block_comment = False

    for line in lines:
        #detects block comment delimeter
        if line.strip().startswith('"""'):
            #beginning of comment
            if not in_block_comment:
                in_block_comment = True
                comment_continuation+=line
            #end of block comment
            else:
                in_block_comment = False
                comment_continuation +=line
                comments.append(comment_continuation)
            #comments.append(line)
        
        #continuation in block comment      
        elif in_block_comment:
            #comments.append(line)
            comment_continuation +=line

        #code without comments:
        else:
            cleaned_lines.append(line) 
    
    return "\n".join(cleaned_lines), comments

def remove_comments_and_excess_space(code):
    # Manual removal of in line comments (using #), & storing them to categorize later
    lines = code.splitlines()
    cleaned_lines = []
    comments = []

    for line in lines:
        line = line.strip()  # Remove extra whitespace
        if line.startswith("#"): #start of comment
            comments.append(line)
            continue  # Skip comments from code but store them
        # If there's an inline comment, split it
        if "#" in line:
            comment_split = line.split("#")
            comments.append(f"#{comment_split[1].strip()}")
            line = comment_split[0].strip()

        #code without comments:
        if line:
            cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines), comments


def tokenize_code(code):
    # Tokenize the code manually
    tokens = {
        'Keywords': [],
        'Identifiers': [],
        'Operators': [],
        'Separators': [],
        'Literals': [],
        'Comments': []
    }

    # Regular expression pattern to match string literals, keywords, identifiers, operators, and separators
    pattern = r'\"[^\"]*\"|\w+|[^\s\w]'

    # Split the code into lines
    lines = code.splitlines()
    
    for line in lines:
        # Use the regular expression to tokenize the line
        words = re.findall(pattern, line)
        for word in words:
            category = categorize_token(word)
            if category == 'Keywords':
                tokens['Keywords'].append(word)
            elif category == 'Operators':
                tokens['Operators'].append(word)
            elif category == 'Separators':
                tokens['Separators'].append(word) 
            elif category == 'Literals':
                tokens['Literals'].append(word)
            else:
                tokens['Identifiers'].append(word)

    return tokens

# Helper function to categorize tokens
def categorize_token(word):
    # Example set for sorting various tokens to resective categories
    keywords = ['print', 'def', 'for', 'if', 'else']
    operators = ['+', '-', '=', '==', '<', '>', '*', '/', '%']
    separators = ['(', ')', ',', ':']
    
    if word in keywords:
        return 'Keywords'
    elif word in operators:
        return 'Operators'
    elif word in separators:
        return 'Separators'
    elif word.startswith('"') and word.endswith('"'):
        return 'Literals'
    elif word.isidentifier():
        return 'Identifiers'

def print_tokens_with_counts(tokens, comments, example_number):
    # Printing tokens in each category and total token count
    
    print(f"Example {example_number}:")
    if example_number == 1:
        print("# Simple Python function")
    elif example_number == 2:
        print('"""\nPython example with variables and a loop\n"""')
    
    #displaying lexemes and tokens as a table
    print("-" * 60)
    print(f"{'Category (Lexemes)':<20} | Tokens")
    print("-" * 60)

    #display the tokens in each category
    for category, token_list in tokens.items():
        
        if token_list:
            print(f"{category:<20} | {', '.join(token_list)}")
    if comments:
        print(f"{'Comments':<20} | {', '.join(comments)}")
    
    print("-" * 60)

    # Calculate the total number of tokens
    total_tokens = sum(len(t) for t in tokens.values()) 
    print(f"Total tokens: {total_tokens}")

def main():
    with open('sampleCode.txt','r') as file: #file is opened to read code
        input_code=file.read()
    
    #splitting the file as example 1 and example 2
    # Example 1: Before the first occurrence of """
    example_1 = input_code.split('"""')[0].strip()

    # Example 2: Everything from the first """ to the end (the comment and the code after it)
    example_2 = '"""\n' + input_code.split('"""', 1)[1].strip()

    #Tokenizing Example 1:

    #Step 1 & 2: Remove comments and extra space from example 1
    cleaned_code_1, comments_1=remove_comments_and_excess_space(example_1)

    # Step 3: Tokenize the cleaned code manually for example 1
    tokens_1 = tokenize_code(cleaned_code_1)
    
    # # Step 4: Print the tokens for example 1
    print_tokens_with_counts(tokens_1, comments_1, 1)

    print(f'*'*60)

    #Tokenizing Example 2
    # Step 1 & 2: Remove comments and excess space for example 2
    cleaned_code_2, comments_2 = remove_block_comments(example_2)

    # Step 3: Tokenize the cleaned code manually for example 2
    tokens_2 = tokenize_code(cleaned_code_2)

    # Step 4: Print the tokens for example 2
    print_tokens_with_counts(tokens_2, comments_2, 2)

if __name__ == "__main__":
    main()
