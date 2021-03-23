##
# @package tokens
#

from dataclasses import dataclass
from enum import Enum

##
# @brief Enum class for holding token type
#
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

##
# @brief Class for holding data of each token
#
@dataclass
class Token:
  type: TokenType
  value: any = None

  ##
  # @brief Check if token matches type and value
  #
  # @param type TokenType for comparison
  # @param value Value for comparison
  # @return Bool True if they matches else False
  #
  def matches(self, type:TokenType, value):
    return self.type == type and self.value == value

  ##
  # @brief Method for printing content of token
  #
  def __repr__(self):
    return f"(TOKEN:{self.type.name}{f' VAL {self.value}' if self.value else ''})"