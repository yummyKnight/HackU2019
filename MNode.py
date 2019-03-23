import Machine
def move():

class MNode:
    type_ = str()
    Machines = []
    k = int()

    def __init__(self, type_, array):
        self.type = type_
        self.arrayOfMachine = array

    def sort_machine(self):
        for x in self.arrayOfMachine:
            x.speed

    @staticmethod
    def sort(array):
        less = []
        equal = []
        greater = []
        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x.speed < pivot.speed:
                    less.append(x)
                elif x.speed == pivot.speed:
                    equal.append(x)
                elif x.speed > pivot.speed:
                    greater.append(x)
            # Don't forget to return something!
            return MNode.sort(greater) + equal + MNode.sort(less) # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array

    def simulate(self,orders):
        for i in self.Machines:
            if i.state==0:
                orders(self.k).iswork=1
                i.state=orders(self.k).amount
                self.k+=1
            else:
                i.state-=i.speed
                if i.state <=0:
                    orders(self.k).iswork=0
                    orders(self.k).state+=1
                    move(orders(self.k))
                    i.state=0
