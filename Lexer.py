from typing import List, Union

from Token import Token, TokenTypes


def lex(num_str: str) -> Union[List[Token], None]:
    """ Convert a numerical decimal string into a number

    :param num_str: A numerical string, either in Base 10 format
    :return: List of Tokens if string is valid, otherwise None
    """

    cleaned_input = num_str.strip()
    tokens: List[Token] = []
    lexeme = ""

    # this is a plain left-to-right, very deterministic lexer
    for i, char in enumerate(cleaned_input):
        lexeme += char

        # this code evaluates whether we should end the current lexeme,
        # or keep going by wrapping to the next iteration of the for loop.
        if char == "-" and i == 0:
            tokens.append(Token(lexeme, TokenTypes.UNARY_SIGN_OP, None))
            lexeme = ""
            continue

        if char.isdigit():
            if i + 1 < len(cleaned_input):
                # if we're at the end the current digit (sub)sequence
                if cleaned_input[i + 1] == ".":
                    tokens.append(
                        Token(lexeme, TokenTypes.INT_PART, int(lexeme)))
                    lexeme = ""
            else:  # it's the end of the string!
                tokens.append(Token(lexeme, TokenTypes.FRAC_PART, int(lexeme)))
                lexeme = ""
        elif char == ".":
            tokens.append(Token(lexeme, TokenTypes.SEPARATOR, None))
            lexeme = ""
        else:
            return None  # invalid numerical string

    return tokens
