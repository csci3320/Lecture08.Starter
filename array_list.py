
class ArrayList():
  def __init__(self):
    self.array = [0] * 2
    self.next = 0

  def add(self, value):
    if self.next < len(self.array):
      self.array[self.next] = value
      self.next += 1
    else:
      temp_array = [0] * len(self.array) * 2
      for i in range(self.next):
        temp_array[i] = self.array[i]
      temp_array[self.next] = value
      self.next += 1
      self.array = temp_array

  def remove(self, value):
    for i in range(self.next):
      if self.array[i] == value:
        for j in range(i, self.next-1):
          self.array[j] = self.array[j+1]
        self.next -= 1
        return

  def contains(self, value):
    for i in range(self.next):
      if self.array[i] == value:
        return True
      
    return False

  def size(self):
    return self.next

  def asList(self):
    new_array = [0] * self.next
    for i in range(self.next):
      new_array[i] = self.array[i]
    return new_array
    pass

a = ArrayList()
a.add("Dinosaur")
a.add("Plant")
a.add("Whatever")
print(a.asList())
a.remove("Dinosaur")
print(a.asList())
