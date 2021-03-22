##
# @package entry_point
#

from .tokenizer import Tokenizer
from .prsr import Parser
from .interpreter import Interpreter
from .basics.number_class import Number

##
# @brief Entrypoint for UI
#
# @param test String input to interpret
#
def interpret_text_input(text:str):
  tokenizer = Tokenizer(text)

  try:
    tokens = tokenizer.parse_input_text()
  except:
    return "Error"

  if not tokens:
    return "0"

  # print(f"Debug Tokens: {tokens}")
  parser = Parser(tokens)
  try:
    node_tree = parser.parse()
  except:
    return "Error"

  if not node_tree:
    return "0"

  # print(f"Debug Nodes: {node_tree}")
  interpreter = Interpreter()
  try:
    value:Number = interpreter.interpret(node_tree)
  except:
    return "Error"

  return str(value)