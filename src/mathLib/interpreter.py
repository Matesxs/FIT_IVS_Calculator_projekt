##
# @package interpreter
#

from .basics.number_class import Number
from .basics.nodes import *
from .basics.tokens import TokenType
from .basics.math_functions import MathFunctions

##
# @brief Interpreter class for executing functions based on input node tree
#
# Based on https://github.com/davidcallanan/py-myopl-code/blob/master/ep14/basic.py line 1908 - 2156 and extended/corrected
#
class Interpreter:
  ##
  # @brief Entry point for interpreting node tree
  #
  # Entry point for interpreting node tree \n
  # Called recursively for whole tree
  #
  # @param node Node of node tree
  # @return Interpreted number of Number class of current part of tree
  #
  def interpret(self, node:Node) -> Number:
    func_name = f"visit_{type(node).__name__}"
    function = getattr(self, func_name, self.no_visit_method)
    return function(node)

  ##
  # @brief Default method if unknown node is passed
  #
  def no_visit_method(self, node):
    raise RuntimeError(f"No visit_{type(node).__name__} function defined")

  ##
  # @brief Interpret basic number node
  #
  # Most simple building block
  #
  # @param node NumberNode to parse
  # @return Number with value from node
  #
  def visit_NumberNode(self, node:NumberNode):
    return Number(node.value)

  ##
  # @brief Interpret UnaryOperationNode
  #
  # Get value from node, interpret it and based on operation token choose operation
  #
  # @param node UnaryOperationNode to parse
  # @return Number with value returned from math function
  #
  def visit_UnaryOperationNode(self, node:UnaryOperationNode):
    number = self.interpret(node.value).get_value()

    if node.operation_token.type == TokenType.MINUS:
      return Number(MathFunctions.invert_operation(number))
    elif node.operation_token.type == TokenType.PLUS:
      return Number(number)
    elif node.operation_token.matches(TokenType.KEYWORD, "fact"):
      return Number(MathFunctions.factorial_operation(number))
    elif node.operation_token.matches(TokenType.KEYWORD, "ln"):
      return Number(MathFunctions.natural_log_operation(number))
    elif node.operation_token.matches(TokenType.KEYWORD, "abs"):
      return Number(MathFunctions.abs_operation(number))
    elif node.operation_token.matches(TokenType.KEYWORD, "sqrt"):
      return Number(MathFunctions.root_operation(2, number))

    raise RuntimeError(f"Unknown unary operation token: {node.operation_token}")

  ##
  # @brief Interpret BinaryOperationNode
  #
  # Get values from node, interpret them and based on operation token choose operation
  #
  # @param node BinaryOperationNode to parse
  # @return Number with value returned from math function
  #
  def visit_BinaryOperationNode(self, node:BinaryOperationNode):
    number1 = self.interpret(node.value1).get_value()
    number2 = self.interpret(node.value2).get_value()

    if node.operation_token.type == TokenType.PLUS:
      return Number(MathFunctions.add_operation(number1, number2))
    elif node.operation_token.type == TokenType.MINUS:
      return Number(MathFunctions.sub_operation(number1, number2))
    elif node.operation_token.type == TokenType.MULTIPLY:
      return Number(MathFunctions.multiply_operation(number1, number2))
    elif node.operation_token.type == TokenType.DIVIDE:
      return Number(MathFunctions.divide_operation(number1, number2))
    elif node.operation_token.type == TokenType.POW:
      return Number(MathFunctions.power_operation(number1, number2))
    elif node.operation_token.type == TokenType.ROOT:
      return Number(MathFunctions.root_operation(number1, number2))

    raise RuntimeError(f"Unknown unary operation token: {node.operation_token}")