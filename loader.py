import untangle
from Story import Story
from Room import Room
class loader():
    def __init__(self,gamefile):
        ''' `gamefile` : filename of the XML game data containing stories '''
        self.gamedata = untangle.parse(gamefile)
        self.stories = []
        #ParseRooms(obj)
        
    def loadStories(self):
        storiesObjs = [story for story in self.gamedata.stories.story]
        names = [story.name.cdata for story in storiesObjs]
        for st in storiesObjs:
            currStory = Story(st.name.cdata,st.startRoom.cdata,st.description.cdata)
            for room in st.room:
                currRoom = Room(room.name.cdata,room.description.cdata,room.art.cdata,room.interactables.cdata)
                currStory.addRoom(currRoom)
            for item in st.item:
                currItem = Item()
                currStory.addItem(currItem)
            for interactable in st.interactable:
                currInteractable = Interactable()
                currStory.addInteractable(currInteractable)
                
            self.stories.append(currStory)
            
    def getStories(self):
        return [story for story in self.stories]
        



        





