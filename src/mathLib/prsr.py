##
# @package prsr
#

from typing import Union
import random
import math
from .basics.tokens import Token
from .basics.tokens import TokenType
from .basics.nodes import *
from .basics.iterator import Iterator

# At start randomly initialize random generator seed
random.seed()

##
# @brief Parser class for assigning context to sequence of tokens
#
# Based on https://github.com/davidcallanan/py-myopl-code/blob/master/ep14/basic.py line 547 - 1250 and extended/corrected
#
class Parser:
  ##
  # @brief Init Parser with list of tokens from Tokenizer
  # Initialize iterator and load first token
  #
  # @param tokens List of tokens to parse
  #
  def __init__(self, tokens:list):
    self.token_interator = Iterator(tokens)

    self.current_token:Union[Token, None] = None
    self.move_forward()

  ##
  # @brief Call for next token in a list
  #
  def move_forward(self):
    try:
      self.current_token = self.token_interator.next()
    except:
      self.current_token = None

  ##
  # @brief Entrypoint for start parsing process
  #
  # @param debug Optional bool param for printing final results from parser
  # @return Node as node tree
  #
  def parse(self, debug:bool=False):
    # Before parsing check if some tokens are loaded
    if self.current_token is None:
      return None

    # Start parsing from expressions
    result = self.expr()

    if self.current_token is not None:
      raise SyntaxError(f"Failed to parse '{self.current_token}'")

    if debug:
      print(f"Debug parser output: {result}")
    return result

  ##
  # @brief Parse expressions
  #
  # This is case with lowest priority
  # We are checking for +- as binary operation (TERM + TERM or TERM - TERM)
  #
  # @return Node as node tree from rest of the operations
  #
  def expr(self):
    return self.binary_operation(self.term, (TokenType.PLUS, TokenType.MINUS))

  ##
  # @brief Parse term
  #
  # This is next priority after factor \n
  # We are checking for */ as binary operation (FACTOR * FACTOR or FACTOR / FACTOR)
  #
  # @return Node as node tree from rest of the operations
  #
  def term(self):
    return self.binary_operation(self.factor, (TokenType.MULTIPLY, TokenType.DIVIDE))

  ##
  # @brief Parse factor
  #
  # This is next prioryty after power operation \n
  # Here we are checking for +- as unary operation (+FACTOR or -FACTOR) \n
  # We are checking for factors again because on this level we can have multiple + or - before some value
  #
  # @return Node as node tree from rest of the operations
  #
  def factor(self):
    token = self.current_token
    if token is None:
      raise SyntaxError("Nothing to parse")

    if token.type in (TokenType.PLUS, TokenType.MINUS):
      self.move_forward()
      return UnaryOperationNode(token, self.factor())
    return self.power()

  ##
  # @brief This is next priority after atom operation \n
  # Here we are checking for power and root operation (ATOM^FACTOR or ATOM√FACTOR) \n
  # Everything before there operators needs to number or other before evaluated number
  #
  # @return Node as node tree from rest of the operations
  #
  def power(self):
    return self.binary_operation(self.atom, (TokenType.POW, TokenType.ROOT), self.factor)

  ##
  # @brief This is most priority operation \n
  # Its basic building block so there are numbers evaluated numbers, constants and buildin functions
  #
  # @return Node as node tree from rest of the operations
  #
  def atom(self):
    token = self.current_token
    if token is None:
      raise SyntaxError("Nothing to parse")

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
      return UnaryOperationNode(token, self.factor()) # We are evaluating factor for abs because when there are no parentecies then we are evaluating only next number with +-
    elif token.type == TokenType.LPAREN:
      self.move_forward()
      res = self.expr()

      if self.current_token is None or self.current_token.type != TokenType.RPAREN:
        raise SyntaxError("Expected ')'")

      self.move_forward()
      return res
    elif token.matches(TokenType.KEYWORD, "ln") or token.matches(TokenType.KEYWORD, "fact"):
      self.move_forward()
      return UnaryOperationNode(token, self.atom()) # We are evaluating only atom because fact can be done only for positive numbers so we dont need to include +-NUMBER

    raise SyntaxError("Unknown token")

  ##
  # @brief Helper function for parsing binary operations
  #
  # @return Node as node tree from rest of the operations
  #
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