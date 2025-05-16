import config

class Parcel:
    def __init__(self, id, pos, delivery_point, colour=config.PARCEL_COLOUR):
        self.id = id
        self.pos = pos
        self.delivery_point = delivery_point
        self.state = 'idle'  #idle, picked, delivered
        self.colour = colour
        
    def pick(self):
        self.state = 'picked'

    def deliver(self):
        self.state = 'delivered'

    def is_waiting(self):
        return self.state == 'idle' 
    
    def __repr__(self):
        return f"Parcel(id={self.id}, pos={self.pos}, delivery_point={self.delivery_point}, state={self.state})"