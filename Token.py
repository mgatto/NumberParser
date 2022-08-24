"""
Provide code to support token usage
"""
from dataclasses import dataclass
from enum import Enum
from typing import Union


class TokenTypes(Enum):
    """ type definitions for tokens """
    UNARY_SIGN = 0
    DIGITS = 1
    SEPARATOR = 2


@dataclass
class Token:
    """ Class to store tokenized strings from a lexer. """
    lexeme: str
    start: int
    end: int
    token_type: TokenTypes

    def __repr__(self):
        return f"({self.token_type.name}: \"{self.lexeme}\"; @{self.start}" \
               f"-{self.end})"
