from dataclasses import dataclass

@dataclass
class Number:
  value: float

  def get_value(self):
    int_val = int(self.value)
    return self.value if int_val != self.value else int_val

  def __repr__(self):
    return f"{self.get_value()}"