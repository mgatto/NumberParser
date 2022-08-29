from typing import Any, Literal
from Token import Token
from dataclasses import dataclass


@dataclass
class Node:
    """ Base class represents a node in the syntax tree """
    token: Token


@dataclass
class ErrorNode(Node):
    """ Node returned in case of an error """
    error: str
    env: Any


@dataclass
class NumberNode(Node):
    """ Container node; equivalent to the Start Symbol """
    number: Node


@dataclass
class DecimalNumberNode(Node):
    part: Any  # a link in the tree graph


@dataclass
class FractionalPartNode(Node):
    """ should be the ultimate leaf node """
    value: Any

    def __str__(self):
        return f"({__name__}={self.value})"


@dataclass
class IntegerPartNode(FractionalPartNode):
    """ Represents the whole part of the decimal number """
    fraction: Any  # a link in the tree graph


@dataclass
class UnaryOperationNode(Node):
    """ Represents the sign of the number """
    sign: Literal["positive", "negative"]
    argument: Node
