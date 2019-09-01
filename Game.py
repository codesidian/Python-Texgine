from Loader import Loader
from Controller import Controller

gameLoader = Loader('game.xml')
gameLoader.loadStories()

for story in gameLoader.getStories():
    print(story)
    for room in story.getRooms():
        print('ROOM INFO:' + str(room.name))
    for inter in story.getInteractables():
        print('INTERACTABLE INFO:' + str(inter))
        for action in inter.getActions():
            print('ACTION INFO:' + str(action))
    for effect in story.getEffects():
        print('EFFECT INFO:' + str(effect))
    for item in story.getItems():
        print('ITEM INFO:' + str(item))
    print('PLAYER INFO:' + str(story.getPlayer()))
    

print('\nEnter the story name or the number of the story you\'d like to play')
for story in gameLoader.getStories():
    print(str(story))


    
