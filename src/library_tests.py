import unittest
import math
import mathLib
from mathLib import Tokenizer, Token, TokenType, Parser, Interpreter, Number
from mathLib.basics.nodes import *
from mathLib.entry_point import interpret_text_input

class MathLibTestAdd(unittest.TestCase):
  def test_add_positive(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(0, 0), 0)
    self.assertEqual(mathLib.MathFunctions.add_operation(0, 5), 5)
    self.assertEqual(mathLib.MathFunctions.add_operation(2, 0), 2)
    self.assertEqual(mathLib.MathFunctions.add_operation(1, 3), 4)

  def test_add_negative(self):
    self.assertEqual(mathLib.MathFunctions.add_operation(-1, -2), -3)
    self.assertEqual(mathLib.MathFunctions.add_operation(-5, 0), -5)
    self.assertEqual(mathLib.MathFunctions.add_operation(0, -8), -8)
    self.assertEqual(mathLib.MathFunctions.add_operation(-20, -33), -53)

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

  def test_sub_mixed(self):
    self.assertEqual(mathLib.MathFunctions.sub_operation(-6, 2.4), -8.4)
    self.assertEqual(mathLib.MathFunctions.sub_operation(-1.2, 4), -5.2)
    self.assertEqual(mathLib.MathFunctions.sub_operation(2.4, -4.5), 6.9)


class MathLibTestMult(unittest.TestCase):
  def test_mult_positive(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(255, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(6, 3), 18)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, 10), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(11, 11), 121)

  def test_mult_negative(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-1, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, -5), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(0, -300), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-245, 0), 0)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-33, -45), 1485)

  def test_mult_mixed(self):
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-4.5, 4), -18)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(2.25, -16), -36)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(10, -3.3), -33)
    self.assertEqual(mathLib.MathFunctions.multiply_operation(-2, 4.8), -9.6)


class MathLibTestDiv(unittest.TestCase):
  def test_div_positive(self):
    self.assertEqual(mathLib.MathFunctions.divide_operation(0, 5), 0)
    self.assertEqual(mathLib.MathFunctions.divide_operation(20, 5), 4)
    self.assertEqual(mathLib.MathFunctions.divide_operation(6, 4), 1.5)
    self.assertEqual(mathLib.MathFunctions.divide_operation(2, 20), 0.1)
    self.assertEqual(mathLib.MathFunctions.divide_operation(500, 40), 12.5)

  def test_div_negative(self):
    self.assertEqual(mathLib.MathFunctions.divide_operation(-5, 5), -1)
    self.assertEqual(mathLib.MathFunctions.divide_operation(0, -5), 0)
    self.assertEqual(mathLib.MathFunctions.divide_operation(9, -3), -3)
    self.assertEqual(mathLib.MathFunctions.divide_operation(-36, -4), 9)
    self.assertEqual(mathLib.MathFunctions.divide_operation(3, -5), -0.6)
    
  def test_div_mixed(self):
    self.assertEqual(mathLib.MathFunctions.divide_operation(6.2, 4), 1.55)
    self.assertEqual(mathLib.MathFunctions.divide_operation(3, -6.5), -0.46153846153846153846153846153846)
    self.assertEqual(mathLib.MathFunctions.divide_operation(-5.5, -6.5), 0.84615384615384615384615384615385)

  def test_division_by_zero(self):
    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.divide_operation(3, 0)

class MathLibTestPow(unittest.TestCase):
  def test_pow_op_with_zero(self):
    self.assertEqual(mathLib.MathFunctions.power_operation(0, 0), 1)
    self.assertEqual(mathLib.MathFunctions.power_operation(0, 12), 0)
    self.assertEqual(mathLib.MathFunctions.power_operation(12, 0), 1)

  def test_pow_positive(self):
    self.assertEqual(mathLib.MathFunctions.power_operation(2, 2), 4)
    self.assertEqual(mathLib.MathFunctions.power_operation(2.4, 2), 5.76)
    self.assertEqual(mathLib.MathFunctions.power_operation(2.4, 4.52), 52.306397819793965)

  def test_pow_negative(self):
    self.assertEqual(mathLib.MathFunctions.power_operation(2, -2), 0.25)
    self.assertEqual(mathLib.MathFunctions.power_operation(-2, 2), 4)
    self.assertEqual(mathLib.MathFunctions.power_operation(-2, -2), 0.25)
    self.assertEqual(mathLib.MathFunctions.power_operation(-2.32, -3), -0.08008220919266884)
    
