class Order:
    nodeArray = set()
    amount = int()
    deadline = int()
    state = int()

    def __init__(self, amount, deadline, state, nodeArray):
        self.amount = amount
        self.deadline = deadline
        self.state = state
        self.nodeArray = nodeArray
