##
# @package library_tests
#

import unittest
import math
from mathLib import MathFunctions
from mathLib import Tokenizer, Token, TokenType, Parser, Interpreter, Number
from mathLib.basics.nodes import *
from mathLib.entry_point import interpret_text_input

##
# @brief Test mathematic operations of math library
#
class MathLibTestBasicFunctions(unittest.TestCase):
  ##
  # @brief Test valid cases of function add
  #
  def test_add(self):
    self.assertEqual(MathFunctions.add_operation(0, 5), 5)
    self.assertEqual(MathFunctions.add_operation(2, 0), 2)

    self.assertEqual(MathFunctions.add_operation(-5, 0), -5)
    self.assertEqual(MathFunctions.add_operation(5, -8), -3)

    self.assertEqual(MathFunctions.add_operation(-5, 2.4), -2.6)
    self.assertEqual(MathFunctions.add_operation(3, -6.2), -3.2)
    self.assertEqual(MathFunctions.add_operation(-3.2, 10), 6.8)

  ##
  # @brief Test valid cases of function subtract
  #
  def test_sub(self):
    self.assertEqual(MathFunctions.sub_operation(0, 0), 0)
    self.assertEqual(MathFunctions.sub_operation(4, 6), -2)
    self.assertEqual(MathFunctions.sub_operation(2, 0), 2)
    self.assertEqual(MathFunctions.sub_operation(255, 55), 200)

    self.assertEqual(MathFunctions.sub_operation(0, -4), 4)
    self.assertEqual(MathFunctions.sub_operation(-12, -4), -8)

    self.assertEqual(MathFunctions.sub_operation(-6, 2.4), -8.4)
    self.assertEqual(MathFunctions.sub_operation(-1.2, 4), -5.2)
    self.assertEqual(MathFunctions.sub_operation(2.4, -4.5), 6.9)

  ##
  # @brief Test valid cases of function multiply
  #
  def test_mult(self):
    self.assertEqual(MathFunctions.multiply_operation(255, 0), 0)
    self.assertEqual(MathFunctions.multiply_operation(0, 10), 0)
    self.assertEqual(MathFunctions.multiply_operation(6, 3), 18)

    self.assertEqual(MathFunctions.multiply_operation(-1, 0), 0)
    self.assertEqual(MathFunctions.multiply_operation(0, -5), 0)
    self.assertEqual(MathFunctions.multiply_operation(-33, -45), 1485)
    self.assertEqual(MathFunctions.multiply_operation(-45, 2), -90)
    self.assertEqual(MathFunctions.multiply_operation(45, -2), -90)

    self.assertEqual(MathFunctions.multiply_operation(-4.5, 4), -18)
    self.assertEqual(MathFunctions.multiply_operation(2.25, -16), -36)
    self.assertEqual(MathFunctions.multiply_operation(10, -3.3), -33)
    self.assertEqual(MathFunctions.multiply_operation(-2, 4.8), -9.6)

  ##
  # @brief Test valid cases of function divide
  #
  def test_div(self):
    self.assertEqual(MathFunctions.divide_operation(0, 5), 0)
    self.assertEqual(MathFunctions.divide_operation(20, 5), 4)
    self.assertEqual(MathFunctions.divide_operation(6, 4), 1.5)

    self.assertEqual(MathFunctions.divide_operation(0, -5), 0)
    self.assertEqual(MathFunctions.divide_operation(9, -3), -3)
    self.assertEqual(MathFunctions.divide_operation(-36, -4), 9)
    self.assertEqual(MathFunctions.divide_operation(-5, 5), -1)

    self.assertEqual(MathFunctions.divide_operation(6.2, 4), 1.55)
    self.assertEqual(MathFunctions.divide_operation(3, -6.5), -0.46153846153846153846153846153846)
    self.assertEqual(MathFunctions.divide_operation(-5.5, -6.5), 0.84615384615384615384615384615385)

  ##
  # @brief Test divide function on division by zero
  #
  # Division by zero is invalid mathematical operation
  #
  def test_division_by_zero(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.divide_operation(3, 0)

    with self.assertRaises(RuntimeError):
      MathFunctions.divide_operation(5.65, 0)

    with self.assertRaises(RuntimeError):
      MathFunctions.divide_operation(-3, 0)

    with self.assertRaises(RuntimeError):
      MathFunctions.divide_operation(-5.65, 0)

  ##
  # @brief Test valid cases of function power for operations with zero
  #
  def test_pow_op_with_zero(self):
    self.assertEqual(MathFunctions.power_operation(0, 0), 1)
    self.assertEqual(MathFunctions.power_operation(0, 12), 0)
    self.assertEqual(MathFunctions.power_operation(12, 0), 1)

  ##
  # @brief Test valid cases of function power
  #
  def test_pow(self):
    self.assertEqual(MathFunctions.power_operation(2, 2), 4)
    self.assertEqual(MathFunctions.power_operation(2.4, 2), 5.76)
    self.assertEqual(MathFunctions.power_operation(2.4, 4.52), 52.306397819793965)

    self.assertEqual(MathFunctions.power_operation(2, -2), 0.25)
    self.assertEqual(MathFunctions.power_operation(-2, 2), 4)
    self.assertEqual(MathFunctions.power_operation(-2, -2), 0.25)
    self.assertEqual(MathFunctions.power_operation(-2.32, -3), -0.08008220919266884)

  ##
  # @brief Test valid cases of function nroot
  #
  def test_root(self):
    self.assertEqual(MathFunctions.root_operation(8, 0), 0)
    self.assertEqual(MathFunctions.root_operation(2, 4), 2)
    self.assertEqual(MathFunctions.root_operation(8, 2.2), 1.1035774941665433)
    self.assertEqual(MathFunctions.root_operation(4.8, 3.25), 1.2783281919978795)

    self.assertEqual(MathFunctions.root_operation(-2, 4), 0.5)
    self.assertEqual(MathFunctions.root_operation(-3.15, 3.45), 0.6749378431838611)

  ##
  # @brief Test nroot of negative numbers
  #
  # Can't do root on negative number without using imaginary numbers.
  #
  def test_root_negative_base(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -5)

    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(2, -2.485)

  ##
  # @brief Test nroot with zero n
  #
  # Root of zero n is not defined
  #
  def test_nroot_zero_n(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 2)

    with self.assertRaises(RuntimeError):
      MathFunctions.root_operation(0, 5.32)

  ##
  # @brief Test valid cases of function natural logarithm
  #
  def test_ln(self):
    self.assertEqual(MathFunctions.natural_log_operation(1), 0)
    self.assertEqual(MathFunctions.natural_log_operation(0.5), -0.6931471805599453)
    self.assertEqual(MathFunctions.natural_log_operation(1.2), 0.1823215567939546)
    self.assertEqual(MathFunctions.natural_log_operation(4), 1.3862943611198906)

  ##
  # @brief Test natural logarithm of zero
  #
  # Natural logarithm is not defined for zero
  #
  def test_ln_zero(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(0)

  ##
  # @brief Test natural logarithm of negative numbers
  #
  # Natural logarithm is not defined for negative numbers
  #
  def test_ln_negative_numbers(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-1)

    with self.assertRaises(RuntimeError):
      MathFunctions.natural_log_operation(-2.25)

  ##
  # @brief Test valid cases of function factorial
  #
  def test_fact(self):
    self.assertEqual(MathFunctions.factorial_operation(0), 1)
    self.assertEqual(MathFunctions.factorial_operation(1), 1)
    self.assertEqual(MathFunctions.factorial_operation(4), 24)

  ##
  # @brief Test factorial of float numbers
  #
  # Factorial of float numbers in undefined
  #
  def test_fact_positive_float_numbers(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(3.35)

    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(12.87)

  ##
  # @brief Test factorial of negative numbers
  #
  # Factorial of negative numbers is undefined
  #
  def test_fact_negative_numbers(self):
    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-5)

    with self.assertRaises(RuntimeError):
      MathFunctions.factorial_operation(-4.2)

  ##
  # @brief Test valid cases of invert function
  #
  def test_invert(self):
    self.assertEqual(MathFunctions.invert_operation(0), 0)
    self.assertEqual(MathFunctions.invert_operation(-5), 5)
    self.assertEqual(MathFunctions.invert_operation(5), -5)
    self.assertEqual(MathFunctions.invert_operation(5.369), -5.369)
    self.assertEqual(MathFunctions.invert_operation(-5.369), 5.369)

##
# @brief Testing Tokenizer class of math library
#
class MathLibTestTokenizer(unittest.TestCase):
  ##
  # @brief Test empty input string
  #
  def test_empty(self):
    self.assertEqual(Tokenizer("").tokenize(), [])
    self.assertEqual(Tokenizer("     ").tokenize(), [])
    self.assertEqual(Tokenizer("\t\t\t").tokenize(), [])
    self.assertEqual(Tokenizer("\n\n\n\n\n").tokenize(), [])
    self.assertEqual(Tokenizer("\t   \t\t\t  \n\t\n  \n").tokenize(), [])

  ##
  # @brief Test multiple decimal dots as series of zeroes
  #
  def test_multidecimal(self):
    self.assertEqual(Tokenizer("...").tokenize(), [
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.0)
    ])

  ##
  # @brief Test example of invalid characters
  #
  def test_invalid_chars(self):
    with self.assertRaises(SyntaxError):
      Tokenizer("&;`#%").tokenize()

    with self.assertRaises(SyntaxError):
      Tokenizer("&; rand `#%").tokenize()

    with self.assertRaises(SyntaxError):
      Tokenizer("e &; rand `#%").tokenize()

  ##
  # @brief Test number input
  #
  def test_numbers(self):
    tokens = Tokenizer("124 256.123 999. .256 . 00000000000000.321").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.NUMBER, 124),
      Token(TokenType.NUMBER, 256.123),
      Token(TokenType.NUMBER, 999.0),
      Token(TokenType.NUMBER, 0.256),
      Token(TokenType.NUMBER, 0.0),
      Token(TokenType.NUMBER, 0.321)
    ])

  ##
  # @brief Test operators
  #
  def test_operators(self):
    tokens = Tokenizer("+-*/???^").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.PLUS),
      Token(TokenType.MINUS),
      Token(TokenType.MULTIPLY),
      Token(TokenType.DIVIDE),
      Token(TokenType.ROOT),
      Token(TokenType.POW)
    ])

  ##
  # @brief Test keywords
  #
  def test_keywords(self):
    tokens = Tokenizer("rand ln fact abs e").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.KEYWORD, "rand"),
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.KEYWORD, "e"),
    ])

  ##
  # @brief Test parentecies
  #
  def test_parents(self):
    tokens = Tokenizer("()").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN)
    ])

    tokens = Tokenizer("(()())").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN)
    ])

    tokens = Tokenizer("((()").tokenize()
    self.assertEqual(tokens, [
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.LPAREN),
      Token(TokenType.RPAREN),
    ])

  def test_combined(self):
    tokens = Tokenizer("25 + 33 * ln(55)^2 * (33 - 11.22) + e / abs(36 - fact(5)) + rand").tokenize()
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
      Token(TokenType.DIVIDE),
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 36),
      Token(TokenType.MINUS),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 5),
      Token(TokenType.RPAREN),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.KEYWORD, "rand"),
    ])

  ##
  # @brief Test combination of valid and invalid tokens
  #
  def test_invalid_expressions(self):
    with self.assertRaises(SyntaxError):
      Tokenizer("randlnfactabse").tokenize()

    with self.assertRaises(SyntaxError):
      Tokenizer("rand 956. tan 14").tokenize()

    with self.assertRaises(SyntaxError):
      Tokenizer("25 + 33 * l(55)^2 * (33 - 11.22) + e").tokenize()

