import math

class MathFunctions:
  @staticmethod
  def add_operation(num1, num2):
    return num1 + num2

  @staticmethod
  def sub_operation(num1, num2):
    return num1 - num2

  @staticmethod
  def multiply_operation(num1, num2):
    return num1 * num2

  @staticmethod
  def divide_operation(num1, num2):
    if num2 == 0:
      raise RuntimeError("Can't divide by zero")
    return num1 / num2

  @staticmethod
  def power_operation(num1, num2):
    return num1 ** num2

  @staticmethod
  def root_operation(n, root):
    if root < 0:
      raise RuntimeError("Base value of root can't be less than zero")

    if n == 0:
      raise RuntimeError("N value of root can't be zero")

    return root ** (1 / n)

  @staticmethod
  def invert_operation(num):
    return -num

  @staticmethod
  def factorial_operation(num):
    int_num = int(num)

    if num < 0:
      raise RuntimeError("Factorial doesn't exist for negative numbers")
    elif int_num != num:
      raise RuntimeError("Can find factorial only for int")
    elif int_num == 0:
      return 1

    factorial = 1
    for i in range(1, int_num + 1):
      factorial *= i

    return factorial

  @staticmethod
  def natural_log_operation(num):
    if num <= 0:
      raise RuntimeError("Natural logarithm is defined only for x > 0")

    return math.log(num)
  
  @staticmethod
  def abs_operation(num):
    return abs(num)