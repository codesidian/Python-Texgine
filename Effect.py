class Effect():
    def __init__(self, name, description, isRoomChange=False, roomname=None):
        self.name = name
        self.description = description
        self.isRoomChange = isRoomChange
        self.roomname = roomname

    def __str__(self):
        return '{self.name}:{self.description}:{self.isRoomChange}:{self.roomname}'.format(self=self)
