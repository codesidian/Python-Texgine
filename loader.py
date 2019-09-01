import untangle
from Story import Story
from Room import Room
from Item import Item
from Interactable import Interactable
from Effect import Effect
from Action import Action
from Validator import Validator
from Player import Player
class invalidSetup(Exception):
    pass

class Loader():
    def __init__(self,gamefile):
        ''' `gamefile` : filename of the XML game data containing stories '''
        #validator = Validator()
        #self.gamedata = validator.validate(untangle.parse(gamefile))
        self.gamedata = untangle.parse(gamefile)
        self.stories = []
        #ParseRooms(obj)
        
    def loadStories(self):
        storyNum = 0
        for st in self.gamedata.stories.story:
            storyNum += 1
            currStory = Story(storyNum,st.name.cdata,st.startRoom.cdata,st.description.cdata)
            
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
                for action in interactable.action:
                    currAction = Action(action.name.cdata, action.description.cdata,
                                        action.failDescription.cdata, action.item.cdata,
                                        action.requiredEffects.cdata, action.givenEffects.cdata,
                                        action.removedEffects.cdata, action.requiredItems.cdata,
                                        action.givenItems.cdata, action.removedItems.cdata,
                                        action.newDesc.cdata, action.newItems.cdata,
                                        action.newArt.cdata, action.newInteractables.cdata)
                    
                    currInteractable.addAction(currAction)
                currStory.addInteractable(currInteractable)
                
            for effect in st.effect:
                try:
                    effectName = effect.name.cdata;
                    if effect.isRoomChange.cdata == "True" and effect.isRoomChange['roomname'] == '':
                        raise invalidSetup(Exception);
                    currEffect = Effect(effect.name.cdata,
                                        effect.description.cdata,
                                        effect.isRoomChange.cdata,
                                        effect.isRoomChange['roomname'])
                except AttributeError:
                    currEffect = Effect(effect.name.cdata,
                                        effect.description.cdata)
                except invalidSetup:
                    print('Warning: InvalidEffect - EFFECT[' + effectName+'] STORY['+ currStory.name+'] ROOMCHANGE INGORED')
                    currEffect = Effect(effect.name.cdata,
                                        effect.description.cdata)
                currStory.addEffect(currEffect)
            
            player = Player(st.player.name.cdata,st.player.description.cdata,
                                st.player.effects.cdata,st.player.items.cdata,
                                st.player.art.cdata)
            currStory.setPlayer(player)
                
            self.stories.append(currStory)
            
    def getStories(self):
        return [story for story in self.stories]
        



        





