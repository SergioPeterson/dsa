
#
# Copyright (c) 2016 Luis Alves
#

import BstNode as Node


class Bst:

    def __init__(self):
        self._root = None

    def insert(self, key):

        if key is None:
            raise AttributeError('key value: None')
        node = Node.BstNode(key)  # a newborn node

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

    def inorder(self):
        ret = []
        self._inorder(self._root, ret)
        return ret

    def _inorder(self, root, ret):
        
        if root is not None:
            self._inorder(root._left, ret)
            ret.append(root._key)
            self._inorder(root._right, ret)

    def search(self, key):

        while self._root is not None and key != self._root._key:
            if key < self._root._key:
                self._root = self._root._left
            else:
                self._root = self._root._right

        return self._root._key

    def rsearch(self, key):
        return self._rsearch(self._root, key)

    def _rsearch(self, root, key):

        if root is None or key == root._key:
            return root

        if key < root._key:
            return self._rsearch(root._left, key)
        else:
            return self._rsearch(root._right, key)

    def minimum(self):

        root = self._root
        while root._left is not None:
            root = root._left

        return root

    def maximum(self):

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

        node = self._rsearch(self._root, key)

        if node is None:
            raise AttributeError('key: Not found')
        if node._right is not None:
            return self._minimum(node._right)

        i = node._p
        while i is not None and node._key == i._right._key:
            node = i
            i = i._p

        return i

    def predecessor(self, key):

        node = self._rsearch(self._root, key)

        if node is None:
            raise AttributeError('key: Not found')
        if node._left is not None:
            return self._maximum(node._left)

        i = node._p
        while i is not None and node._key == i._left._key:
            node = i
            i = i._p

        return i

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

        node = self.search(self._root, key)
        if node is None:
            raise AttributeError('key: Not found')

        if node._left is None:
            self._transplant(node, node._right)
        elif node._right is None:
            self._transplant(node, node._left)
        else:
            minimum = self.minimum(node._right)

            if minimum._p._key != node._key:
                self._transplant(minimum, minimum._right)
                minimum._right = node._right
                minimum._right._p = minimum

            self._transplant(node, minimum)
            minimum._left = node._left
            minimum._left._p = minimum

# Bst.py
