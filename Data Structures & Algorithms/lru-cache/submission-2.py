# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.cap = capacity
#         ##print (self.cache)
        

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
        

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value

#         if len(self.cache)>self.cap:
#             self.cache.popitem(last=False)

class Node:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity) -> None:
        self.cache = dict()
        self.capacity = capacity
        self.right, self.left  = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    def insert(self,node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node
    
    def get(self, key) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        
        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]





        


































        
