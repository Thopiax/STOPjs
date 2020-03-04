class Player:

    def __init__(self, room, color):
        self.room = room
        self.id = color


    def __repr__(self):
        return {
            "room": self.room,
            "color": self.room
        }


def get_new_color():
    return "BLUE"