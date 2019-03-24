class Machine:
    history = []  # dinamic array of logs
    state = int()
    indexorder = -1
    type_ = str()
    id_ = str()

    def __init__(self, id_, type_, speed, kremont=0.99):
        self.id = id_
        self.type = type_
        self.speed = speed * kremont
