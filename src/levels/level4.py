class Data: pass

# Game.
game = Data()
game.coutdown = 300 # Seconds.
game.trophy = [
    { 'time_left': 45, 'trophy': 3 },
    { 'time_left': 25, 'trophy': 2 },
    { 'time_left': 1, 'trophy': 1 },
]

# Map.
map = Data()
map.image_path = 'assets/maps/MAP02.png' # Location of game map.
map.forbidden_area_color = (255, 0, 0, 0) # (R, G, B, A).
map.forbidden_area = [ 
    # [(size), (location)],
    [(1280, 76), (0, 0)],
    [(102, 76), (0, 360)],
    [(779, 76), (177, 360)],
    [(258, 76), (1021, 360)],
    [(75, 718), (-74, 0)],
    [(75, 718), (1280, 0)],
    [(1279, 61), (0, 720)],
]

# Obstacles.
obstacle = Data()
obstacle.list = [
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position':[839, 80],
        'scale': 1,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position':[975, 369],
        'scale': 1,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [1061, 92],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [237, 694],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [963, 658],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/fence.png',
        'position': [113, 390],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [433, 98],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [681, 82],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [448, 98],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [614, 684],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [865, 700],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [850, 700],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [94, 83],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [110, 83],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [230, 96],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [1204, 685],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [1188, 685],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [1068, 698],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [1142, 369],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position': [1031, 399],
        'scale': 1,
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
car.traffic_density = [6, 8]
car.speed_range = [25, 55]
car.direction = {
    # 'direction': [random range position y]
    'left': [
        [174, 300],
        [473, 572],
    ],
    'right': [
        [463, 572],
        [174, 220],
    ],
}

# Civilians.
civilian = Data()
civilian.list = [
    {
        'name': 'tony', # jack, mark, tony
        'position': [31, 100],
        'destination': [1000, 420]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [120, 420],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [50, 710],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [1120, 710],
        'destination': [1252, 100]
    },
]

# Palyer
player = Data()
player.name = 'tony' # jack, mark, tony
player.position = [120, 100]
player.health = 3
player.speed = 6