class Data: pass

# Game.
game = Data()
game.coutdown = 145 # Seconds.
game.trophy = [
    { 'time_left': 100, 'trophy': 3 },
    { 'time_left': 60, 'trophy': 2 },
    { 'time_left': 1, 'trophy': 1 },
]

# Map.
map = Data()
map.image_path = 'assets/maps/MAP01.png' # Location of game map.
map.forbidden_area_color = (255, 0, 0, 0) # (R, G, B, A).
map.forbidden_area = [ 
    # [(size), (location)],
    [(1280, 243), (0, 0)],
    [(1279, 61), (1, 720)],
    [(75, 718), (1280, 0)],
    [(75, 718), (-75, 0)],
    [(94, 51), (0, 669)],
    [(765, 51), (185, 669)],
    [(239, 51), (1041, 669)],
]

# Obstacles.
obstacle = Data()
obstacle.list = [
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [30, 312],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [481, 287],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [529, 523],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1200, 531],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [716, 531],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [35, 531],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1115, 287],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [397, 560],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [1200, 312],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [671, 312],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [186, 640],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [840, 544],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [817, 296],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [261, 296],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [1100, 550],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [237, 547],
        'scale': 1,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [996, 635],
        'scale': 0.8,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [145, 303],
        'scale': 0.7,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [329, 598],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [532, 629],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [883, 265],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [606, 272],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [416, 245],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [561, 610],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [831, 244],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
]

# Cars.
car = Data()
car.use = [ 
    'assets/images/cars/vertical/1.png',
    'assets/images/cars/vertical/2.png',
    'assets/images/cars/vertical/3.png',
    # 'assets/images/cars/vertical/4.png',
    # 'assets/images/cars/vertical/5.png',
    # 'assets/images/cars/vertical/6.png',
    # 'assets/images/cars/vertical/7.png',
    # 'assets/images/cars/vertical/8.png',
    # 'assets/images/cars/vertical/9.png',
    # 'assets/images/cars/vertical/10.png',
]
car.traffic_density = [3, 6]
car.speed_range = [15, 35]
car.direction = {
    # 'direction': [random range position y]
    'left': [
        [350, 420],
    ],
    'right': [
        [430, 500],
    ],
}

# Civilians.
civilian = Data()
civilian.list = [
    {
        'name': 'mark', # jack, mark, tony
        'position': [280, 280],
        'destination': [1227, 620]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [780, 280],
        'destination': [1227, 620]
    },
    {
        'name': 'mark', # jack, mark, tony
        'position': [690, 650],
        'destination': [1227, 270]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [1170, 650],
        'destination': [1227, 270]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [140, 710],
        'destination': [28, 270]
    },
]

# Palyer
player = Data()
player.name = 'tony' # jack, mark, tony
player.position = [200, 290]
player.health = 3
player.speed = 4