from loader import loader

gameloader = loader('game.xml')
gameloader.loadStories()

for story in gameloader.getStories():
    print(story)
    for room in story.getRooms():
        print(room.name)