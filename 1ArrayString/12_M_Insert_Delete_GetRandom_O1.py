import random


class RandomizedSet(object):

    def __init__(self):
        self.my_set = set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.my_set:
            return False
        self.my_set.add(val)
        return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.my_set:
            return False
        self.my_set.remove(val)
        return True


    def getRandom(self):
        """
        :rtype: int
        """
        return list(self.my_set)[random.randint(0, len(self.my_set)-1)]


randomizedSet = RandomizedSet()
randomizedSet.insert(1)
randomizedSet.remove(2)
randomizedSet.insert(2)
randomizedSet.getRandom()
randomizedSet.remove(1)
randomizedSet.insert(2)
randomizedSet.getRandom()
