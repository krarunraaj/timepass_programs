class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self , new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print()    



if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()
    llist.insertAtBeginning(5)
    llist.insertAtBeginning(50)
    llist.printList()
           
