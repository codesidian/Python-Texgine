class Room():
    def __init__(self, name,description,art,interactables):
        self.name = name
        self.description = description
        self.art = art
        self.interactables = interactables

    def getRooms(self):
        return self.rooms
    
    def getItems(self):
        return self.items
    
    def __str__(self):
        return '{self.name} - {self.description}'.format(self=self)