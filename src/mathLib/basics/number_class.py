##
# @package number_class
#

from dataclasses import dataclass

##
# @brief Number class
#
# Hold result of interpreter and correctly represent it when converted to string
#
@dataclass
class Number:
  value: float

  ##
  # @brief Check if value is float or int and return value according to it
  #
  # @return Int or float value
  #
  def get_value(self):
    int_val = int(self.value)
    return self.value if int_val != self.value else int_val

  def __repr__(self):
    return f"{self.get_value()}"