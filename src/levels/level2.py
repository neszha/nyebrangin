class Data: pass

# Game.
game = Data()
game.coutdown = 60 # Seconds.

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
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [25, 284],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [248, 556],
        'scale': 1,
        'rotation': 16,
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
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [140, 303],
        'scale': 1,
        'rotation': 0,
        'danger': True,
    },
]

# Cars.
car = Data()
car.use = [ 
    'assets/images/cars/vertical/1.png',
    'assets/images/cars/vertical/2.png',
    # 'assets/images/cars/vertical/3.png',
    # 'assets/images/cars/vertical/4.png',
    # 'assets/images/cars/vertical/5.png',
    # 'assets/images/cars/vertical/6.png',
    # 'assets/images/cars/vertical/7.png',
    # 'assets/images/cars/vertical/8.png',
    # 'assets/images/cars/vertical/9.png',
    # 'assets/images/cars/vertical/10.png',
]
car.traffic_density = [1, 3]
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
        'name': 'jack', # jack, mark, tony
        'position': [46, 255],
        'destination': [1227, 640]
    },
    {
        'name': 'mark', # jack, mark, tony
        'position': [266, 640],
        'destination': [1227, 270]
    },
]

# Palyer
player = Data()
player.name = 'tony' # jack, mark, tony
player.position = [200, 290]
player.health = 3
player.speed = 5