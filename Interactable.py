class Interactable():
    def __init__(self,name, description, requiredEffects = []):
        '''
            -`name`: the name of the interactable
            -`description`: the description of the interactable
            -`requiredEffects`: a list of required effects(objs).
        '''
        self.name = name
        self.description = description
        self.requiredEffects = requiredEffects
        self.actions = []
    def getActions(self):
        return self.actions
    
    def addAction(self,action):
        self.actions.append(action)
        
    def setName(self,name):
        self.name = name
        
    def setDescription(self,desc):
        self.description = desc
    
    def addRequiredEffect(self,effect):
        self.requiredEffects.append(effect)

    def __str__(self):
        return '{self.name}:{self.description}:{self.requiredEffects}:{self.actions}'.format(self=self)
    
