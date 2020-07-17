"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head:
            self.head.prev = ListNode(value,None,self.head)
            self.head = self.head.prev   
        else:
            self.head = ListNode(value)
            self.tail = self.head
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head:
            value = self.head.value
            self.delete(self.head)
            return value
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.tail:
            self.tail.next = ListNode(value,self.tail,None)
            self.tail = self.tail.next
        else:
            self.tail = ListNode(value)
            self.head = self.tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail:
            value = self.tail.value
            self.delete(self.tail)
            return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        node_val = node.value
        self.delete(node)
        self.add_to_head(node_val)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        node_val = node.value
        self.delete(node)
        self.add_to_tail(node_val)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        self.length -=1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
        elif self.tail == node:
            self.tail = node.prev
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        maxval = self.head.value
        curr = self.head
        while curr.next:
            if curr.next.value > maxval:
                maxval = curr.next.value
            curr = curr.next
        return maxval

############################################################

class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node

    Methods/Behavior/Operations:
    1. Get value
    2. Set value
    3. Get next
    4. Set next
    """
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    """
    Data:
    1. A reference to the head Node
    2. A reference to the tail Node

    Behavior/Methods:
    1. Add To Tail
    2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
    3. Remove Head
    4. Remove Tail
    5. Contains?
    6. Get Maximum?
    """
    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value, None)
        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # if the list is initially empty, set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the tail
        else:
            # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
            # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # return the value
            return head.get_value()
        # otherwise we have more than one element in our list
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        return value

    def contains(self, value):
        if not self.head:
            return False

        # Recursive solution
        # def search(node):
        #   if node.get_value() == value:
        #     return True
        #   if not node.get_next():
        #     return False
        #   return search(node.get_next())
        # return search(self.head)
    
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value



class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size 

    def push(self, value):
        self.size  += 1
        return self.storage.add_to_tail(value)


    def pop(self):
        if self.size >  0:
            self.size  -= 1
            return self.storage.remove_tail()
            
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -=1
            return self.storage.remove_head()

# class CircularQueue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.add_to_tail(value)

#     def dequeue(self):
#         if self.size > 0:
#             self.size -=1
#             return self.storage.remove_head()


############################################################

class RingBuffer:
    def __init__(self, capacity):
        # Maximum size of the Ring Buffer
        self.capacity = capacity
        # A queue storing the items
        self.storage = DoublyLinkedList()

    def append(self, item):
        # enqueue an item to the queue
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            # max_value = self.storage.get_max()
            _ = self.storage.remove_from_head()
            self.storage.add_to_head(item)

    def get(self):
        result = []
        while len(self.storage) > 0:
            result.append(self.storage.remove_from_head())
        return result

    def get_max(self):
        return self.storage.get_max()

#############################################################

# class RingBuffer:
#     def __init__(self, capacity):
#         # Maximum size of the Ring Buffer
#         self.capacity = capacity
#         # A queue storing the items
#         self.storage = Queue()

#     def append(self, item):
#         # enqueue an item to the queue
#         if len(self.storage) < self.capacity:
#             self.storage.enqueue(item)
#         else:
#             _ = self.storage.dequeue()
#             self.storage.enqueue(item)

#     def get(self):
#         result = []
#         while len(self.storage) > 0:
#             result.append(self.storage.dequeue())
#         return result

if __name__ == "__main__":
    rb = RingBuffer(5)
    rb.append('a')
    rb.append('b')
    rb.append('c')
    print(rb.get_max())
