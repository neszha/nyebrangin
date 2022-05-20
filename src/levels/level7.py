class Data: pass

# Game.
game = Data()
game.coutdown = 465# Seconds.
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

# Obstacles.
obstacle = Data()
obstacle.list = [
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [75, 300],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [337, 418],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/puddle.png',
        'position': [168, 64],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [1114, 415],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/chopped.png',
        'position': [830, 673],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [145, 424],
        'scale': 0.8,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [1110, 692],
        'scale': 0.8,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/gravel.png',
        'position': [423, 673],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/gravel.png',
        'position': [1012, 55],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [1108, 52],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [903, 422],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [641, 66],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [42, 691],
        'scale': 0.6,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position': [572, 285],
        'scale': 0.8,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [362, 26],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [1059, 384],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [661, 384],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/tree.png',
        'position': [887, 13],
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
car.traffic_density = [6, 10]
car.speed_range = [30, 60]
car.direction = {
    # 'direction': [random range position y]
    'left': [
        [104, 227],
       # [473, 572],
    ],
    'right': [
        [463, 572],
       # [174, 220],
    ],
}

# Civilians.
civilian = Data()
civilian.list = [
    {
        'name': 'mark', # jack, mark, tony
        'position': [1161, 90],
        'destination': [975, 430]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [978, 420],
        'destination': [1252, 70]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [382, 440],
        'destination': [1252, 70]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [539, 710],
        'destination': [1252, 70]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [1120, 710],
        'destination': [1252, 70]
    },

]

# Palyer
player = Data()
player.name = 'tony' # jack, mark, tony
player.position = [120, 100]
player.health = 3
player.speed = 8