"""
Programming assignment file for CSCI3320
The University of Nebraska at Omaha
"""
from multiprocessing.managers import listener_client


#
# The following clasess should not be edited in this assignment 
# (except including the manupulation of the self.tail pointer).
# Look below for the comment with "Start Assignment"
# to see the code that needs to be edited
#

class Node:
    """ A singly-linked node. """
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None





class SinglyLinkedList:
    # Do Not Add Any Changes to the SinglyLinkedList class
    def __init__ (self):
        self.head = None
        self.tail = None

    # Checks if the list is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
   
    def prepend(self, data): # Do not edit this function
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node    
            self.tail = node
        else:  
            node.next = self.head
            self.head = node        

    def append(self, data): # Do not edit this function
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node    
        else:   
            self.tail.next = node
            self.tail = node
            
    def delete_first_node (self): # Do not edit this function
        current = self.head  
        if self.head is None:
            print("No data element to delete")
            return None
        elif current == self.head:
            self.head = current.next
            return current.data    
          
    def delete_last_node (self): # Do not edit this function
        current = self.head 
        prev = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        while current:
            if current.next is None:
                prev.next = current.next 
                self.tail = prev
                return current.data
            prev = current
            current = current.next

def printInOrder(list):  # Do not edit this function
    """Start an in-order printing of node items for the given list"""
    # Recurse starting with the head node
    printNext(list.head)

def printNext(node):  # Do not edit this function
    """If the node is valid, print the given node and then continue to recurse"""
    # Stopping condition
    if node == None:
        return

    # Print to the console
    if node.next != None:
        print(str(node.data), " => ", end='')
    else:
        print(str(node.data))

    # Recursion     
    printNext(node.next)





#
# Start assignment
# The following methods and classes need to be updated for this assignment
#
def reverseList(list):  # Edit this function
    """Reverse the singly linked list *in place* using recursion."""
    # Recurse starting with the head node
    list.head = reverseRecursive(list.head)


def reverseRecursive(node):
    # Stopping condition
    if (node == None) or (node.next == None):
        return node

    # Recursion
    rest_of_list_reversed = reverseRecursive(node.next)

    node.next.next = node  # The 'next node's next' should point to the current node
    node.next = None  # Set the current node's next to None (since it will be the new tail)

    # Return the new head of the reversed list
    return rest_of_list_reversed




# Implement the following classes and methods using the singly linked list
class Queue:   # Edit this class
 
    def __init__(self): 
        self.list = SinglyLinkedList()   # A linked list to be used
        self.count = 0                   # the number of elements
 
    # Insert a new element into the queue 
    # i.e just insert a new element at the end of the linked list.
    def enqueue(self, data):
        self.list.append(data)
        self.count += 1

    # Remove the front element from the queue
    # i.e just delete and return an element 
    # at the beginning of the linked list
    # if the list is not empty
    def dequeue(self):
        if self.count == 0:
            print("Queue is empty, cannot dequeue.")
            return None

        data = self.list.delete_first_node()
        self.count -= 1
        return data
 
    # Returns the top element of the stack if the list is not empty
    def front(self):
        if self.count == 0:
            print("Queue is empty.")
            return None
        return self.list.head.data

    # Print all elements in the queue from the front element.
    def printQueue(self):
        current = self.list.head
        if current is None:
            print("Queue is empty.")
            return

        while current:
            if current.next != None:
                print(str(current.data), " => ", end='')
            else:
                print(str(current.data))
            current = current.next
        print()




# Implement the following classes and methods using the singly linked list
# as the base class. You will need to implement the doubly linked list
class DoublyLinkedList:      # Edit this class
    # implement a doubly linked list by refering 
    # the implementation of the SinglyLinkedList class
    def __init__ (self):
        self.head = None
        self.tail = None

    # Checks if the list is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
   
    def prepend(self, data): 
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def append(self, data): 
        # Encapsulate the data in a Node 
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def delete_first_node (self): 
        current = self.head  
        if self.head is None:
            print("No data element to delete")
            return None
        elif current == self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = current.next
                self.head.previous = None
            return current.data

    def delete_last_node (self): 
        current = self.head
        if self.head is None:
            print("No data element to delete")
            return None
        while current:
            if current.next is None:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = current.previous
                    self.tail.next = None
                return current.data
            current = current.next
    
    def print_list(self):  # Do not edit this function
        current = self.head
        while current:
            print(current.data, end=' <=> ' if current.next else '\n')
            current = current.next




