
import trees.BinarySearchTreeNode as Node

class BinarySearchTree:

    def __init__(self):
        """
        Constructor responsible to initialize the BST structure
        """
        self._root = None

    def insert(self, key):
        """
        Inserts a new node into the BST

        Args:
            param1: The key to be inserted into the BST
        
        Raises:
            TypeError: key is not a valid integer
        """
        try:
            node = Node.BinarySearchTreeNode(key)  # a newborn node

            correctPosition = None
            i = self._root

            while i is not None:
                correctPosition = i
                if (node._key < i._key):
                    i = i._left
                else:
                    i = i._right

            node._p = correctPosition
            if correctPosition is None:
                self._root = node
            elif node._key < correctPosition._key:
                correctPosition._left = node
            else:
                correctPosition._right = node
        except TypeError:
            pass

    def inorder(self):
        """
        Return all the elements in inorder style
        """
        ret = []
        self._inorder(self._root, ret)
        return ret

    def _inorder(self, root, ret):
    
        if root is not None:
            self._inorder(root._left, ret)
            ret.append(root._key)
            self._inorder(root._right, ret)

    def search(self, key): 
        """
        Searchs for a key in the Bst
        
        Args:
            param1: The key to be searched inside the BST
        
        Raises:
            TypeError: key is not a valid integer    
        """
        try:
            root = self._root
            while root is not None and key != root._key:
                if key < root._key:
                    root = root._left
                else:
                    root = root._right
        
            if root is not None:
                return root
            return Node.BinarySearchTreeNode(None)
        except TypeError:
            pass

    def minimum(self):
        """
        Searchs for the minimum element in the BST 
        """
        root = self._root
        while root._left is not None:
            root = root._left

        return root

    def maximum(self):
        """
        Searchs for the maximum element in the BST 
        """
        root = self._root
        while root._right is not None:
            root = root._right

        return root

    def _minimum(self, root):

        while root._left is not None:
            root = root._left

        return root

    def _maximum(self, root):

        while root._right is not None:
            root = root._right

        return root

    def successor(self, key):
        """
        Returns the successor of the key

        Args:
            param1: The key used to get the sucessor
        
        Raises:
            TypeError: key is not a valid integer
        """
        try:
            node = self.search(key)

            if node is None:
                return None
            if node._right is not None:
                return self._minimum(node._right)

            i = node._p
            while i is not None and node._key == i._right._key:
                node = i
                i = i._p

            return i
        except TypeError:
            pass

    def predecessor(self, key):
        """
        Returns the predecessor of the key

        Args:
            param1: The key used to get the predecessor
        
        Raises:
            TypeError: key is not a valid integer
        """
        try:
            node = self.search(key)

            if node is None:
                return None
            if node._left is not None:
                return self._maximum(node._left)

            i = node._p
            while i is not None and node._key == i._left._key:
                node = i
                i = i._p

            return i
        except TypeError:
            pass

    def _transplant(self, n1, n2):

        if n1._p is None:
            self._root = n2
        elif n1 == n1._p._left:
            n1._p._left = n2
        else:
            n1._p._right = n2
        if n2 is not None:
            n2._p = n1._p

    def delete(self, key):
        """
        Deletes a node with the given key

        Args:
            param1: The key used to delete the node
        
        Raises:
            TypeError: key is not a valid integer
        """
        try:
            node = self.search(key)
            if node._key is None:
                return Node.BinarySearchTreeNode(None)
        
            # leaf case
            if node._left is None and node._right is None:
                if node._p._right is not None:
                    if node._p._right._key == node._key:
                        inode._p._right = None
                else:
                    node._p._left = None
            else:

                if node._left is None:
                    self._transplant(node, node._right)
                elif node._right is None:
                    self._transplant(node, node._left)
                else:
                    minimum = self._minimum(node._right)
            
                    if minimum._p._key != node._key:
                        self._transplant(minimum, minimum._right)
                        minimum._right = node._right
                        minimum._right._p = minimum

                    self._transplant(node, minimum)
                    minimum._left = node._left
                    minimum._left._p = minimum
        except TypeError:
            pass

# BinarySearchTree.py
