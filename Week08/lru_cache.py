import collections


class LRUCache(object):

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic: return -1

        val = self.dic.pop(key)
        self.dic[key] = val
        return val

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remian > 0:
                self.remian -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value