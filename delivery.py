import config
import pygame

class DeliveryPoint:
    def __init__(self, id, pos,  threshold = config.DELIVERY_THRESHOLD, colour=config.DELIVERY_COLOUR):
        self.id = id
        self.pos = pos
        self.threshold = threshold
        self.parcels = []
        self.load_threshold = threshold
        self.colour = colour    

    def receive_parcel(self, parcel):
        self.parcels.append(parcel)

    def is_ready(self):
        return len(self.parcels) >= self.threshold
    
    def load_truck(self):
        if self.is_ready():
            self.parcels = []

    def update(self):
        if self.is_ready():
            self.load_truck()
        
    
    def draw(self, screen):
        x, y = self.pos
        rect = pygame.Rect(x * config.CELL_SIZE, y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, self.colour, rect)

        font = pygame.font.SysFont(None, 24)
        text = font.render(str(len(self.parcels)), True, (0, 0, 0))
        screen.blit(text, (x * config.CELL_SIZE + 5, y * config.CELL_SIZE + 5))
        
    def __repr__(self):
        return f"Delivery(id={self.id}, pos={self.pos}, threshold={self.threshold}, parcels={len(self.parcels)})"
