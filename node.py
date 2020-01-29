import pygame

class Node:
    def __init__(self, val = None, nxt = None):
        self.val = val
        self.nxt = nxt

class SLL:
    def __init__(self, head = None):
        self.head = head

#Defining SLL functions

    def addToFront(self, node):
        if self.head == None:
            self.head = node
        node.nxt = self.head
        self.head = node
        return
    
    def dropFront(self):
        if self.head == None:
            #print("nothing to take out!")
            return
        # print("executing drop")
        self.head = self.head.nxt

    def append(self, node):
        if self.head == None:
            self.head = node
            return
        runner = self.head
        while runner.nxt != None:
            runner = runner.nxt
        if runner.nxt == None:
            runner.nxt = node
        return
    
    def dropBack(self):
        if self.head == None:
            #print("nothing to take!")
            return
        if self.head.nxt == None:
            self.head = None
            return
        runner = self.head
        while runner.nxt.nxt != None:
            runner = runner.nxt
        if runner.nxt.nxt == None:
            runner.nxt = None
        return
        
    def valCheck(self, val):
        runner = self.head
        if self.head == None:
            #print("nope")
            return
        while runner.val != val:
            if runner.nxt == None:
                
                break
            runner = runner.nxt
        if runner.val == val:
            #print("found")
            return(True)
        else:
            #print("not Found")
            return(False)

    def printSLL(self):
        if self.head == None:
            print("Nothing in this list!")
            return
        runner = self.head
        while runner.nxt != None:
            # print("Node Value is", runner.val)
            runner = runner.nxt
        # print("Last node value is", runner.val)
        pass
    
    def cleanNode(self, node):
        if node == None:
            print("Here's your problem!")
        newNode = Node(node.val)
        newNode.nxt = None
        return (newNode)

    def removeDupes(self):
        cleanSLL = SLL()
        node = self.cleanNode(self.head)
        cleanSLL.head = node
        runner = self.head
        while runner.nxt != None:
            #print(runner.val)
            if cleanSLL.valCheck(runner.val) == True:
                #print("Nah")
                runner = runner.nxt
            else:
                #print("yah")
                cleanSLL.append(self.cleanNode(runner))
        return cleanSLL
            
    #print("Catching")
        
######################TEST CODE#################################

# newList = SLL()
# newList.append(Node(1))
# newList.append(Node(1))
# newList.append(Node(1))
# newList.append(Node(3))
# newList.append(Node(3))
# newList.append(Node(3))
# newList.append(Node(4))
# newList.append(Node(4))
# newList.append(Node(4))

# newList.valCheck(3)
# newList.valCheck(10)

# #
# newList = newList.removeDupes()

# newX = SLL()
# newX.append(Node(1))

# newX.removeDupes()
# newX.printSLL()
# newList.printSLL()