class Data: pass

# Game.
game = Data()
game.coutdown = 60 * 2 # Seconds.
game.trophy = [
    { 'time_left': 45, 'trophy': 3 },
    { 'time_left': 25, 'trophy': 2 },
    { 'time_left': 1, 'trophy': 1 },
]

# Map.
map = Data()
map.image_path = 'assets/maps/MAP03.png' # Location of game map.
map.forbidden_area_color = (255, 0, 0, 0) # (R, G, B, A).
map.forbidden_area = [ 
    # [(size), (location)],
    [(1282, 54), (0, 0)],
    [(99, 89), (0, 330)],
    [(350, 89), (174, 330)],
    [(350,89), (600, 330)],
    [(252,89), (1026, 330)],
    [(75, 718), (-74, 0)],
    [(75, 718), (1280, 0)],
    [(1279, 61), (0, 720)],
]

# Obstacles.S
obstacle = Data()
obstacle.list = [
    {
        'image_path': 'assets/images/obstacles/gravel.png',
        'position': [1061, 67],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [111, 318],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [908, 675],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [908, 308],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [44, 417],
        'scale': 0.6,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [1131, 52],
        'scale': 0.6,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [732, 302],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [1126, 673],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [774, 692],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [667, 679],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [805, 433],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [778, 431],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [561, 57],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [222, 70],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [69, 52],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [523, 58],
        'scale': 0.6,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [895, 415],
        'scale': 0.8,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [887, 70],
        'scale': 0.8,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [1027, 695],
        'scale': 0.8,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/trunk.png',
        'position': [531, 695],
        'scale': 0.8,
        'rotation': 16,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1189, 642],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [340, 642],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1059, 390],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [767, 24],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [360, 292],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1182, 292],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [417, 420],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [204, 420],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [383, 58],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [179, 668],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
]

# Cars.
car = Data()
car.use = [ 
    # 'assets/images/cars/vertical/1.png',
    # 'assets/images/cars/vertical/2.png',
    # 'assets/images/cars/vertical/3.png',
    # 'assets/images/cars/vertical/4.png',
    # 'assets/images/cars/vertical/5.png',
    'assets/images/cars/vertical/6.png',
    'assets/images/cars/vertical/7.png',
    'assets/images/cars/vertical/8.png',
    'assets/images/cars/vertical/9.png',
    'assets/images/cars/vertical/10.png',
]
car.traffic_density = [6, 10]
car.speed_range = [30, 60]
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
        'position': [356, 710],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [978, 420],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [50, 710],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [539, 710],
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
player.name = 'jack' # jack, mark, tony
player.position = [120, 100]
player.health = 3
player.speed = 8