class MathLibTestRoot(unittest.TestCase):
  def test_root_positive(self):
    self.assertEqual(mathLib.MathFunctions.root_operation(8, 0), 0)
    self.assertEqual(mathLib.MathFunctions.root_operation(2, 4), 2)
    self.assertEqual(mathLib.MathFunctions.root_operation(8, 2.2), 1.1035774941665433)
    self.assertEqual(mathLib.MathFunctions.root_operation(4.8, 3.25), 1.2783281919978795)

  def test_root_negative(self):
    self.assertEqual(mathLib.MathFunctions.root_operation(-2, 4), 0.5)
    self.assertEqual(mathLib.MathFunctions.root_operation(-3.15, 3.45), 0.6749378431838611)

  def test_root_invalid_cases(self):
    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.root_operation(2, -5)

    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.root_operation(0, 2)
      
class MathLibTestLn(unittest.TestCase):
  def test_ln(self):
    self.assertEqual(mathLib.MathFunctions.natural_log_operation(1), 0)
    self.assertEqual(mathLib.MathFunctions.natural_log_operation(0.5), -0.6931471805599453)
    self.assertEqual(mathLib.MathFunctions.natural_log_operation(1.2), 0.1823215567939546)
    self.assertEqual(mathLib.MathFunctions.natural_log_operation(4), 1.3862943611198906)

  def test_ln_invalid_cases(self):
    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.natural_log_operation(0)

    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.natural_log_operation(-1)

    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.natural_log_operation(-2.25)

class MathLibTestFact(unittest.TestCase):
  def test_fact_positive_whole_numbers(self):
    self.assertEqual(mathLib.MathFunctions.factorial_operation(0), 1)
    self.assertEqual(mathLib.MathFunctions.factorial_operation(1), 1)
    self.assertEqual(mathLib.MathFunctions.factorial_operation(4), 24)

  def test_fact_invalid_cases(self):
    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.factorial_operation(3.35)

    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.factorial_operation(-5)

    with self.assertRaises(RuntimeError):
      mathLib.MathFunctions.factorial_operation(-4.2)

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
    self.assertEqual(Parser([Token(TokenType.NUMBER, 124.34)]).parse(), NumberNode(124.34))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 321)]).parse(), NumberNode(321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 0)]).parse(), NumberNode(0))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -321)]).parse(), NumberNode(-321))
    self.assertEqual(Parser([Token(TokenType.NUMBER, -51.3)]).parse(), NumberNode(-51.3))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "e")]).parse(), NumberNode(math.e))
    self.assertIsInstance(Parser([Token(TokenType.KEYWORD, "rand")]).parse(), NumberNode)

  def test_binary_operations(self):
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MINUS), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.MINUS), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.MULTIPLY), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.MULTIPLY), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.POW), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.POW), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.ROOT), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.ROOT), NumberNode(50)))
    self.assertEqual(Parser([Token(TokenType.NUMBER, 25), Token(TokenType.DIVIDE), Token(TokenType.NUMBER, 50)]).parse(), BinaryOperationNode(NumberNode(25), Token(TokenType.DIVIDE), NumberNode(50)))

  def test_unary_operations(self):
    self.assertEqual(Parser([Token(TokenType.PLUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.PLUS), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.MINUS), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.MINUS), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "abs"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "fact"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(11)))
    self.assertEqual(Parser([Token(TokenType.KEYWORD, "ln"), Token(TokenType.NUMBER, 11)]).parse(), UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(11)))

  def test_valid_parents(self):
    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)))

    self.assertEqual(Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.PLUS), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse(),
                     BinaryOperationNode(BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50)), Token(TokenType.PLUS), BinaryOperationNode(NumberNode(25), Token(TokenType.PLUS), NumberNode(50))))

  def test_invalid_parents(self):
    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN), Token(TokenType.RPAREN)]).parse()

    with self.assertRaises(SyntaxError):
      Parser([Token(TokenType.LPAREN), Token(TokenType.LPAREN), Token(TokenType.NUMBER, 25), Token(TokenType.PLUS), Token(TokenType.NUMBER, 50), Token(TokenType.RPAREN)]).parse()

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

