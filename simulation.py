import config
from robots import Robot
from pickup import PickupPoint
from delivery import DeliveryPoint
from utils import Timer

class Simulation:
    def __init__(self):
        self.pickup_point = PickupPoint(pos=(2, 2))

        # Delivery points
        self.delivery_points = {
            'A': DeliveryPoint('A', (18, 2)),
            'B': DeliveryPoint('B', (18, 10)),
            'C': DeliveryPoint('C', (18, 18))
        }

        self.robots = [
            Robot(id=1, home=(0, 0)),
            Robot(id=2, home=(0, config.GRID_HEIGHT - 1))
        ]

        self.spawn_timer = Timer(4)
        self.all_parcels = []

        # Set up robots with references to each other
        for robot in self.robots:
            robot.set_other_robots(self.robots)

    def find_best_robot_for_task(self):
        idle_robots = [r for r in self.robots if r.state == "idle"]
        if not idle_robots:
            return None
            
        # Find the closest idle robot to the pickup point
        best_robot = min(
            idle_robots,
            key=lambda r: r.distance_to(self.pickup_point.pos)
        )
        return best_robot

    def update(self):
        # 1. Spawn a new parcel every 20 seconds
        if self.spawn_timer.ready():
            self.pickup_point.spawn_parcel()
            self.spawn_timer.reset()

        # 2. Assign tasks to idle robots
        while self.pickup_point.parcels:
            best_robot = self.find_best_robot_for_task()
            if not best_robot:
                break
                
            parcel = self.pickup_point.parcels.pop(0)
            delivery_point = self.delivery_points[parcel.delivery_point]
            best_robot.assign_task(
                parcel=parcel,
                pickup_pos=self.pickup_point.pos,
                delivery_pos=delivery_point.pos,
                delivery_point=delivery_point
            )
            self.all_parcels.append(parcel)

        # 3. Update robot movement and task completion
        for robot in self.robots:
            robot.move()

        # 4. Update delivery points
        for dp in self.delivery_points.values():
            dp.update()

    def draw(self, screen):
        self.pickup_point.draw(screen)
        for dp in self.delivery_points.values():
            dp.draw(screen)
        for robot in self.robots:
            robot.draw(screen)
