class Item():
    def __init__(self,name,description,sellable,value):
        self.name = name 
        self.description = description
        self.sellable = sellable
        self.value = value
    
    def __str__(self):
        return '{self.name}:{self.description}:{self.sellable}:{self.value}'.format(self=self)