class MathLibTestInterpreter(unittest.TestCase):
  def setUp(self) -> None:
    self.interpreter = Interpreter()

  def test_numbers(self):
    self.assertEqual(self.interpreter.interpret_node_tree(NumberNode(0)), Number(0))
    self.assertEqual(self.interpreter.interpret_node_tree(NumberNode(256)), Number(256))
    self.assertEqual(self.interpreter.interpret_node_tree(NumberNode(-128)), Number(-128))
    self.assertEqual(self.interpreter.interpret_node_tree(NumberNode(-12.65)), Number(-12.65))
    self.assertEqual(self.interpreter.interpret_node_tree(NumberNode(16.7)), Number(16.7))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(10.6))), Number(10.6))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(10.6))), Number(-10.6))
    
  def test_binary_operations(self):
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(3), Token(TokenType.PLUS), NumberNode(5))), Number(8))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.PLUS), NumberNode(2.25))), Number(8.5))

    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(3), Token(TokenType.MINUS), NumberNode(5))), Number(-2))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.MINUS), NumberNode(2.25))), Number(4))

    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(3), Token(TokenType.MULTIPLY), NumberNode(5))), Number(15))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.MULTIPLY), NumberNode(2.25))), Number(14.0625))

    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(3), Token(TokenType.DIVIDE), NumberNode(5))), Number(0.6))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.DIVIDE), NumberNode(2.25))), Number(2.7777777777777777777777777777778))

    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(3), Token(TokenType.POW), NumberNode(5))), Number(243))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.POW), NumberNode(2.25))), Number(61.763235550163658828103389539702))

    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(5), Token(TokenType.ROOT), NumberNode(3))), Number(1.2457309396155173259666803366403))
    self.assertEqual(self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(2.25), Token(TokenType.ROOT), NumberNode(6.25))), Number(2.2580026753417055949906722148876))

  def test_unary_operations(self):
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(0))), Number(0))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(0))), Number(0))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.PLUS), NumberNode(10.6))), Number(10.6))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.MINUS), NumberNode(10.6))), Number(-10.6))

    self.assertAlmostEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(5))).get_value(), Number(1.6094379124341003746007593332262).get_value())
    self.assertAlmostEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(1.1))).get_value(), Number(0.09531017980432486004395212328077).get_value())

    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(10.456))), Number(10.456))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "abs"), NumberNode(-10.456))), Number(10.456))

    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(5))), Number(120))
    self.assertEqual(self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(0))), Number(1))

  def test_invalid_cases(self):
    # Result is imaginary number that is not supported
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(2.25), Token(TokenType.ROOT), NumberNode(-6.25)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(0), Token(TokenType.ROOT), NumberNode(6.25)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(6.25), Token(TokenType.DIVIDE), NumberNode(0)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(0)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "ln"), NumberNode(-2.5)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(-2)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "fact"), NumberNode(3.35)))

  def test_invalid_operations(self):
    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(UnaryOperationNode(Token(TokenType.KEYWORD, "fasfafasfa"), NumberNode(3.35)))

    with self.assertRaises(RuntimeError):
      self.interpreter.interpret_node_tree(BinaryOperationNode(NumberNode(8), Token(TokenType.KEYWORD, "wtwtta"), NumberNode(3.35)))

