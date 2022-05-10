class Data: pass

# Game.
game = Data()
game.coutdown = 60 # Seconds.

# Map.
map = Data()
map.image_path = 'assets/maps/MAP02.png' # Location of game map.
map.forbidden_area_color = (255, 0, 0, 100) # (R, G, B, A).
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
civilian = Data()
civilian.list = [
    {
        'name': 'tony',
        'position': [300, 290],
        'destination': [600, 290]
    },
    {
        'name': 'tony',
        'position': [400, 290],
        'destination': [700, 290]
    },
    {
        'name': 'tony',
        'position': [700, 290],
        'destination': [700, 600]
    }
]

# Cars.
car = Data()
car.use = [ 
    'assets/images/cars/vertical/1.png',
    'assets/images/cars/vertical/2.png',
    'assets/images/cars/vertical/3.png',
]
car.traffic_density = [6, 10]
car.speed_range = [30, 60]
car.direction = {
    # 'direction': [random range position y]
    'left': [174, 300],
    'right': [463, 572],
}

# Civilians.
civilian = Data()
civilian.list = [
    {
        'name': 'tony',
        'position': [300, 290],
        'destination': [600, 290]
    },
    {
        'name': 'tony',
        'position': [400, 290],
        'destination': [700, 290]
    },
    {
        'name': 'tony',
        'position': [700, 290],
        'destination': [700, 600]
    },
]

# Palyer
player = Data()
player.name = 'tony'
player.position = [120, 100]
player.health = 3
player.speed = 8