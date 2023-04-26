"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. 
If it cannot be locked, then it should return false. 
Otherwise, it should lock it and return true.
unlock, which unlocks the node. 
If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. 
You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. 
Each method should run in O(h), where h is the height of the tree.

"""







class TreeNode:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.is_locked = False
        self.locked_descendants_count = 0

    def _can_lock_or_unlock(self):
        if self.locked_descendants_count > 0:
            return False
        curr = self.parent
        while curr:
            if curr.is_locked:
                return False
            curr = curr.parent
        return True

    def is_locked(self):
        return self.is_locked

    def lock(self):
        if self._can_lock_or_unlock():
            self.is_locked = True
            curr = self.parent
            while curr:
                curr.locked_descendants_count += 1
                curr = curr.parent
            return True
        else:
            return False

    def unlock(self):
        if self._can_lock_or_unlock():
            self.is_locked = False
            curr = self.parent
            while curr:
                curr.locked_descendants_count -= 1
                curr = curr.parent
            return True
        else:
            return False
