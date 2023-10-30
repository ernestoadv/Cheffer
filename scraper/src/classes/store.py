import json

class Store:
    id: str
    name: str

    def __init__(self, id, name):
        self.id = id
        self.name = name.value
                
    def __json__(self):
        return json.dumps(self, default=lambda x: x.__dict__)

    def __str__(self):
        string = "> Store:\n\n"
        string += "* ID: " + self.id + "\n"
        string += "* Name: " + self.name + "\n"
        return string