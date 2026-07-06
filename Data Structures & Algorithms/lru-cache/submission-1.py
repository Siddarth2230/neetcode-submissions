class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insertAtStart(self, node):
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        node.prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertAtStart(self.cache[key])
            
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.insertAtStart(node)
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self.insertAtStart(node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.removeNode(lru)
            del self.cache[lru.key]

        
        
