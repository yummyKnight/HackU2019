class Order:
    nodeArray = set()
    amount = int()
    deadline = int()
    state = int()
    iswork = bool()
    arrayLen = int()
    number = int()

    def __init__(self, amount, deadline, nodeArray):
        self.amount = amount
        self.deadline = deadline
        self.nodeArray = nodeArray
        self.arrayLen = len(nodeArray)
