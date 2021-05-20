#constantes
POS_X = 0
POS_Y = 1
map_width = 20
map_height = 15

my_position = [3, 1]

print("+" + "-" * map_width * 3 + "+")

for coordinate_y in range(map_height):
    print("|", end="")
    for coordinate_x in range(map_width):
        #si tu posicionX y posicionY estan dentro de las coordenadas X y X, pon un @
        if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
            print(" @ ", end="")
        else:
            print("   ", end="")
    print("|")

print("+" + "-" * map_width * 3 + "+")

