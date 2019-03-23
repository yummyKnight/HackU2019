class Machine:
    history = []  # dinamic array of logs
    state = false

    def __init__(self, id, type, speed, kremont):
        self.id = id
        self.type = type
        self.speed = speed * kremont
