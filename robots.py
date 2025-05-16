import pygame
import config
import utils
from parcel import Parcel

class Robot:
    def __init__(self, id, home, colour=config.ROBOT_COLOUR, speed=config.ROBOT_SPEED): 
        self.id = id
        self.pos = home                           # (x,y)
        self.state = 'idle'                       # idle, moving, delivering, picking up
        self.task = None                          # (type, target_pos)
        self.path = []
        self.color = colour
        self.speed = speed
        self.carrying = False
        self.carried_parcel = None
        self.other_robots = []  
        self.waiting_pos = None

        self.move_counter = 0
        self.move_delay = 5
        
        self.last_positions = []
        self.stuck_threshold = 10
        self.waiting_time = 0

    def set_other_robots(self, robots):
        self.other_robots = [r for r in robots if r.id != self.id]

    def distance_to(self, pos):
        return abs(self.pos[0] - pos[0]) + abs(self.pos[1] - pos[1])

    def is_path_clear(self, next_pos):
        # Check if any other robot is at or moving to the next position
        for robot in self.other_robots:
            if robot.pos == next_pos:
                return False
            if robot.path and robot.path[0] == next_pos:
                # deadlock solution
                if robot.pos == self.path[0] and next_pos == robot.path[0]:
                    # Robot with lower ID waits instead of recalculating
                    if self.id < robot.id:
                        self.waiting_time = 20  # Wait for 20 frames
                        return False
        return True

    def is_stuck(self):
        # Check if robot is oscillating between positions
        if len(self.last_positions) >= self.stuck_threshold:
            # Check if we're alternating between 2 positions
            unique_positions = set(tuple(pos) for pos in self.last_positions)
            return len(unique_positions) <= 2
        return False

    def pick_parcel(self, parcel):
        self.carrying = True
        self.carried_parcel = parcel
        parcel.pick()

    def drop_parcel(self):
        if self.carrying:
            # Get the delivery point from the task and add the parcel to it
            delivery_point = self.task['delivery_point']  # This needs to be passed in assign_task
            delivery_point.receive_parcel(self.carried_parcel)
            self.carried_parcel.deliver()
            self.carried_parcel = None
            self.carrying = False

    def assign_task(self, parcel, pickup_pos, delivery_pos, delivery_point):
        self.task = {
            'parcel': parcel,
            'pickup_pos': pickup_pos,
            'delivery_pos': delivery_pos,
            'delivery_point': delivery_point,  
            'stage': 'picking_up'
        }
   
        if not self.waiting_pos:
            self.waiting_pos = self.find_waiting_position(pickup_pos)
        self.state = 'moving'
        self.path = utils.a_star(self.pos, pickup_pos, config.OBSTACLE_LIST, config.GRID_WIDTH, config.GRID_HEIGHT)

    def recalculate_path(self):
        if self.task:
            if self.task['stage'] == 'picking_up':
                target = self.task['pickup_pos']
            elif self.task['stage'] == 'delivering':
                target = self.task['delivery_pos']
        elif self.state == 'returning':
            target = self.waiting_pos
        else:
            return

        
        temp_obstacles = config.OBSTACLE_LIST + [r.pos for r in self.other_robots]
        # Calculate alternative path
        self.path = utils.a_star(
            self.pos,
            target,
            temp_obstacles,
            config.GRID_WIDTH,
            config.GRID_HEIGHT
        )

    def move(self):
        # Handle waiting time
        if self.waiting_time > 0:
            self.waiting_time -= 1
            return

        # Only process movement every N frames
        self.move_counter += 1
        if self.move_counter < self.move_delay:
            return
        self.move_counter = 0

        # Update position history
        self.last_positions.append(self.pos)
        if len(self.last_positions) > self.stuck_threshold:
            self.last_positions.pop(0)

        if self.path:
            next_pos = self.path[0]
            if self.is_path_clear(next_pos):
                self.pos = self.path.pop(0)
                # Clear stuck detection if we successfully moved
                if len(self.last_positions) >= 2 and self.last_positions[-1] != self.last_positions[-2]:
                    self.last_positions = []
            else:
                # Check if we're stuck before recalculating
                if self.is_stuck():
                    # Add random delay before recalculating to break symmetry
                    self.waiting_time = self.id * 5  
                    self.last_positions = []  
                self.recalculate_path()
        elif self.task:
            if self.task['stage'] == 'picking_up':
                self.pick_parcel(self.task['parcel'])
                # Recalculate path to avoid other robots
                self.path = utils.a_star(
                    self.pos, 
                    self.task['delivery_pos'],
                    config.OBSTACLE_LIST + [r.pos for r in self.other_robots],
                    config.GRID_WIDTH,
                    config.GRID_HEIGHT
                )
                self.task['stage'] = 'delivering'
            elif self.task['stage'] == 'delivering':
                self.drop_parcel()
                self.task = None
                self.state = 'returning'
                # Immediately calculate path to waiting position
                self.path = utils.a_star(
                    self.pos,
                    self.waiting_pos,
                    config.OBSTACLE_LIST + [r.pos for r in self.other_robots],
                    config.GRID_WIDTH,
                    config.GRID_HEIGHT
                )
        elif self.state == 'returning' and not self.path:
            self.state = 'idle'

    def draw(self, screen):
        x = self.pos[0] * config.CELL_SIZE
        y = self.pos[1] * config.CELL_SIZE
        pygame.draw.rect(screen, self.color, (x, y, config.CELL_SIZE, config.CELL_SIZE))  

    def find_waiting_position(self, pickup_pos):
        return (pickup_pos[0] + 1, pickup_pos[1] + 1)  



        