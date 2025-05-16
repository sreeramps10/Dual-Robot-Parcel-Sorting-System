# Dual-Robot-Parcel-Sorting-System

This is a dual robot parcel delivery system implemented using Pygame. Two robots are allowed to pick up parcels from the center pick up point and deliver them to the designated delivery points while avoiding obstacles in a 2D environment. Every 4 seconds a parcel with a delivery point of random choice spawns at the pick up point where a max of 5 parcels is the capacity. After the delivery of 20 parcels to either of the three delivery points, that point will revert its number of parcel count back to 0 as the parcels will be loaded onto a truck.

Features:
- 20x20 Grid Based Environment
- 2 Autonomous Robots
- 1 Pick Up Point
- 3 Delivery Points
- Obstacle avoidance
- A* Algorithm Path Planning
- Timed Parcel Generation and Task Allocation



https://github.com/user-attachments/assets/921985ba-15c2-4b30-bff1-06a7a2b491e3



Project Structure:
1) main.py           # Runs Simulation Loop
2) simulation.py     # Manages environment, robots and parcels
3) config.py         # Initialize data
4) utils.py          # Helper functions and A* Algorithm
5) parcel.py         # Define Parcel movement
6) robots.py         # Robot class and behaviour
7) delivery.py       # Delivery point behaviour
8) pickup.py         # Pick up point behaviour
9) grid.py           # Grid and obstacles drawing

Requirements:
- python 3.7+
- pygame library

How to Run:
python3 main.py

Future Improvements:
- More than 2 robots
- More than 1 pick up point
- Better UI

