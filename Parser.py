""" Provide support for parsing tokens """
from typing import List, Union

from Node import NumberNode, DecimalNumberNode, Node, ErrorNode, UnaryOperationNode, \
    IntegerPartNode
from Token import Token, TokenTypes


class Parser:
    """ a recursive descent parser for number strings """
    token_list = []
    current_token: Union[Token, None]

    def __init__(self, tokens: List[Token]):
        self.token_list = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.token_list)
        except StopIteration:
            self.current_token = None

    # could also be named "start()"
    def parse(self):
        if self.current_token is None:
            return None

        # the root of the AST
        # TODO maybe the first advance() should be here?
        result = self.number()
        return result

        if self.current_token is not None:
            return ErrorNode(token=self.current_token, error="Bad syntax")
        else:
            return result

    def number(self):
        # print(f"current token in number()={self.current_token}")

        decimal_number = self.decimal_number()
        num_node = NumberNode(token=None, number=decimal_number)

        return num_node

    def decimal_number(self):
        # what kind of token?

        # sign is optional
        if self.current_token.token_type == TokenTypes.UNARY_SIGN:
            result = self.sign()
        elif self.current_token.token_type == TokenTypes.DECIMAL_DIGITS:
            result = self.int_part()

        # print(f"result of self.sign()={result}")
        if result is None:
            return ErrorNode(token=self.current_token, error="Syntax error")

        dec_node = DecimalNumberNode(token=None, part=result)
        return dec_node

    def sign(self):
        # print(f"current token in sign()={self.current_token}")

        if self.current_token is not None and self.current_token.token_type == TokenTypes.UNARY_SIGN:
            sign_node = UnaryOperationNode(
                token=self.current_token, sign="negative", argument=None)

            # next node should be an int_part
            self.advance()  # self.current_token should now be of type DECIMAL_DIGITS
            result = self.int_part()
            if result is None:
                return ErrorNode(token=self.current_token,
                                 error="Syntax error from int_part()")
            elif isinstance(result, ErrorNode):
                return result
            else:
                sign_node.argument = result
                return sign_node
        else:
            return None  # signal to callee to disregard this optional node

    def int_part(self) -> Union[Node, None]:
        # print(f"Current Token in int_part()= {self.current_token}")

        if self.current_token is not None and self.current_token.token_type \
                == TokenTypes.DECIMAL_DIGITS:
            integer_part = IntegerPartNode(token=self.current_token, value=int(
                self.current_token.lexeme), fraction=None)

            # we expect the next node, if any to be a separator
            self.advance()
            result = self.separator()
        else:
            return ErrorNode(token=self.current_token, error="Syntax error")

        integer_part.fraction = result
        return integer_part

    def separator(self):
        # print(f"current token in separator()={self.current_token}")

        if self.current_token is not None and self.current_token == \
                TokenTypes.SEPARATOR:
            # then we have a fraction!
            self.advance()
            result = self.frac_part()
            return result

    def frac_part(self):
        # print(f"current token in frac_part()={self.current_token}")
        pass
