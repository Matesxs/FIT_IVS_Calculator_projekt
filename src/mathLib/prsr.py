from typing import Union
import random
import math
from .basics.tokens import Token
from .basics.tokens import TokenType
from .basics.nodes import *
from .basics.iterator import Iterator

random.seed()

class Parser:
  def __init__(self, tokens:list):
    self.token_interator = Iterator(tokens)

    self.current_token:Union[Token, None] = None
    self.move_forward()

  def move_forward(self):
    try:
      self.current_token = self.token_interator.next()
    except:
      self.current_token = None

  def parse(self):
    if self.current_token is None:
      return None

    result = self.expr()

    if self.current_token is not None:
      raise SyntaxError(f"Failed to parse '{self.current_token}'")

    return result

  def expr(self):
    return self.binary_operation(self.term, (TokenType.PLUS, TokenType.MINUS))

  def term(self):
    return self.binary_operation(self.factor, (TokenType.MULTIPLY, TokenType.DIVIDE))

  def factor(self):
    token = self.current_token

    if token.type in (TokenType.PLUS, TokenType.MINUS):
      self.move_forward()
      return UnaryOperationNode(token, self.factor())
    return self.power()

  def power(self):
    return self.binary_operation(self.atom, (TokenType.POW, TokenType.ROOT), self.factor)

  def atom(self):
    token = self.current_token

    if token.type == TokenType.NUMBER:
      self.move_forward()
      return NumberNode(token.value)
    elif token.matches(TokenType.KEYWORD, "rand"):
      self.move_forward()
      return NumberNode(random.random())
    elif token.matches(TokenType.KEYWORD, "e"):
      self.move_forward()
      return NumberNode(math.e)
    elif token.matches(TokenType.KEYWORD, "abs"):
      self.move_forward()
      return UnaryOperationNode(token, self.factor())
    elif token.type == TokenType.LPAREN:
      self.move_forward()
      res = self.expr()

      if self.current_token is None or self.current_token.type != TokenType.RPAREN:
        raise SyntaxError("Expected ')'")

      self.move_forward()
      return res
    elif token.matches(TokenType.KEYWORD, "ln") or token.matches(TokenType.KEYWORD, "fact"):
      self.move_forward()
      return UnaryOperationNode(token, self.atom())

  def binary_operation(self, func_a, operations, func_b=None):
    if func_b is None:
      func_b = func_a

    left = func_a()

    while self.current_token is not None and self.current_token.type in operations:
      operation_token = self.current_token
      self.move_forward()
      right = func_b()
      left = BinaryOperationNode(left, operation_token, right)

    return left