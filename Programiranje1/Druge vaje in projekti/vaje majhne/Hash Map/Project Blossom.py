from linked_list import Node, LinkedList
from blossom import flower_definitions 

class Flowers:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
      return sum(key.encode())
    
  def compress(self, hash_code):
      return hash_code % self.array_size

  def assign(self, key, value):
      
      array_index = self.compress(self.hash(key))
      payload = Node([key, value])
      list_at_array = self.array[array_index]

      for item in list_at_array:

        if key == item[0]:
          item[0] = value

      list_at_array.insert(payload)

  def retrieve(self, key):
      index = self.compress(self.hash(key))
      list_at_index = self.array[index]

      for i in list_at_index:

        if key == i[0]:
          return i[1]
        
      return None

#TESTING:
blossom = Flowers(len(flower_definitions))
for f in flower_definitions:
  blossom.assign(f[0], f[1])
print(blossom.retrieve('daisy'))