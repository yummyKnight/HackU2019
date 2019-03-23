import Order
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

    def clasterization(self): # индексы в orderNumber
        pass

    @staticmethod
    def qck_sort(Order_arr):
        less = []
        equal = []
        greater = []
        if len(Order_arr) > 1:
            pivot = Order_arr[0].dedlin + Order_arr[0].amount + Order_arr[0].arrayLen
            for x in Order_arr:
                if x.dedlin + x.amount + x.arrayLen < pivot:
                    less.append(x)
                elif x.speed == pivot:
                    equal.append(x)
                elif x.dedlin + x.amount + x.arrayLen > pivot:
                    greater.append(x)
            # Don't forget to return something!
            return Claster.clasterization(greater) + equal + Claster.clasterization(
                less)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
            return Order_arr

    def sort_orders(self):
        for i in self.Order_arr:
            for j in MNode: # MNode = array of Node
                if i.nodeArray[i.state] == j.type_:
                    j.Order_arr.append(i)
