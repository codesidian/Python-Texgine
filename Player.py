class Player():
    def __init__(self,name,description,effects = [] ,items = [],art = ''):
        self.name = name
        self.description = description
        self.effects = effects
        self.items = items
        self.art = art
    
    def getEffects(self):
        return self.effects
    def getItems(self):
        return self.items
    def getArt(self):
        return self.art
    
    def addEffect(self,effect):
        self.effects.append(effect)
    def addItem(self,item):
        self.items.append(item)
    
    def setDescription(self,description):
        self.description = description
        
    def __str__(self):
        return '{self.name}:{self.description}:{self.effects}:{self.items}:{self.art}'.format(self=self)