# Implement the following classes and methods using the doubly linked list
class twoStacks:   # Edit this class
 
    def __init__(self):  # Do not edit this function
        self.list = DoublyLinkedList()   # A linked list to be used
        self.list.append(None)           # The seperator between Stack1 and Stack2 

    # Insert a new element into the stack1 
    # i.e just insert a new element at the beginning of the linked list.
    def push1(self, data):
        self.list.prepend(data)

    # Insert a new element into the stack2 
    # i.e just insert a new element at the end of the linked list.
    def push2(self, data):
        self.list.append(data)

    # Remove the top element from the stack1
    # if stack1 is not empty
    def pop1(self):
        if self.list.head == self.list.tail:
            print("Stack1 Underflow error")
            return None

        current = self.list.head
        if current.data is None:
            print("Stack1 Underflow error")
            return None

        return self.list.delete_first_node()

    # Remove the top element from the stack2
    # if stack2 is not empty
    def pop2(self):
        if self.list.head == self.list.tail:
            print("Stack2 Underflow error")
            return None

        current = self.list.tail
        if current.data is None:
            print("Stack2 Underflow error")
            return None

        return self.list.delete_last_node()

    # Returns the top element of the stack1 if stack1 is not empty
    def top1(self):
        if self.list.head == self.list.tail:
            print("Stack1 is empty")
            return None

        current = self.list.head
        if current.data is None:
            print("Stack1 is empty")
            return None

        return current.data
 
    # Returns the top element of the stack2 if the stack2 is not empty
    def top2(self):
        if self.list.head == self.list.tail:
            print("Stack2 is empty")
            return None

        current = self.list.tail
        if current.data is None:
            print("Stack2 is empty")
            return None

        return current.data




def menu():
    choice = 0
    while choice != 17:
        print("1) Construct a list L1 with a set of initial elements\n"
              "2) Reverse the list\n"
              "3) Print the list L1\n"
              "4) Construct a queue Q1 with a set of initial elements\n"
              "5) Print a front element of Q1\n"
              "6) Dequeue from the front of Q1\n"
              "7) Enqueue to the tail of Q1\n"
              "8) Print the queue Q1 from the first to the last element.\n"
              "9) Construct a twoStack T1 with a set of initial elements\n"
              "10) Print a top element of S1\n"
              "11) Pop from S1\n"
              "12) Push to S1 (to the front of twoStack)\n"
              "13) Print a top element of S2\n"
              "14) Pop from S2\n"
              "15) Push to S2 (to the end of twoStack)\n"
              "16) Print the twoStack T1 (print the head to the tail of the doubly linked list)\n"
              "17) Exit the program.\n")
        try:
            choice = int(input("Enter choice [1-17]: "))
            Choice(choice)
        except ValueError:
            print("Invalid input")

def Choice(choice):
    match choice:
        case 1:
            while True:
                try:
                    list_input = input("Enter initial elements: ")
                    list = [int(num) for num in list_input.split(',')]
                    break
                except ValueError:
                    print("Invalid input. Enter a set of numbers separated by commas.")
            for num in list:
                list_L1.append(num)
            print()
        case 2:
            reverseList(list_L1)
            print()
        case 3:
            printInOrder(list_L1)
            print()
        case 4:
            while True:
                try:
                    queue_input = input("Enter initial elements: ")
                    queue = [int(num) for num in queue_input.split(',')]
                    break
                except ValueError:
                    print("Invalid input. Enter a set of numbers separated by commas.")
            for num in queue:
                queue_Q1.enqueue(num)
            print()
        case 5:
            print(queue_Q1.front())
            print()
        case 6:
            print(queue_Q1.dequeue())
            print()
        case 7:
            while True:
                try:
                    element_input = int(input("Enter element: "))
                    queue_Q1.enqueue(element_input)
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
            print()
        case 8:
            queue_Q1.printQueue()
            print()
        case 9:
            while True:
                try:
                    s1_input = input("Enter initial elements for S1: ")
                    s1 = [int(num) for num in s1_input.split(',')]

                    s2_input = input("Enter initial elements for S2: ")
                    s2 = [int(num) for num in s2_input.split(',')]
                    break
                except ValueError:
                    print("Invalid input. Enter a set of numbers separated by commas.")
            for num in s1:
                twoStack_T1.push1(num)
            for num in s2:
                twoStack_T1.push2(num)
            print()
        case 10:
            print(twoStack_T1.top1())
            print()
        case 11:
            print(twoStack_T1.pop1())
            print()
        case 12:
            while True:
                try:
                    element_input = int(input("Enter element: "))
                    twoStack_T1.push1(element_input)
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
            print()
        case 13:
            print(twoStack_T1.top2())
            print()
        case 14:
            print(twoStack_T1.pop2())
            print()
        case 15:
            while True:
                try:
                    element_input = int(input("Enter element: "))
                    twoStack_T1.push2(element_input)
                    break
                except ValueError:
                    print("Invalid input. Enter a number.")
            print()
        case 16:
            twoStack_T1.list.print_list()
            print()
        case 17:
            print()
        case _:
            print("Invalid choice")




if __name__ == "__main__":            
# The following codes are given for 
# the example of the use of the singly linked list.
# You must modify the following codes to implement
# a menu driven user interface at the command line
    list_L1 = SinglyLinkedList()
    queue_Q1 = Queue()
    twoStack_T1 = twoStacks()
    menu()