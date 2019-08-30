class Action():
    def __init__(self, name, description,
                 faildescription, item, requiredEffects,
                 givenEffects, removedEffects, requiredItems,
                 givenItems, removedItems, newDesc,
                 newItems, newArt, newInteractables):
        self.name = name
        self.description = description
        self.faildescription = faildescription
        self.item = item
        self.requiredEffects = requiredEffects
        self.givenEffects = givenEffects
        self.removedEffects = removedEffects
        self.requiredItems = requiredItems
        self.givenItems = givenItems
        self.removedItems = removedItems
        self.newDesc = newDesc
        self.newItems = newItems
        self.newArt = newArt
        self.newInteractables = newInteractables
    def __str__(self):
        return '''
                {self.name}:{self.description}
                {self.faildescription}:{self.item}
                {self.requiredEffects}:{self.givenEffects}
                {self.removedEffects}:{self.requiredItems}
                {self.givenItems}:{self.removedItems}
                {self.newDesc}:{self.newItems}
                {self.newArt}:{self.newInteractables}
                '''.format(self=self)

                
        
