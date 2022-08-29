from Lexer import lex
from Parser import Parser

if __name__ == '__main__':
    tokens_0 = lex("-123")
    tokens_1 = lex("123")
    tokens_2 = lex("-123.0")
    tokens_3 = lex("-1,123.0")
    tokens_4 = lex("100_123")

    parser = Parser(tokens_0)
    ast = parser.parse()
    print(ast)

# What kinds of transforms can I do with it?
# - reverse the number parts
# - print it as a fraction of some kind?
# - translate to a different locale !
# - internally transform to IEEE 475 floating point
