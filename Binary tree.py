class BinTreeNode:  # Binary Tree implementation using python
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinTree:
    def __init__(self):
        self.root=None
        
    def root(self):
        return self.root

    def add(self,val):
        if self.root==None:
            self.root=BinTreeNode(val)
        else:
            self._add(val,self.root)

    def _add(self,val,node):
        if val<node.data:
            if node.left==None:
                node.left=BinTreeNode(val)
            else:
                self._add(val,node.left)
        else:
            if node.right==None:
                node.right=BinTreeNode(val)
            else:
                self._add(val,node.right)
# binary tree traversal
    def preOrder(self,node):
        if node is not None:
            print node.data,
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self,node):
        if node is not None:
            self.inOrder(node.left)
            print node.data,
            self.inOrder(node.right)

    def postOrder(self,node):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print node.data,

    def count(self,node):
        if node==None:
            return 0
        else:
            return 1+self.count(node.left)+self.count(node.right)

    def maximum(self,node):
        if node is None :
            return None
        elif node.right is None :
            return node
        else :
            return self.maximum(node.right)                

t=BinTree()
t.add(50)
t.add(10)
t.add(15)
t.add(8)
print "Pre-Order Traversal"
t.preOrder(t.root)
print "\n"
print "In-Order Traversal"
t.inOrder(t.root)
print "\n"
print "Post-Order Traversal"
t.postOrder(t.root)
print "\n"
print "Count"
print t.count(t.root)
t.add(70)
t.add(60)
t.add(75)
t.add(30)
print "Pre-Order Traversal"
t.preOrder(t.root)
print "\n"
print "In-Order Traversal"
t.inOrder(t.root)
print "\n"
print "Post-Order Traversal"
t.postOrder(t.root)
print "\n"
print "Count"
print t.count(t.root)
print ""
print "Maximum"
print t.maximum(t.root).data
