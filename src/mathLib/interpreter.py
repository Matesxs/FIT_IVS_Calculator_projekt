from .basics.number_class import Number
from .basics.nodes import *
from .basics.tokens import TokenType
from .basics.math_functions import MathFunctions

class Interpreter:
  def interpret_node_tree(self, node) -> Number:
    func_name = f"visit_{type(node).__name__}"
    function = getattr(self, func_name, self.no_visit_method)
    return function(node)

  def no_visit_method(self, node):
    raise RuntimeError(f"No visit_{type(node).__name__} function defined")

  def visit_NumberNode(self, node:NumberNode):
    return Number(node.value)

  def visit_UnaryOperationNode(self, node:UnaryOperationNode):
    number = self.interpret_node_tree(node.value).get_value()

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

    raise RuntimeError(f"Unknown unary operation token: {node.operation_token}")

  def visit_BinaryOperationNode(self, node:BinaryOperationNode):
    number1 = self.interpret_node_tree(node.value1).get_value()
    number2 = self.interpret_node_tree(node.value2).get_value()

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