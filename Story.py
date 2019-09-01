class Story():
    def __init__(self, number, name,startroom,description):
        self.number = number
        self.name = name
        self.startroom = startroom
        self.description = description
        self.rooms = []
        self.items = []
        self.interactables = []
        self.effects = []
        self.player = None
        
    def setPlayer(self,player):
        self.player = player
        
    def addRoom(self,room):
        self.rooms.append(room)
    
    def addItem(self,item):
        self.items.append(item)
        
    def addInteractable(self,interactable):
        self.interactables.append(interactable)
    
    def addEffect(self,effect):
        self.effects.append(effect)

    def getPlayer(self):
        return self.player
    
    def getRooms(self):
        return self.rooms
    
    def getItems(self):
        return self.items
    
    def getInteractables(self):
        return self.interactables
    
    def getEffects(self):
        return self.effects
    
    def __str__(self):
        return '({self.number}) {self.name} - {self.description}'.format(self=self)
