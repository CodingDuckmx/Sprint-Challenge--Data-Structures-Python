class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        prev = None
        curr = self.head          

        while curr:
            next_node = curr.get_next()
            curr.set_next(prev)

            prev = curr
            curr = next_node

            if next_node:
                next_node = next_node.get_next()
        
        self.head = prev


if __name__ == "__main__":
    
    ll = LinkedList()
    ll.add_to_head(1)
    ll.add_to_head(2)
    ll.add_to_head(3)
    print(ll.head.value)
    ll.reverse_list(ll.head,None)
    print(ll.head.value)
            
