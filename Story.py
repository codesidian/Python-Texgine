class Story():
    def __init__(self, name,startroom,description):
        self.name = name
        self.startroom = startroom
        self.description = description
        self.rooms = []
        self.items = []
        self.interactables = []
        self.effects = []
        
    def addRoom(self,room):
        self.rooms.append(room)
    
    def addItem(self,item):
        self.items.append(item)
        
    def addInteractable(self,interactable):
        self.interactables.append(interactable)
    
    def addEffect(self,effect):
        self.effects.append(effect)

    def getRooms(self):
        return self.rooms
    
    def getItems(self):
        return self.items
    
    def getInteractables(self):
        return self.interactables
    
    def getEffects(self):
        return self.effects
    
    def __str__(self):
        return '{self.name} - {self.description}'.format(self=self)
