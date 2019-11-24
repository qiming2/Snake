class GameObj(object):

    def __init__(self, location=(0, 0),
                 velocity=[0, 0],
                 acceleration=[0, 0],
                 tag=None,
                 width=0,
                 height=0,
                 color="red"):
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self.tag = tag
        self.width = width
        self.height = height
        self.color = color

