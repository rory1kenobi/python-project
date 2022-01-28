class Sight:
    def __init__(self, sight_name, country, description, visited=False, id=None):
        self.sight_name= sight_name
        self.country = country
        self.description = description
        self.visited = visited
        self.id = id

    def mark_visted(self):
        self.visited = True