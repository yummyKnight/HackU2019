import Order
import math


class Claster:
    Order_arr = []

    def __init__(self):
        pass

    def push(self, Order):
        self.Order_arr.append = Order

    def mashtabir(self, av_dedline, av_amount, av_array):

        mu = (av_dedline + av_amount + av_array) / (3 * len(Order_arr))

        for i in range(0, len(Order_arr)):
            sig = ((Order_arr[i].dedline + Order_arr[i].amount + Order_arr[i].arrayLen) - mu) ** 2

        sig = sqrt(sig / (3 * len(Order_arr)))

        for i in range(0, len(Order_arr)):
            dedline = Order_arr[i].dedline
            amount = Order_arr[i].amount
            array = Order_arr[i].arrayLen

            Order_arr[i].dedline = (dedline - mu) / sig
            Order_arr[i].amount = (dedline - mu) / sig
            Order_arr[i].arrayLen = (dedline - mu) / sig

    def clasterization(self):
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
            return Claster.clasterization(greater) + equal + Claster.clasterization(less)  # Just use the + operator to join lists
        # Note that you want equal ^^^^^ not pivot
        else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
            return array
