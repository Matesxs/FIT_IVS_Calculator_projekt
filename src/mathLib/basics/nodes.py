from dataclasses import dataclass
from .tokens import Token

@dataclass
class NumberNode:
  value: float

  def __repr__(self):
    return f"{self.value}"

@dataclass
class UnaryOperationNode:
  operation_token: Token
  value: any

  def __repr__(self):
    return f"({self.operation_token.type.name}, {self.value})"

@dataclass
class BinaryOperationNode:
  value1: any
  operation_token: Token
  value2: any

  def __repr__(self):
    return f"({self.value1}, {self.operation_token.type.name}, {self.value2})"