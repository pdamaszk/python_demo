class Wezel:

    def __init__(self, data):
        self.lewy = None
        self.prawy = None
        self.elem = data

# Insert method to create nodes
    def insert(self, data):

        if self.elem:
            if data < self.elem:
                if self.lewy is None:
                    self.lewy = Wezel(data)
                else:
                    self.lewy.insert(data)
            elif data > self.elem:
                if self.prawy is None:
                    self.prawy = Wezel(data)
                else:
                    self.prawy.insert(data)
        else:
            self.elem = data
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.elem:
            if self.lewy is None:
                return str(lkpval)+" Not Found"
            return self.lewy.findval(lkpval)
        elif lkpval > self.elem:
            if self.prawy is None:
                return str(lkpval)+" Not Found"
            return self.prawy.findval(lkpval)
        else:
            print(str(self.elem) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.lewy:
            self.lewy.PokazDrzewo()
        print(self.elem, end=' '),
        if self.prawy:
            self.prawy.PokazDrzewo()


root = Wezel(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
print()
print(root.findval(7))
print(root.findval(14))
