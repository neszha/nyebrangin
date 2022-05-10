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
    [(258, 76), (1021, 360)],
    [(779, 76), (177, 360)],
    
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
]
car.traffic_density = [1, 3]
car.speed_range = [100, 2000]
car.direction = {
    # 'direction': [random range position y]
    'left': [350, 420],
    'right': [430, 500],
}

# Civilians.
civilian = Data()

# Palyer
player = Data()
player.name = 'tony'
player.position = [200, 290]
player.health = 3
player.speed = 8