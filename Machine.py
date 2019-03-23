class Machine:
    history = []  # dinamic array of logs
    state = 0

    def __init__(self, id, type, speed, kremont):
        self.id = id
        self.type = type
        self.speed = speed * kremont