class MathLibTestExpressions(unittest.TestCase):
  def test_special_zero_cases(self):
    self.assertEqual(interpret_text_input("00000000000000"), "0")
    self.assertEqual(interpret_text_input("0000000.000"), "0")
    self.assertEqual(interpret_text_input("             "), "0")
    self.assertEqual(interpret_text_input("\t   \n   \t\t    \t \t\n  "), "0")
    self.assertEqual(interpret_text_input(".025"), "0.025")
    self.assertEqual(interpret_text_input("12."), "12")

  def test_solve_add_expressions(self):
    self.assertEqual(interpret_text_input("10 + 2"), "12")
    self.assertEqual(interpret_text_input("-10 + 2"), "-8")
    self.assertEqual(interpret_text_input("10 + -2"), "8")
    self.assertEqual(interpret_text_input("-10 + -2"), "-12")
    self.assertEqual(interpret_text_input("10.25 + 2"), "12.25")
    self.assertEqual(interpret_text_input("10 + -2.45"), "7.55")

  def test_solve_sub_epressions(self):
    self.assertEqual(interpret_text_input("10 - 2"), "8")
    self.assertEqual(interpret_text_input("-10 - 2"), "-12")
    self.assertEqual(interpret_text_input("10 - -2"), "12")
    self.assertEqual(interpret_text_input("-10 - -2"), "-8")
    self.assertEqual(interpret_text_input("10.25 - 2"), "8.25")
    self.assertEqual(interpret_text_input("10 - -2.45"), "12.45")

  def test_solve_mult_expressions(self):
    self.assertEqual(interpret_text_input("10 * 2"), "20")
    self.assertEqual(interpret_text_input("-10 * 2"), "-20")
    self.assertEqual(interpret_text_input("10 * -2"), "-20")
    self.assertEqual(interpret_text_input("-10 * -2"), "20")
    self.assertEqual(interpret_text_input("10.25 * 2"), "20.5")
    self.assertEqual(interpret_text_input("10 * -2.45"), "-24.5")

  def test_solve_div_epressions(self):
    self.assertEqual(interpret_text_input("10 / 2"), "5")
    self.assertEqual(interpret_text_input("-10 / 2"), "-5")
    self.assertEqual(interpret_text_input("10 / -2"), "-5")
    self.assertEqual(interpret_text_input("-10 / -2"), "5")
    self.assertEqual(interpret_text_input("10.25 / 2"), "5.125")
    self.assertAlmostEqual(float(interpret_text_input("10 / -2.45")), float("-4.0816326530612244897959183673469"))

  def test_solve_pow_expressions(self):
    self.assertEqual(interpret_text_input("10^2"), "100")
    self.assertEqual(interpret_text_input("-10^2"), "-100")
    self.assertEqual(interpret_text_input("10^-2"), "0.01")
    self.assertEqual(interpret_text_input("-10^-2"), "-0.01")
    self.assertEqual(interpret_text_input("10.25^-2"), "0.009518143961927425")
    self.assertEqual(interpret_text_input("-10^2.65"), "-446.683592150963")

  def test_solve_root_expressions(self):
    self.assertEqual(interpret_text_input("2√4"), "2")
    self.assertEqual(interpret_text_input("2√0"), "0")
    self.assertEqual(interpret_text_input("(-2)√4"), "0.5")
    self.assertEqual(interpret_text_input("1√4.25"), "4.25")
    self.assertEqual(interpret_text_input("(-4)√8.48"), "0.5860046159133241")

  def test_solve_ln_expressions(self):
    self.assertEqual(interpret_text_input("ln 1"), "0")
    self.assertEqual(interpret_text_input("ln 2"), "0.6931471805599453")
    self.assertEqual(interpret_text_input("ln 0.3"), "-1.2039728043259361")

  def test_solve_fact_expressions(self):
    self.assertEqual(interpret_text_input("fact 0"), "1")
    self.assertEqual(interpret_text_input("fact 1"), "1")
    self.assertEqual(interpret_text_input("fact 5"), "120")
    self.assertEqual(interpret_text_input("fact 20"), "2432902008176640000")

  def test_solve_abs_expressions(self):
    self.assertEqual(interpret_text_input("abs 0"), "0")
    self.assertEqual(interpret_text_input("abs 20"), "20")
    self.assertEqual(interpret_text_input("abs -20"), "20")
    self.assertEqual(interpret_text_input("abs -20.35"), "20.35")
    self.assertEqual(interpret_text_input("abs 20.35"), "20.35")

  def test_complex_expressions(self):
    self.assertEqual(interpret_text_input("-e^255 / (2 * ln 3 - 8) + 16"), "95820210894447476699954462365897586339592546523970120325143657272553038596932333318376235909933899240886501392")
    self.assertEqual(interpret_text_input("abs -15 + 30 * fact 2 * 3"), "195")
    self.assertEqual(interpret_text_input("abs(-15 + 30) * fact 2 * 3"), "90")

  def test_invalid_expressions(self):
    self.assertEqual(interpret_text_input("10.25 / 0"), "Error")

    self.assertEqual(interpret_text_input("2√-25.3"), "Error")
    self.assertEqual(interpret_text_input("0√4"), "Error")

    self.assertEqual(interpret_text_input("ln 0"), "Error")
    self.assertEqual(interpret_text_input("ln -15"), "Error")

    self.assertEqual(interpret_text_input("fact -5"), "Error")
    self.assertEqual(interpret_text_input("fact 1.256"), "Error")

  def test_invalid_input(self):
    self.assertEqual(interpret_text_input("fwafwafwi f wf w fwaf wf wa+ wf+w 565f4w6a 6556465 wf*wf*wa "), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30 * fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) ** fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) */ fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) ^/ fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + 30) + ln / fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-15 + abs) + fact 2 * 3"), "Error")
    self.assertEqual(interpret_text_input("abs(-fact + 5) + fact 2 * 3"), "Error")

  def test_empty_input(self):
    self.assertEqual(interpret_text_input(""), "0")

if __name__ == '__main__':
  try:
    unittest.main()
  except Exception as e:
    print(f"Compiling of test failed\n{e}")
