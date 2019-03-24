import Machine
import Order


def move(Order):
    if MNode.type_ == Order.nodeArray[Order.state]:
        for i in range(MNode.k, len(MNode.Order_arr)):
            if MNode.Order_arr[i - 1].number < Order.number < MNode.Order_arr[i].number:
                break
            MNode.Order_arr.insert(i, Order)


class MNode:
    type_ = str()
    k = 0
    def __init__(self, type_, array):
        self.Machines = []
        self.Order_arr = []
        self.type_ = type_
        for i in array:
            if i.type_ == self.type_:
                self.Machines.append(i)

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
            return MNode.sort(greater) + equal + MNode.sort(less)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array

    def simulate(self, orders):
        for i in self.Machines:
            if i.state == 0:
                orders(self.k).iswork = 1
                i.state = orders(self.k).amount
                self.k += 1
            else:
                i.state -= i.speed
                if i.state <= 0:
                    orders(self.k).iswork = 0
                    orders(self.k).state += 1
                    move(orders(self.k))
                    i.state = 0


def CreateKnots(machines):
    Mnodes = []
    Types = []
    """for x in machines:
        if !(x in(Mnodes.type_)):
            Mnode = MNode(x.type, machines)
            Mnodes.append(Mnode)
    return Mnodes"""
    for x in machines:
        if (x.type_ in Types) == False:
            Types.append(x.type_)
    for x in range(len(Types)):
        buf= MNode(Types[x], machines)
        Mnodes.append(buf)
    return Mnodes