##
# @brief Testing Parser class of math library
#
class MathLibTestParser(unittest.TestCase):
  ##
  # @brief Test empty list of tokens
  #
  def test_empty(self):
    node_tree = Parser([]).parse()
    self.assertEqual(node_tree, None)

  ##
  # @brief Test unknown tokens
  #
  def test_unknown_token(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fafsafasfasfasfasfawsfwa")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "randbla")]).parse()

  ##
  # @brief Test parsing numbers
  #
  def test_numbers(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 124.34)]).parse(), NumberNode(124.34))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 321)]).parse(), NumberNode(321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 0)]).parse(), NumberNode(0))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -51.3)]).parse(), NumberNode(-51.3))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "e")]).parse(), NumberNode(math.e))
    self.assertIsInstance(Parser([Token(TokenType.KEYWORD, "rand")]).parse(), NumberNode)

  ##
  # @brief Test parsing binary operations
  #
  def test_binary_operations(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MINUS), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.MINUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.MULTIPLY), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.POW), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.POW), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.ROOT), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.ROOT), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))

  ##
  # @brief Test parsing unary operations
  #
  def test_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.PLUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.PLUS), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.MINUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.MINUS), NumberNode(11)))

  ##
  # @brief Test parsing keyword unary operations
  #
  def test_keyword_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "abs"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "ln"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(11)))

  ##
  # @brief Test parsing valid operations with parentecies
  #
  def test_valid_parents(self):
    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))

    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.PLUS), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)), Token(TokenType.PLUS), BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50))))

  ##
  # @brief Test parsing invalid operations with parentecies
  #
  def test_invalid_parents(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

  ##
  # @brief Test parsing complex operations and operations order
  #
  def test_operation_order(self):
    # ---5
    tokens = [
      Token(TokenType.MINUS),
      Token(TokenType.MINUS),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 5),
    ]
    self.assertEqual(str(Parser(tokens).parse()), "(MINUS, (MINUS, (MINUS, 5)))")

    # -e^255 / (2 * ln 3 - 8) + 16
    tokens = [
      Token(TokenType.MINUS),
      Token(TokenType.KEYWORD, "e"),
      Token(TokenType.POW),
      Token(TokenType.NUMBER, 255),
      Token(TokenType.DIVIDE),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "ln"),
      Token(TokenType.NUMBER, 3),
      Token(TokenType.MINUS),
      Token(TokenType.NUMBER, 8),
      Token(TokenType.RPAREN),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 16),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "(((MINUS, (2.718281828459045, POW, 255)), DIVIDE, ((2, MULTIPLY, (LN, 3)), MINUS, 8)), PLUS, 16)")

    # abs -15 + 30 * fact 2 * 3
    tokens = [
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.NUMBER, -15),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 30),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 3),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "((ABS, -15), PLUS, ((30, MULTIPLY, (FACT, 2)), MULTIPLY, 3))")

    # abs(-15 + 30) * fact 2 * 3
    tokens = [
      Token(TokenType.KEYWORD, "abs"),
      Token(TokenType.LPAREN),
      Token(TokenType.NUMBER, -15),
      Token(TokenType.PLUS),
      Token(TokenType.NUMBER, 30),
      Token(TokenType.RPAREN),
      Token(TokenType.MULTIPLY),
      Token(TokenType.KEYWORD, "fact"),
      Token(TokenType.NUMBER, 2),
      Token(TokenType.MULTIPLY),
      Token(TokenType.NUMBER, 3),
    ]

    self.assertEqual(str(Parser(tokens).parse()), "(((ABS, (-15, PLUS, 30)), MULTIPLY, (FACT, 2)), MULTIPLY, 3)")

  ##
  # @brief Test parsing invalid input with only operators
  #
  def test_only_operator_input(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.PLUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MINUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "abs")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "ln")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact")]).parse()

  def test_invalid_multi_operations(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MULTIPLY), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 10)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 10), Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 10), Token(TokenType.MULTIPLY), Token(TokenType.MULTIPLY), Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.POW), Token(TokenType.POW), Token(TokenType.NUMBER, 10)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.ROOT), Token(TokenType.NUMBER, 10), Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 10), Token(TokenType.ROOT), Token(TokenType.POW), Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.MINUS), Token(TokenType.MINUS), Token(TokenType.NUMBER, 10), Token(TokenType.MINUS), Token(TokenType.POW), Token(TokenType.NUMBER, 10)]).parse()

  ##
  # @brief Test parsing unfinished expressions
  #
  def test_unfinished_expesions(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.PLUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.MINUS)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.MULTIPLY)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.DIVIDE)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.POW)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.ROOT)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "abs")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "ln")]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 5), Token(TokenType.KEYWORD, "fact")]).parse()

