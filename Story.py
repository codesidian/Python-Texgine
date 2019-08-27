class Story():
    def __init__(self, name,startroom,description):
        self.name = name
        self.startroom = startroom
        self.description = description
        self.rooms = []
        self.items = []
        self.interactables = []
        
    def addRoom(self,room):
        self.rooms.append(room)
    
    def addItem(self,item):
        self.items.append(item)
        
    def addInteractable(self,interactable):
        self.items.append(interactable)

    def getRooms(self):
        return self.rooms
    
    def getItems(self):
        return self.items
    
    def getInteractables(self):
        return self.getInteractables
    
    def __str__(self):
        return '{self.name} - {self.description}'.format(self=self)