##
# @package math_functions
#

import math

##
# @brief Class for holding all math functions
#
class MathFunctions:
  ##
  # @brief Add method
  #
  # Add two numbers together
  #
  # @param num1 Float or int
  # @param num2 Float or int
  # @return Added values of these two numbers
  #
  @staticmethod
  def add_operation(num1, num2):
    return num1 + num2

  ##
  # @brief Subtract method
  #
  # Subtract second number from first
  #
  # @param num1 Float or int
  # @param num2 Float or int
  # @return Result from subtracting num2 from num1
  #
  @staticmethod
  def sub_operation(num1, num2):
    return num1 - num2

  ##
  # @brief Multiply method
  #
  # Multiply first and second numbers
  #
  # @param num1 Float or int
  # @param num2 Float or int
  # @return Result from subtracting num2 from num1
  #
  @staticmethod
  def multiply_operation(num1, num2):
    return num1 * num2

  ##
  # @brief Divide method
  #
  # Divide first number by second \n
  # @warning
  # num2 can't be zero!
  #
  # @param num1 Float or int
  # @param num2 Float or int
  # @return Result from division num1 by num2
  #
  @staticmethod
  def divide_operation(num1, num2):
    if num2 == 0:
      raise RuntimeError("Can't divide by zero")
    return num1 / num2

  ##
  # @brief Power method
  #
  # Power first number by second
  #
  # @param num1 Float or int
  # @param num2 Float or int
  # @return Result from powering num1 by num2
  #
  @staticmethod
  def power_operation(num1, num2):
    return num1 ** num2

  ##
  # @brief Root method
  #
  # Make n root of value \n
  # @warning
  # value can't be less than zero! \n
  # @warning
  # n can't be zero!
  #
  # @param n Float or int
  # @param value Float or int
  # @return Result from n root of value
  #
  @staticmethod
  def root_operation(n, value):
    if value < 0:
      raise RuntimeError("Base value of root can't be less than zero")

    if n == 0:
      raise RuntimeError("N value of root can't be zero")

    return value ** (1 / n)

  ##
  # @brief Invert method
  #
  # Invert number
  #
  # @param num Float or int
  # @return Inverted value of num
  #
  @staticmethod
  def invert_operation(num):
    return -num

  ##
  # @brief Factorial method
  #
  # @warning
  # num must be natural number!
  #
  # @param num Int
  # @return Factorial of num
  #
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

  ##
  # @brief Natural logarithm method
  #
  # @warning
  # num must be larger or equal zero!
  #
  # @param num Float or int
  # @return Natural logarithm of num
  #
  @staticmethod
  def natural_log_operation(num):
    if num <= 0:
      raise RuntimeError("Natural logarithm is defined only for x > 0")

    return math.log(num)

  ##
  # @brief Absolute value method
  #
  # @param num Float or int
  # @return Absolute value of num
  #
  @staticmethod
  def abs_operation(num):
    return abs(num)