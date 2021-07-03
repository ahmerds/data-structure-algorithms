class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

# binary Search Tree
class BST:
  def __init__(self):
    self.root = None

  def insert(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert(data, self.root)

  def _insert(self, data, curr_node):
    if data < curr_node.data:
      if curr_node.left is None:
        curr_node.left = Node(data)
      else:
        self._insert(data, curr_node.left)

    elif data > curr_node.data:
      if curr_node.right is None:
        curr_node.right = Node(data)
      else:
        self._insert(data, curr_node.right)

    else:
      print("Value is already present in tree")

  def find(self, data):
    if self.root:
      is_found = self._find(data, self.root)
      if is_found:
        return True
      return False
    else:
      return None

  def _find(self, data, curr_node):
    if data > curr_node.data and curr_node.right:
      return self._find(data, curr_node.right)
    elif data < curr_node.data and curr_node.left:
      return self._find(data, curr_node.left)

    if data == curr_node.data:
      return True

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(7))
