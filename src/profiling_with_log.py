import threading
from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput
from mathLib.entry_point import interpret_text_input
from mathLib.basics.math_functions import MathFunctions
import cProfile, pstats, io
from pstats import SortKey
import random
import sys
import time

sys.setrecursionlimit(50_000_000)
threading.stack_size(0x8000000)

random.seed()

def standart_deviation(input_string):
  return interpret_text_input(input_string)

def create_sum_string(numbers):
  total = "("
  for number in numbers:
    total += str(number) + "+"
  return total[:-1] + ")"

def get_numbers_testing(x):
  return list(range(x))

def ecxecute():
  numbers = get_numbers_testing(100_000)
  n = len(numbers)
  input_string = f"2√(1 / ({n} - 1) * ({create_sum_string([MathFunctions.power_operation(float(number), 2) for number in numbers])} - {n} * ((1 / {n}) * {create_sum_string(numbers)})^2))"

  try:
    with PyCallGraph(output=GraphvizOutput(output_file='../profiling/profiling_output.png'), config=Config(groups=True)):
      standart_deviation(input_string)
  except Exception as e:
    print(f"Failed to create call graph\n{e}")

  pr = cProfile.Profile()
  pr.enable()
  standart_deviation(input_string)
  pr.disable()

  s = io.StringIO()
  ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CUMULATIVE)
  ps.print_stats()

  with open("../profiling/profile_log.txt", "w") as f:
    f.write(s.getvalue())

  stime = time.time()
  print(standart_deviation(input_string))
  print(f"Exec time: {time.time() - stime}ms")

if __name__ == '__main__':
  t = threading.Thread(target=ecxecute)
  t.start()
  t.join()