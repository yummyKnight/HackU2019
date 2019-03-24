from Order import *
from math import sqrt
from MNode import *


class Claster:
    Order_arr = []

    def __init__(self, order_arr):
        self.Order_arr = order_arr
    # def push(self, Order):
    #     self.Order_arr.append = Order
    def mashtabir(self):

        av_array = sum([x.arrayLen for x in self.Order_arr])
        av_amount = sum([x.amount for x in self.Order_arr])
        av_dedline = sum([x.dedline for x in self.Order_arr])

        mu = (av_dedline + av_amount + av_array) / (3 * len(self.Order_arr))

        for i in range(0, len(self.Order_arr)):
            sig = ((self.Order_arr[i].dedline + self.Order_arr[i].amount + self.Order_arr[i].arrayLen) - mu) ** 2

        sig = sqrt(sig / (3 * len(self.Order_arr)))

        for i in range(0, len(self.Order_arr)):
            dedline = self.Order_arr[i].dedline
            amount = self.Order_arr[i].amount
            array = self.Order_arr[i].arrayLen

            self.Order_arr[i].dedline = (dedline - mu) / sig
            self.Order_arr[i].amount = (dedline - mu) / sig
            self.Order_arr[i].arrayLen = (dedline - mu) / sig

    def clasterization(self):  # индексы в orderNumber
        pass

    @staticmethod
    def sort_orders(orders, Mnodes):
        f = open('versual.txt', 'w')
        xg = 0
        for i in range(100):
            for j in range(100):  # MNodes = array of Node
                f.write(orders[i].nodeArray[orders[i].state - 1]+" =? "+Mnodes[j].type_)
                if orders[i].nodeArray[orders[i].state - 1] in Mnodes[j].type_:
                    xg+=1
                    print(str(i) + " " + str(j) + "  " + str(orders[i].amount))
                    f.write("  Видимо да")
                    buf = Order.Order(orders[i].amount, orders[i].deadline, orders[i].nodeArray)
                    Mnodes[j].Order_arr.append(buf)
                f.write("\n")
        print(xg)
        return Mnodes
        # for i in orders:
        #     for j in Mnodes:  # MNodes = array of Node
        #         f.write(i.nodeArray[i.state - 1]+" =? "+j.type_)
        #         if i.nodeArray[i.state - 1] in j.type_:
        #             f.write("  Видимо да")
        #             j.Order_arr.append(i)
        #         f.write("\n")

    @staticmethod
    def qck_sort(Order_arr):
        less = []
        equal = []
        greater = []
        if len(Order_arr) > 1:
            pivot = Order_arr[0].deadline
            for x in Order_arr:
                if x.deadline < pivot:
                    less.append(x)
                elif x.deadline == pivot:
                    equal.append(x)
                elif x.deadline > pivot:
                    greater.append(x)
            # Don't forget to return something!
            return Claster.qck_sort(greater) + equal + Claster.qck_sort(less)
            # Just use the + operator to join lists
            # Note that you want equal ^^^^^ not pivot
        else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
            return Order_arr

