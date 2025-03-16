class Elem:

    def __init__(self, v, next=None):
        self.val = v
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def __repr__(self):
        
        if self.head is None:
            return ''
        
        p = self.head

        string = 'HEAD'
        while p is not None:
            string += f" --->  {p.val}"
            p = p.next
        string += f" ---> {p}"
        
        return string

    def printAll(self):

        ''''
        Print the linked list elements in order
        '''

        if self.head is None:
            return
        
        p = self.head

        print("HEAD ", end=""),
        while p is not None:
            print(" ---> ", p.val, end="")
            p = p.next
        print(" ---> ", p)

        return

    def printReverse(self):

        '''
        Reverses the order of the linked list and then prints the values.
        '''
        
        if self.head is None:
            return
        
        p = self.head
        pp = None

        while p is not None:
            pNext = p.next
            p.next = pp
            pp = p
            p = pNext

        self.head = pp

        self.printAll()

        return
    

    def printRec(self):

        '''
        Prints the values in the linked list in reverse order using recursion.
        '''
        
        print("HEAD ", end=""),

        def _printRek(head):
            if head is None:
                return
            _printRek(head.next)
            print(" ---> ", head.val, end="")

        _printRek(self.head)
        print(" ---> ", None)

        return

    def insertFirst(self, v):
        '''
        Inserts a new element at the beginning of the list.

        The HEAD is set to the new element, and the new element points to the previous HEAD.
        '''
        self.head = Elem(v, self.head) 

    def delMax(self):
        '''
        Removes the maximum element from the list and returns it.
        '''
        if self.head is None:
            return 
        
        pMax = self.head # maximum pointer
        ppMax = None # maximum previous pointer

        p = self.head.next # pointer
        pp = self.head # previous pointer

        while p != None:

            if p.val > pMax.val:
                pMax = p
                ppMax = pp

            pp = p
            p = p.next
            
        if ppMax is None:
            # The first value is the maximum one.
            return self.delFirst()
        else:
            ppMax.next = pMax.next
        pMax.next = None
        return pMax
        

    def delFirst(self):
        '''
        Removes the first element from the list and returns it.
        '''
        if self.head is None:
            return
        p = self.head
        self.head = self.head.next
        p.next=None
        return p
    
    def search(self, v):
        '''
        Searches for a value and returns it, or returns None if it is not found.
        '''
        p = self.head
        
        while p != None or p.val != v:
            p = p.next
        return p
    