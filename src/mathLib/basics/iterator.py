class Iterator:
  def __init__(self, input_data):
    self.input_data = input_data
    self.index = 0

  def next(self):
    try:
      result = self.input_data[self.index]
      self.index += 1
    except Exception:
      raise Exception("OOI")
    return result