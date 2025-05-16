from parcel import Parcel
from utils import generate_random_parcel_id
import pygame
import config


class PickupPoint:
    def __init__(self, pos, capacity = config.MAX_PARCELS, colour=config.PICKUP_COLOUR):
        self.pos = pos
        self.capacity = capacity
        self.parcels = []
        self.colour = colour

    def spawn_parcel(self):
        if len(self.parcels) < self.capacity:
            parcel_id, delivery_point = generate_random_parcel_id()
            new_parcel = Parcel(self.pos, parcel_id, delivery_point)
            self.parcels.append(new_parcel)
            print(f"Spawned parcel {parcel_id} for delivery point {delivery_point}")
        else:
            print("Pickup point full — cannot spawn more parcels.")

    def draw(self, screen):
        x, y = self.pos
        rect = pygame.Rect(x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, self.colour, rect)
        
        font = pygame.font.SysFont(None, 24)
        text = font.render(str(len(self.parcels)), True, (0, 0, 0))
        screen.blit(text, (x * config.CELL_SIZE + 5, y * config.CELL_SIZE + 5))
        
    def remove_parcel(self, parcel):
        if parcel in self.parcels:
            self.parcels.remove(parcel)

    def has_parcel(self):
        return len(self.parcels) > 0
    
    def get_parcel(self):
        if self.has_parcels():
            return self.parcels[0]
        else:
            return None

    def __repr__(self):
        return f"Pickup(pos={self.pos}, Parcels={len(self.parcels)}/{self.capacity})"
    


        