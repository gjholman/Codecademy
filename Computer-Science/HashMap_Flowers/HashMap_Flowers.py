from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
    
  def hash(self, key):
    return sum(key.encode())
  
  def compress(self, hash_code):    
    return hash_code % self.array_size
  
  def assign(self, key, value):
    hash_key = self.hash(key)
    array_index = self.compress(hash_key)
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for item in list_at_array:
      if item[0] == key:
        item[1] = value
        return
    list_at_array.insert(payload)
    return
  
  def retrieve(self, key):
    hash_key = self.hash(key)
    retrieval_index = self.compress(hash_key)
    list_at_index = self.array[retrieval_index]
    for item in list_at_index:
      if item[0] == key:
        return item[1]
    return None

  
 
blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
  blossom.assign(element[0], element[1])
print(blossom.retrieve('rose'))