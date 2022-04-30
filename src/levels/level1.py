class Data: pass

# Map.
map = Data()
map.image_path = 'assets/maps/MAP01.png'
map.forbidden_area_color = (0, 0, 0, 150)
map.forbidden_area = [ 
    # [(size), (location)],
    [(1280, 243), (0, 0)],
    [(94, 51), (0, 669)],
    [(765, 51), (185, 669)],
    [(239, 51), (1041, 669)],
]

# Player.
player = Data()
player.positions = [100, 100]
player.health = 3
