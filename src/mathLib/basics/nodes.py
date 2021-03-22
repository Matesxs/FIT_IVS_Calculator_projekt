from dataclasses import dataclass
from .tokens import Token

@dataclass
class Node:
  def __repr__(self):
    raise NotImplementedError("Implement in child classes")

@dataclass
class NumberNode(Node):
  value: float

  def __repr__(self):
    return f"{self.value}"

@dataclass
class UnaryOperationNode(Node):
  operation_token: Token
  value: any

  def __repr__(self):
    return f"({self.operation_token.type.name if self.operation_token.value is None else str(self.operation_token.value).upper()}, {self.value})"

@dataclass
class BinaryOperationNode(Node):
  value1: any
  operation_token: Token
  value2: any

  def __repr__(self):
    return f"({self.value1}, {self.operation_token.type.name if self.operation_token.value is None else str(self.operation_token.value).upper()}, {self.value2})"