##
# @brief Testing Interpreter class of math library
#
class MathLibTestInterpreter(unittest.TestCase):
  ##
  # @brief Create parser instance
  #
  def setUp(self) -> None:
    self.interpreter = Interpreter()

  ##
  # @brief Testing interpretation of numbers
  #
  def test_numbers(self):
    self.assertEqual(self.interpreter.interpret(NumberNode(0)), Number(0))
    self.assertEqual(self.interpreter.interpret(NumberNode(256)), Number(256))
    self.assertEqual(self.interpreter.interpret(NumberNode(-128)), Number(-128))
    self.assertEqual(self.interpreter.interpret(NumberNode(-12.65)), Number(-12.65))
    self.assertEqual(self.interpreter.interpret(NumberNode(16.7)), Number(16.7))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(10.6))), Number(10.6))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(10.6))), Number(-10.6))

  ##
  # @brief Testing interpretation of binary operations
  #
  def test_binary_operations(self):
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.PLUS), NumberNode(5))), Number(8))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.PLUS), NumberNode(2.25))), Number(8.5))

    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.MINUS), NumberNode(5))), Number(-2))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.MINUS), NumberNode(2.25))), Number(4))

    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.MULTIPLY), NumberNode(5))), Number(15))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.MULTIPLY), NumberNode(2.25))), Number(14.0625))

    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.DIVIDE), NumberNode(5))), Number(0.6))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.DIVIDE), NumberNode(2.25))), Number(2.7777777777777777777777777777778))

    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(3), Token(TokenType.POW), NumberNode(5))), Number(243))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.POW), NumberNode(2.25))), Number(61.763235550163658828103389539702))

    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(5), Token(TokenType.ROOT), NumberNode(3))), Number(1.2457309396155173259666803366403))
    self.assertEqual(self.interpreter.interpret(BinaryOperationNode(NumberNode(2.25), Token(TokenType.ROOT), NumberNode(6.25))), Number(2.2580026753417055949906722148876))

  ##
  # @brief Testing interpretation of unary operations
  #
  def test_unary_operations(self):
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(0))), Number(0))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(0))), Number(0))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(10.6))), Number(10.6))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(10.6))), Number(-10.6))

    self.assertAlmostEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(5))).get_value(), Number(1.6094379124341003746007593332262).get_value())
    self.assertAlmostEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(1.1))).get_value(), Number(0.09531017980432486004395212328077).get_value())

    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(10.456))), Number(10.456))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(-10.456))), Number(10.456))

    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(5))), Number(120))
    self.assertEqual(self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(0))), Number(1))

  ##
  # @brief Testing interpretation of invalid function parameters
  #
  def test_invalid_cases(self):
    # Result is imaginary number that is not supported
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(2.25), Token(TokenType.ROOT), NumberNode(-6.25)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(0), Token(TokenType.ROOT), NumberNode(6.25)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(6.25), Token(TokenType.DIVIDE), NumberNode(0)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(0)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(-2.5)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(-2)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(3.35)))

  ##
  # @brief Testing interpretation of unknown tokens
  #
  def test_invalid_operations(self):
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(UnaryOperationNode(Token(TokenType.KEYWORD, "fasfafasfa"), NumberNode(3.35)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret(BinaryOperationNode(NumberNode(8), Token(TokenType.KEYWORD, "wtwtta"), NumberNode(3.35)))

##
# @brief Testing entrypoint for UI
#
class MathLibTestExpressions(unittest.TestCase):
  ##
  # @brief Testing interpretation of empty input
  #
  def test_empty_input(self):
    self.assertEqual(interpret_text_input(""), "0")

  ##
  # @brief Testing interpretation of special cases that should interpret to zero
  #
  def test_special_zero_cases(self):
    self.assertEqual(interpret_text_input("00000000000000"), "0")
    self.assertEqual(interpret_text_input("0000000.000"), "0")
    self.assertEqual(interpret_text_input("             "), "0")
    self.assertEqual(interpret_text_input("\t   \n   \t\t    \t \t\n  "), "0")
    self.assertEqual(interpret_text_input(".025"), "0.025")
    self.assertEqual(interpret_text_input("12."), "12")

  ##
  # @brief Testing interpretation of add expressions
  #
  def test_solve_add_expressions(self):
    self.assertEqual(interpret_text_input("10 + 2"), "12")
    self.assertEqual(interpret_text_input("-10 + 2"), "-8")
    self.assertEqual(interpret_text_input("10 + -2"), "8")
    self.assertEqual(interpret_text_input("-10 + -2"), "-12")
    self.assertEqual(interpret_text_input("10.25 + 2"), "12.25")
    self.assertEqual(interpret_text_input("10 + -2.45"), "7.55")

  ##
  # @brief Testing interpretation of sub expressions
  #
  def test_solve_sub_epressions(self):
    self.assertEqual(interpret_text_input("10 - 2"), "8")
    self.assertEqual(interpret_text_input("-10 - 2"), "-12")
    self.assertEqual(interpret_text_input("10 - -2"), "12")
    self.assertEqual(interpret_text_input("-10 - -2"), "-8")
    self.assertEqual(interpret_text_input("10.25 - 2"), "8.25")
    self.assertEqual(interpret_text_input("10 - -2.45"), "12.45")

  ##
  # @brief Testing interpretation of mult expressions
  #
  def test_solve_mult_expressions(self):
    self.assertEqual(interpret_text_input("10 * 2"), "20")
    self.assertEqual(interpret_text_input("-10 * 2"), "-20")
    self.assertEqual(interpret_text_input("10 * -2"), "-20")
    self.assertEqual(interpret_text_input("-10 * -2"), "20")
    self.assertEqual(interpret_text_input("10.25 * 2"), "20.5")
    self.assertEqual(interpret_text_input("10 * -2.45"), "-24.5")

  ##
  # @brief Testing interpretation of div expressions
  #
  def test_solve_div_epressions(self):
    self.assertEqual(interpret_text_input("10 / 2"), "5")
    self.assertEqual(interpret_text_input("-10 / 2"), "-5")
    self.assertEqual(interpret_text_input("10 / -2"), "-5")
    self.assertEqual(interpret_text_input("-10 / -2"), "5")
    self.assertEqual(interpret_text_input("10.25 / 2"), "5.125")
    self.assertAlmostEqual(float(interpret_text_input("10 / -2.45")), float("-4.0816326530612244897959183673469"))

  ##
  # @brief Testing interpretation of power expressions
  #
  def test_solve_pow_expressions(self):
    self.assertEqual(interpret_text_input("10^2"), "100")
    self.assertEqual(interpret_text_input("-10^2"), "-100")
    self.assertEqual(interpret_text_input("10^-2"), "0.01")
    self.assertEqual(interpret_text_input("-10^-2"), "-0.01")
    self.assertEqual(interpret_text_input("10.25^-2"), "0.009518143961927425")
    self.assertEqual(interpret_text_input("-10^2.65"), "-446.683592150963")

  ##
  # @brief Testing interpretation of root expressions
  #
  def test_solve_root_expressions(self):
    self.assertEqual(interpret_text_input("2???4"), "2")
    self.assertEqual(interpret_text_input("2???0"), "0")
    self.assertEqual(interpret_text_input("(-2)???4"), "0.5")
    self.assertEqual(interpret_text_input("1???4.25"), "4.25")
    self.assertEqual(interpret_text_input("(-4)???8.48"), "0.5860046159133241")

  ##
  # @brief Testing interpretation of ln expressions
  #
  def test_solve_ln_expressions(self):
    self.assertEqual(interpret_text_input("ln 1"), "0")
    self.assertEqual(interpret_text_input("ln 2"), "0.6931471805599453")
    self.assertEqual(interpret_text_input("ln 0.3"), "-1.2039728043259361")

  ##
  # @brief Testing interpretation of factorial expressions
  #
  def test_solve_fact_expressions(self):
    self.assertEqual(interpret_text_input("fact 0"), "1")
    self.assertEqual(interpret_text_input("fact 1"), "1")
    self.assertEqual(interpret_text_input("fact 5"), "120")
    self.assertEqual(interpret_text_input("fact 20"), "2432902008176640000")

  ##
  # @brief Testing interpretation of abs expressions
  #
  def test_solve_abs_expressions(self):
    self.assertEqual(interpret_text_input("abs 0"), "0")
    self.assertEqual(interpret_text_input("abs 20"), "20")
    self.assertEqual(interpret_text_input("abs -20"), "20")
    self.assertEqual(interpret_text_input("abs -20.35"), "20.35")
    self.assertEqual(interpret_text_input("abs 20.35"), "20.35")

  ##
  # @brief Testing interpretation of more complex expressions
  #
  def test_complex_expressions(self):
    self.assertEqual(interpret_text_input("-e^255 / (2 * ln 3 - 8) + 16"), "95820210894447476699954462365897586339592546523970120325143657272553038596932333318376235909933899240886501392")
    self.assertEqual(interpret_text_input("abs -15 + 30 * fact 2 * 3"), "195")
    self.assertEqual(interpret_text_input("abs(-15 + 30) * fact 2 * 3"), "90")

  ##
  # @brief Testing interpretation of invalid expressions
  #
  def test_invalid_expressions(self):
    self.assertEqual(interpret_text_input("10.25 / 0"), "Error")

    self.assertEqual(interpret_text_input("2???-25.3"), "Error")
    self.assertEqual(interpret_text_input("0???4"), "Error")

    self.assertEqual(interpret_text_input("ln 0"), "Error")
    self.assertEqual(interpret_text_input("ln -15"), "Error")

    self.assertEqual(interpret_text_input("fact -5"), "Error")
    self.assertEqual(interpret_text_input("fact 1.256"), "Error")

  ##
  # @brief Testing interpretation of invalid inputs
  #
  def test_invalid_input(self):
    self.assertEqual(interpret_text_input("fwafwafwi f wf w fwaf wf wa+ wf+w 565f4w6a 6556465 wf*wf*wa "), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30 * fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) ** fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) */ fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) ^/ fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) + ln / fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + abs) + fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-fact + 5) + fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs -10 + 5) + fact 2 * 3"), "Error")


if __name__ == '__main__':
  try:
    unittest.main()
  except Exception as e:
    print(f"Compiling of test failed\n{e}")
