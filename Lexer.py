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
        # This could be a problem for accepting European formats later,
        # where commas are the decimal separator...
        lexeme += char

        #  Below are the significant characters for the lexer

        # this code evaluates whether we should end the current lexeme,
        # or keep going by wrapping to the next iteration of the for loop.
        if char in ["-"] and i == 0:  # , "+"
            tokens.append(Token(lexeme, 0, 1, TokenTypes.UNARY_SIGN))
            lexeme = ""
            continue

        if char.isdigit():
            if i + 1 < len(cleaned_input):
                # if we're at the end the current digit (sub)sequence
                if cleaned_input[i + 1] == ".":
                    tokens.append(
                        Token(lexeme, i - len(lexeme) + 1, i + 1,
                              TokenTypes.DIGITS))
                    lexeme = ""
            else:  # it's the end of the string!
                tokens.append(Token(lexeme, i - len(lexeme) + 1, i + 1,
                                    TokenTypes.DIGITS))
                lexeme = ""
        elif char == ".":
            tokens.append(Token(lexeme, i, i + 1, TokenTypes.SEPARATOR))
            lexeme = ""
        elif char in ",_":
            # if we didn't explicitly allow ",", then the else block below
            # would return an error state. The position count will be
            # one-off no matter what.
            lexeme = lexeme[:-1]  # remove the thousands separator
            continue
        else:
            return None  # invalid numerical string
            # TODO raise an exception instead?

    return tokens
