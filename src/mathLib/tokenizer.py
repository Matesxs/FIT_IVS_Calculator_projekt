from .basics.constants import DIGITS, WHITE_SPACE, LATTERS, KEYWORDS
from .basics.iterator import Iterator
from .basics.tokens import Token, TokenType

class Tokenizer:
  def __init__(self, text_input:str):
    self.text_iterator = Iterator(text_input)

    self.current_character = None
    self.move_forward()

  def move_forward(self):
    try:
      self.current_character = self.text_iterator.next()
    except:
      self.current_character = None

  def parse_input_text(self):
    tokens = []

    while self.current_character is not None:
      # Found white space - skip
      if self.current_character in WHITE_SPACE:
        self.move_forward()

      # We found number token
      elif self.current_character == "." or self.current_character in DIGITS:
        tokens.append(self.parse_number_token())

      elif self.current_character == "+":
        self.move_forward()
        tokens.append(Token(TokenType.PLUS))

      elif self.current_character == "-":
        self.move_forward()
        tokens.append(Token(TokenType.MINUS))

      elif self.current_character == "*":
        self.move_forward()
        tokens.append(Token(TokenType.MULTIPLY))

      elif self.current_character == "/":
        self.move_forward()
        tokens.append(Token(TokenType.DIVIDE))

      elif self.current_character == "^":
        self.move_forward()
        tokens.append(Token(TokenType.POW))

      elif self.current_character == "√":
        self.move_forward()
        tokens.append(Token(TokenType.ROOT))

      elif self.current_character == "(":
        self.move_forward()
        tokens.append(Token(TokenType.LPAREN))

      elif self.current_character == ")":
        self.move_forward()
        tokens.append(Token(TokenType.RPAREN))

      else:
        res = self.parse_parse_keyword()
        if not res:
          raise SyntaxError("Found invalid tokens in input")
        tokens.append(res)
    return tokens

  def parse_number_token(self):
    number_string = self.current_character
    decimal_place_token_found = self.current_character == "."

    self.move_forward()

    while self.current_character is not None and (self.current_character == "." or self.current_character in DIGITS):
      if self.current_character == ".":
        if decimal_place_token_found:
          break
        decimal_place_token_found = True

      number_string += self.current_character
      self.move_forward()

    if number_string.endswith("."):
      number_string += "0"
    elif number_string.startswith("."):
      number_string = "0" + number_string

    return Token(TokenType.NUMBER, float(number_string))

  def parse_parse_keyword(self):
    if self.current_character not in LATTERS:
      return None

    string_val = self.current_character
    self.move_forward()

    while self.current_character is not None and self.current_character in LATTERS:
      string_val += self.current_character
      self.move_forward()

    if string_val in KEYWORDS:
      return Token(TokenType.KEYWORD, string_val)
    return None