from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
  NUMBER    =   0
  PLUS      =   1
  MINUS     =   2
  MULTIPLY  =   3
  DIVIDE    =   4
  POW       =   5
  ROOT      =   6 # "√"
  LPAREN    =   7
  RPAREN    =   8
  KEYWORD   =   9

@dataclass
class Token:
  type: TokenType
  value: any = None

  def matches(self, type:TokenType, value):
    return self.type == type and self.value == value

  def __repr__(self):
    return f"(TOKEN:{self.type.name}{f' VAL {self.value}' if self.value else ''})"