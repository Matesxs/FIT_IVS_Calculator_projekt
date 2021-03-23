##
# @package nodes
#

from dataclasses import dataclass
from .tokens import Token

##
# @brief Base class for all nodes
#
@dataclass
class Node:
  ##
  # @brief Implementation requirement for each node for conversion to string
  #
  def __repr__(self):
    raise NotImplementedError("Implement in child classes")

##
# @brief Class for holding number node data
#
@dataclass
class NumberNode(Node):
  value: float

  ##
  # @brief Method for printing content of node
  #
  def __repr__(self):
    return f"{self.value}"

##
# @brief Class for holding data for unary operation
#
@dataclass
class UnaryOperationNode(Node):
  operation_token: Token
  value: any

  ##
  # @brief Method for printing content of node
  #
  def __repr__(self):
    return f"({self.operation_token.type.name if self.operation_token.value is None else str(self.operation_token.value).upper()}, {self.value})"

##
# @brief Class for holding data for binary operation
#
@dataclass
class BinaryOperationNode(Node):
  value1: any
  operation_token: Token
  value2: any

  ##
  # @brief Method for printing content of node
  #
  def __repr__(self):
    return f"({self.value1}, {self.operation_token.type.name if self.operation_token.value is None else str(self.operation_token.value).upper()}, {self.value2})"