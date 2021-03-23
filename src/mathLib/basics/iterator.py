##
# @package iterator
#

##
# @brief Class for iterating over list of data
#
class Iterator:
  ##
  # @brief Init input data and set index to start
  #
  def __init__(self, input_data):
    self.__input_data = input_data
    self.__index = 0

  ##
  # @brief Get current character and move index one forward
  #
  # @return Item from input data on current index
  #
  def next(self):
    try:
      result = self.__input_data[self.__index]
      self.__index += 1
    except Exception:
      raise Exception("OOI")
    return result