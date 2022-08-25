from enum import Enum
from typing import Any

from Token import Token
from dataclasses import dataclass


# class NodeRoles(Enum):
#     """ type definitions for tokens """
#     START = 0
#     SIGN = 1
#     INT_PART = 2
#     FRAC_PART = 3


@dataclass
class Node:
    """ represents a node in the syntax tree """
    token: Token


@dataclass
class ErrorNode(Node):
    """ semper """
    error: str
    env: Any


@dataclass
class NumberNode(Node):
    """ Container node; equivalent to the Start Symbol """
    part: Any  # a link in the tree graph
    # TODO just rename it generically to node: Any or node: Union[Node, None]
    # or to be specific and artistic, then name it: start: Union[Node, None]


@dataclass
class FractionalPartNode(Node):
    """ should be the ultimate leaf node """
    value: Any

    def __str__(self):
        return f"({__name__}={self.value})"


@dataclass
class IntegerPartNode(FractionalPartNode):
    """ semper """
    fraction: Any  # a link in the tree graph
    # TODO just rename it generically to node: Any or node: Union[Node, None]


@dataclass
class OperationNode(Node):
    """ semper """
    argument: Node
    # TODO just rename it generically to node: Any or node: Union[Node, None]
