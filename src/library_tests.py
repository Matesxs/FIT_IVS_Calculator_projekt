import unittest
import math
import mathLib
from mathLib import Tokenizer, Token, TokenType, Parser, nodes

class MathLibTestAdd(unittest.TestCase):
  def test_add_positive(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(0, 0), 0)
    self.assertEqual(mathLib.MathFunctions.add_operation(0, 5), 5)
    self.assertEqual(mathLib.MathFunctions.add_operation(2, 0), 2)
    self.assertEqual(mathLib.MathFunctions.add_operation(1, 3), 4)
    self.assertEqual(mathLib.MathFunctions.add_operation(1111, 500), 1611)

  def test_add_negative(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(-1, -2), -3)
    self.assertEqual(mathLib.MathFunctions.add_operation(-5, 0), -5)
    self.assertEqual(mathLib.MathFunctions.add_operation(0, -8), -8)
    self.assertEqual(mathLib.MathFunctions.add_operation(-255, -255), -510)

  def test_add_positive_negative(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(-5, 10), 5)
    self.assertEqual(mathLib.MathFunctions.add_operation(-12, 10), -2)
    self.assertEqual(mathLib.MathFunctions.add_operation(2, -10), -8)
    self.assertEqual(mathLib.MathFunctions.add_operation(3, -1), 2)
    self.assertEqual(mathLib.MathFunctions.add_operation(-12, 12), 0)

  def test_add_decimal(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(-1.2, 4.2), 3)
    self.assertEqual(mathLib.MathFunctions.add_operation(6.7, -2.2), 4.5)
    self.assertEqual(mathLib.MathFunctions.add_operation(-5.2, -2.7), -7.9)

  def test_add_mixed(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(-5, 2.4), -2.6)
    self.assertEqual(mathLib.MathFunctions.add_operation(3, -6.2), -3.2)
    self.assertEqual(mathLib.MathFunctions.add_operation(-3.2, 10), 6.8)

class MathLibTestSub(unittest.TestCase):
  def test_sub_positive(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(0, 0), 0)
    self.assertEqual(mathLib.MathFunctions.sub_operation(4, 6), -2)
    self.assertEqual(mathLib.MathFunctions.sub_operation(2, 0), 2)
    self.assertEqual(mathLib.MathFunctions.sub_operation(0, 4), -4)
    self.assertEqual(mathLib.MathFunctions.sub_operation(255, 55), 200)

  def test_sub_negatibe(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(0, -4), 4)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-6, 0), -6)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-12, -4), -8)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-2, -6), 4)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-600, -820), 220)

  def test_sub_positive_negative(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(-6, 5), -11)
    self.assertEqual(mathLib.MathFunctions.sub_operation(5, 2), 3)
    self.assertEqual(mathLib.MathFunctions.sub_operation(3, -6), 9)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-25, -6), -19)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-300, 120), -420)

  def test_sub_decimal(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(-2.3, 2.6), -4.9)
    self.assertEqual(mathLib.MathFunctions.sub_operation(6.4, 1.2), 5.2)
    self.assertEqual(mathLib.MathFunctions.sub_operation(3.8, -0.2), 4)

  def test_sub_mixed(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(-6, 2.4), -8.4)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-1.2, 4), -5.2)
    self.assertEqual(mathLib.MathFunctions.sub_operation(2.4, -4.5), 6.9)

class MathLibTestMult(unittest.TestCase):
  def test_mult_positive(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(5, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(255, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(3, 1), 3)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(6, 3), 18)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(1, 10), 10)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, 10), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, 60), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(11, 11), 121)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(600, 33), 19800)

  def test_mult_negative(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-1, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, -5), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-3, -2), 6)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, -300), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-245, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-10, -2), 20)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-3, -3), 9)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-33, -45), 1485)

  def test_mult_positive_negative(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-10, 2), -20)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(2, -8), -16)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-44, 22), -968)

  def test_mult_decimal(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(2.2, 4.6), 10.12)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-6.3, 3.5), -22.05)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(2.1, -4.6), -9.66)

  def test_mult_mixed(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-4.5, 4), -18)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(2.25, -16), -36)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(10, -3.3), -33)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-2, 4.8), -9.6)

class MathLibTestDiv(unittest.TestCase):
  def test_div_positive(self):
    self.assertEqual(mathLib.MathFunctions.divide_operation(0, 5), 0)
    self.assertEqual(mathLib.MathFunctions.divide_operation(20, 5), 4)
    self.assertEqual(mathLib.MathFunctions.divide_operation(3, 3), 1)
    self.assertEqual(mathLib.MathFunctions.divide_operation(6, 4), 1.5)
    self.assertEqual(mathLib.MathFunctions.divide_operation(2, 20), 0.1)
    self.assertEqual(mathLib.MathFunctions.divide_operation(500, 40), 12.5)

  def test_division_by_zero(self):
    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.divide_operation(3, 0)

    with self.assertRaises(RuntimeError):
      self.assertRaises(mathLib.MathFunctions.divide_operation(600, 0))

