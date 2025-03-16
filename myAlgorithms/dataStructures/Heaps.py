import math
from linkedList import LinkedList, Elem

class heap:

    def __init__(self):
        self.A = [None] # index 0 is reserved for sentinel 
        self.hl = len(self.A)

    def __repr__(self):
        return str(self.A)

    def downHeap(self, i):
        if i < 1:
            raise ValueError('False value')

        while True:
            if 2*i > self.hl:
                break
            
            k = 2*i
            
            if self.hl >= 2*i+1 and self.A[2*i+1] > self.A[2*i]:
                k = 2*i+1
            
            if self.A[k] < self.A[i]:
                break
            
            self.A[i] , self.A[k] = self.A[k] , self.A[i]
            i = k
    
    def upHeap(self, i):

        while True:
            if i//2 < 1:
                break

            k = i//2

            if self.A[i] < self.A[k]:
                break
            
            self.A[i] , self.A[k] = self.A[k] , self.A[i]
            i = k
        

class Heaps:
    
    def __init__(self):
        self.root = None

    def DelMax(self):

        if self.root is None:
            return 

        p1 = self.root.left
        p2 = self.root.right

        elemMax = self.root.val
        self.root = p1

        self.Union(p2)

        return elemMax
    
    def heapToList(self):

        head = LinkedList()

        while self.root is not None:

            elemMax = self.DelMax()
            
            head.insertFirst(elemMax)
        return head
    
    def printHeap(self):

        def printHeap_(node, level=0, prefix="Root: "):

            print(" " * (level * 4) + prefix + str(node.val))

            if node.left is not None:
                printHeap_(node.left,level + 1, "L--> ")
            else:
                print(" " * ((level + 1) * 4) + "L--> None")

            if node.right is not None:
                printHeap_(node.right, level + 1, "R--> ")
            else:
                print(" " * ((level + 1) * 4) + "R--> None")
        root = self.root
        printHeap_(root)
        return


class nodeLeftistHeap:   
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.npl = 0

class leftistHeap(Heaps):
    def __init__(self):
        super().__init__()

    def setNPL(self):

        def _setnpl(_root):

            if _root is None:
                return -1
            
            npl_left = _setnpl(_root.left)
            npl_right = _setnpl(_root.right)

            npl = min(npl_left, npl_right) + 1

            _root.npl = npl

            return npl
        
        _setnpl(self.root)
    
    def findMaxNpl(self):

        def _findMaxNpl(root):
            if root is None: 
                return -1, root
            
            maxLeftNpl, maxLeftElem = _findMaxNpl(root.left)
            maxRightNpl, maxRightElem = _findMaxNpl(root.right)

            maxNpl = max(maxLeftNpl, maxRightNpl, root.npl)

            if maxNpl == maxRightNpl:
                return maxNpl, maxRightElem
            
            elif maxNpl == maxLeftNpl:
                return maxNpl, maxLeftElem
            
            else:
                return maxNpl, root

        return _findMaxNpl(self.root)
    

    def Union(self, heap):

        def _Union(p1,p2):
            if p1 is None:
                return p2
            if p2 is None:
                return p1
            if p2.val > p1.val:
                p2, p1 = p1, p2
            
            p1.right = _Union(p1.right, p2)

            # swap

            leftNpl = -1 if p1.left is None else p1.left.npl
            rightNpl = -1 if p1.right is None else p1.right.npl

            if leftNpl < rightNpl:
                p1.left, p1.right = p1.right, p1.left

            # set new npl

            p1.npl = min(leftNpl, rightNpl)

            return p1

        self.root = _Union(self.root, heap)
        return 

    def Insert(self, val):

        newNode = nodeLeftistHeap(val = val)

        if self.root is None:
            self.root = newNode
        else:
            self.Union(newNode)

        return 
    


        



class nodeSkewHeap:   
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class skewHeap(Heaps): 

    def __init__(self):
        super().__init__()

    
    def Union(self, Heap_):
        def Union_(p1,p2):
            if p1 is None:
                return p2
            if p2 is None:
                return p1
            if p1.val < p2.val:
                p1,p2 = p2,p1
            p = Union_(p1.right, p2)
            p1.left, p1.right = p, p1.left

            return p1
         
        self.root = Union_(self.root, Heap_)

    def Insert(self, val):

        newNode = nodeSkewHeap(val = val)

        if self.root is None:
            self.root = newNode
        else:
            self.Union(newNode)

        return 
            

