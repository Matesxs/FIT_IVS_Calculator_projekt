from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput
from mathLib.entry_point import interpret_text_input
from mathLib.basics.math_functions import MathFunctions
import cProfile, pstats, io
from pstats import SortKey
import random
import sys

sys.setrecursionlimit(1_000_000)
random.seed()

def standart_deviation(input_string):
  return interpret_text_input(input_string)

def create_sum_string(numbers):
  total = "("
  for number in numbers:
    total += str(number) + "+"
  return total[:-1] + ")"

def get_numbers_testing(x):
  return [random.random() * 1000 for _ in range(x)]

if __name__ == '__main__':
  numbers = get_numbers_testing(1_000)
  n = len(numbers)
  input_string = f"(1 / ({n} - 1) * ({create_sum_string([MathFunctions.power_operation(float(number), 2) for number in numbers])} - {n} * ((1 / {n}) * {create_sum_string(numbers)})^2))√2"

  with PyCallGraph(output=GraphvizOutput(output_file='../profiling/profiling_output.png'), config=Config(groups=True)):
    standart_deviation(input_string)

  pr = cProfile.Profile()
  pr.enable()
  standart_deviation(input_string)
  pr.disable()

  s = io.StringIO()
  ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
  ps.print_stats()

  with open("../profiling/profile_log.txt", "w") as f:
    f.write(s.getvalue())