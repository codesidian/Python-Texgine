import untangle
from Story import Story
from Room import Room
from Item import Item
from Interactable import Interactable

class loader():
    def __init__(self,gamefile):
        ''' `gamefile` : filename of the XML game data containing stories '''
        self.gamedata = untangle.parse(gamefile)
        self.stories = []
        #ParseRooms(obj)
        
    def loadStories(self):
        for st in self.gamedata.stories.story:
            currStory = Story(st.name.cdata,st.startRoom.cdata,st.description.cdata)
            for room in st.room:
                currRoom = Room(room.name.cdata,room.description.cdata,room.art.cdata,room.interactables.cdata)
                currStory.addRoom(currRoom)
            for item in st.item:
                currItem = Item(item.name.cdata,item.description.cdata,item.sellable.cdata,item.value.cdata)
                currStory.addItem(currItem)
            for interactable in st.interactable:
                currInteractable = Interactable(interactable.name.cdata,
                                                interactable.description.cdata,
                                                interactable.requiredEffects.cdata.split(','))
                                                #this is fine, we can just check for req effect name in player's effect list
                currStory.addInteractable(currInteractable)
                
            self.stories.append(currStory)
            
    def getStories(self):
        return [story for story in self.stories]
        



        





