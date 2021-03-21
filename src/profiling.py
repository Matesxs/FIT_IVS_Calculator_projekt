from mathLib.entry_point import interpret_text_input
from mathLib.basics.math_functions import MathFunctions
import random
import sys

sys.setrecursionlimit(1_000_000)
random.seed()

def standart_deviation(numbers, n):
  input_string = f"(1 / ({n} - 1) * ({create_sum_string([MathFunctions.power_operation(float(number), 2) for number in numbers])} - {n} * ((1 / {n}) * {create_sum_string(numbers)})^2))√2"
  return interpret_text_input(input_string)

def create_sum_string(numbers):
  total = "("
  for number in numbers:
    total += str(number) + "+"
  return total[:-1] + ")"

def get_numbers_testing(x):
  return [random.random() * 1000 for _ in range(x)]

def profile():
  # numbers = get_numbers_testing(1_000)
  numbers = input("Input numbers for standart deviation: ")
  numbers = str(numbers).replace(" ", ";").replace("\t", ";").replace("\n", ";").replace("\r", "").replace(",", ".").split(";")
  print(standart_deviation(numbers, len(numbers)))

if __name__ == '__main__':
  profile()