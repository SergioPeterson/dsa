
class BstNode:

    def __init__(self, key):
        self._key = key
        self._p = None
        self._left = None
        self._right = None

    # Priting out the object's key value
    def __repr__(self):
        return '%d' % self._key

    def __set__(self, key):
        self._key = key

# BstNode.py
