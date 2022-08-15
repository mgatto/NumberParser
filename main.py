from Lexer import lex

if __name__ == '__main__':
    number_tokens = lex("-123.0")
    print(number_tokens)

# What kinds of transforms can I do with it?
# - reverse the number parts
# - print it as a fraction of some kind?
# - translate to a different locale !