class MathLibTestTokenizer(unittest.TestCase):
  def test_empty(self):
    self.assertEqual(Tokenizer("").parse_input_text(), [])
    self.assertEqual(Tokenizer("     ").parse_input_text(), [])
    self.assertEqual(Tokenizer("\t\t\t").parse_input_text(), [])
    self.assertEqual(Tokenizer("\n\n\n\n\n").parse_input_text(), [])
    self.assertEqual(Tokenizer("\t   \t\t\t  \n\t\n  \n").parse_input_text(), [])

  def test_multidecimal(self):
    self.assertEqual(Tokenizer("...").parse_input_text(), [
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0)
    ])

  def test_invalid_chars(self):
    with self.assertRaises(SyntaxError):
      Tokenizer("&;`#%").parse_input_text()

  def test_numbers(self):
    tokens = Tokenizer("124 256.123 999. .256 . 00000000000000.321").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.NUMBER, 124),
      Token(TokenType.NUMBER, 256.123),
      Token(TokenType.NUMBER, 999.0),
      Token(TokenType.NUMBER, 0.256),
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.321)
    ])

  def test_operators(self):
    tokens = Tokenizer("+-*/√^").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.PLUS),
      Token(TokenType.MINUS),
      Token(TokenType.MULTIPLY),
      Token(TokenType.DIVIDE),
      Token(TokenType.ROOT),
      Token(TokenType.POW)
    ])

  def test_keywords(self):
    tokens = Tokenizer("rand ln fact abs e").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.KEYWORD, "rand"),
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.KEYWORD, "e"),
    ])
    
    with self.assertRaises(SyntaxError):
      Tokenizer("randlnfactabse").parse_input_text()

  def test_parents(self):
    tokens = Tokenizer("()").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN)
    ])

    tokens = Tokenizer("(()())").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN)
    ])

    tokens = Tokenizer("((()").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
    ])

  def test_combined(self):
    tokens = Tokenizer("25 + 33 * ln(55)^2 * (33 - 11.22) + e").parse_input_text()
    self.assertEqual(tokens, [
      Token(TokenType.NUMBER, 25),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 33),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 55),
      Token(TokenType.RPAREN),
      Token(TokenType.POW),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 33),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 11.22),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.KEYWORD, "e"),
    ])

class MathLibTestParser(unittest.TestCase):
  def test_empty(self):
    node_tree = Parser([]).parse()
    self.assertEqual(node_tree, None)

  def test_unknown_token(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fafsafasfasfasfasfawsfwa")]).parse()

  def test_numbers(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 124.34)]).parse(), nodes.NumberNode(124.34))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 321)]).parse(), nodes.NumberNode(321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 0)]).parse(), nodes.NumberNode(0))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -321)]).parse(), nodes.NumberNode(-321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -51.3)]).parse(), nodes.NumberNode(-51.3))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "e")]).parse(), nodes.NumberNode(math.e))
    self.assertIsInstance(Parser([Token(TokenType.KEYWORD, "rand")]).parse(), nodes.NumberNode)

  def test_binary_operations(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.PLUS), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MINUS), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.MINUS), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.MULTIPLY), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.DIVIDE), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.POW), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.POW), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.ROOT), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.ROOT), nodes.NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.DIVIDE), nodes.NumberNode(50)))

  def test_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.PLUS), Token(TokenType.NUMBER, 11)]).parse(), nodes.UnaryOperationNode(Token(TokenType.PLUS), nodes.NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.MINUS), Token(TokenType.NUMBER, 11)]).parse(), nodes.UnaryOperationNode(Token(TokenType.MINUS), nodes.NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "abs"), Token(TokenType.NUMBER, 11)]).parse(), nodes.UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), nodes.NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 11)]).parse(), nodes.UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), nodes.NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "ln"), Token(TokenType.NUMBER, 11)]).parse(), nodes.UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), nodes.NumberNode(11)))

  def test_parents(self):
    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.PLUS), nodes.NumberNode(50)))

    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.PLUS), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     nodes.BinaryOperationNode(nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.PLUS), nodes.NumberNode(50)), Token(TokenType.PLUS), nodes.BinaryOperationNode(nodes.NumberNode(25), Token(TokenType.PLUS), nodes.NumberNode(50))))

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

  def test_operation_order(self):
    

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

if __name__ == '__main__':
  unittest.main()