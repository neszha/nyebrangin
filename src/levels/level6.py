class Data: pass

# Game.
game = Data()
game.coutdown = 60 # Seconds.
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
player.name = 'tony' # jack, mark, tony
player.position = [120, 100]
player.health = 3
player.speed = 8