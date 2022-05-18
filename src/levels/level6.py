class Data: pass

# Game.
game = Data()
game.coutdown = 400 # Seconds.
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
        'position': [822, 97],
        'scale': 0.5,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [229, 683],
        'scale': 0.5,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [136, 363],
        'scale': 0.5,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [770, 683],
        'scale': 0.5,
        'rotation': 0,
        'danger': True,
    },
    {
        'image_path': 'assets/images/obstacles/hole.png',
        'position': [983, 370],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [899, 78],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [1106, 77],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [1123, 78],
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
        'position': [453, 98],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [678, 702],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/wooden-box.png',
        'position': [911, 702],
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
        'image_path': 'assets/images/obstacles/stone.png',
        'position':[509, 78],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone.png',
        'position':[1061, 92],
        'scale': 0.5,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position':[94, 83],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position':[110, 83],
        'scale': 1,
        'rotation': 0,
        'danger': False,
    },
    {
        'image_path': 'assets/images/obstacles/stone-block.png',
        'position':[972, 702],
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
        [174, 300],
        #[473, 572],
    ],
    'right': [
        [463, 572],
        #[174, 220],
    ],
}

# Civilians.
civilian = Data()
civilian.list = [
    {
        'name': 'mark', # jack, mark, tony
        'position': [356, 140],
        'destination': [140, 420]
    },
     {
        'name': 'jack', # jack, mark, tony
        'position': [747, 100],
        'destination': [140, 420]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [978, 420],
        'destination': [1252, 100]
    },
    {
        'name': 'tony', # jack, mark, tony
        'position': [50, 710],
        'destination': [1252, 100]
    },
    {
        'name': 'mark', # jack, mark, tony
        'position': [539, 710],
        'destination': [1252, 100]
    },
    {
        'name': 'jack', # jack, mark, tony
        'position': [1120, 710],
        'destination': [1252, 100]
    },

]

# Palyer
player = Data()
player.name = 'tony' # jack, mark, tony
player.position = [150, 100]
player.health = 3
player.speed = 8