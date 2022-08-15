"""
Provide code to support token usage
"""
from dataclasses import dataclass
from enum import Enum
from typing import Union


class TokenTypes(Enum):
    """ type definitions for tokens """
    UNARY_SIGN_OP = 0
    INT_PART = 1
    SEPARATOR = 2
    FRAC_PART = 3


@dataclass
class Token:
    """
    Class to store tokenized strings from a lexer.
    """

    lexeme: str
    token_type: TokenTypes
    value: Union[float, None]

    def __repr__(self):
        return f"({self.token_type.name}: {self.lexeme})"