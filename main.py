from Lexer import lex

if __name__ == '__main__':
    tokens_1 = lex("123")  # ouch! [(FRAC_PART: "123"; @0-3)]
    tokens_2 = lex("-123.0")
    tokens_3 = lex("-1,123.0")
    tokens_4 = lex("100_123")
    print(tokens_1, tokens_2, tokens_3, tokens_4, sep="\n")

# What kinds of transforms can I do with it?
# - reverse the number parts
# - print it as a fraction of some kind?
# - translate to a different locale !
# - internally transform to IEEE 475 floating point
