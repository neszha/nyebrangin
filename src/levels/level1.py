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
    [(94, 51), (0, 669)],
    [(765, 51), (185, 669)],
    [(239, 51), (1041, 669)],
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
car.speed_range = [10, 40]
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