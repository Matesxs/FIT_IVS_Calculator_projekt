from mathLib.entry_point import interpret_text_input
from mathLib.basics.math_functions import MathFunctions
import random
import sys

# Rise recursion limit because we used them a lot so it doesnt break
sys.setrecursionlimit(1_000_000)
random.seed()

# Generate input string for math lib and execute calculation
def standart_deviation(numbers, n):
  input_string = f"2√(1 / ({n} - 1) * ({create_sum_string([MathFunctions.power_operation(float(number), 2) for number in numbers])} - {n} * ((1 / {n}) * {create_sum_string(numbers)})^2))"
  return interpret_text_input(input_string)

# Create string with sum of all numbers
def create_sum_string(numbers):
  total = "("
  for number in numbers:
    total += str(number) + "+"
  return total[:-1] + ")"

# Load user input, sanitize it and pass for formating for math lib
def profile():
  numbers = input("Input numbers for standart deviation: ")
  numbers = str(numbers).replace(" ", ";").replace("\t", ";").replace("\n", ";").replace("\r", "").replace(",", ".").split(";")
  print(standart_deviation(numbers, len(numbers)))

if __name__ == '__main__':
  profile()