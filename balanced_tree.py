class Node:
  def __init__(self,value):
    self.val = value
    self.left = None
    self.right = None
    self.height = 0

def getHeight(root):
  if root is None:
    return 0
  return root.height         

def getBalance(root):
  return getHeight(root.left)- getHeight(root.right)

def rightRotate(root):
  left = root.left
  rightOfLeft = left.right
  
  left.right = root
  root.left = rightOfLeft
  
  root.height = 1+ max(getHeight(root.left),getHeight(root.right))
  left.height = 1+ max(getHeight(left.left),getHeight(left.right))
  return left

def leftRotate(root):
  right = root.right
  leftOfRight = right.left
  
  right.left = root
  root.right = leftOfRight
  
  root.height = 1+ max(getHeight(root.left),getHeight(root.right))
  right.height = 1+ max(getHeight(right.left),getHeight(right.right))
  return right

def avl(root,value):
  if root is None:
    return Node(value)
  
  if root.val > value:
    root.left = avl(root.left,value)
  elif root.val < value:
    root.right = avl(root.right,value)
  else:
    return root
  
  root.height = 1 + max(getHeight(root.left),getHeight(root.right))
  
  balance = getBalance(root)
  
  if balance > 1 and value < root.left.val:
    root = rightRotate(root)
    
  elif balance < -1 and value > root.right.val:
    root = leftRotate(root)
  elif balance < -1 and value < root.right.val:
    root.right = rightRotate(root.right)
    root = leftRotate(root)
  elif balance > 1 and value > root.left.val:
    root.left = leftRotate(root.left)
    root = rightRotate(root)
  return root

root = Node(7)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(9)
root.right.right = Node(15)

def dfs(root):
  if root is None: 
    return None
  print(root.val,end="->")
  dfs(root.left)
  dfs(root.right)

root = avl(root,12)
dfs(root)