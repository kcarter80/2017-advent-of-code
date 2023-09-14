coordinates = {'0,0':1,'1,0':1}
# order is always, right, up, left, down
moving = 'right'
current_square_value = 1
current_x = 1
current_y = 0

while current_square_value <= 368078:
    if moving == 'right':
        # check if square above is filled
        if f"{current_x},{current_y + 1}" in coordinates:
            current_x += 1
        else:
            moving = 'up'
            current_y += 1
    elif moving == 'up':
        # check if square to left is filled
        if f"{current_x - 1},{current_y}" in coordinates:
            current_y += 1
        else:
            moving = 'left'
            current_x -= 1
    elif moving == 'left':      
        # check if square below is filled
        if f"{current_x},{current_y - 1}" in coordinates:
            current_x -= 1
        else:
            moving = 'down'
            current_y -= 1
    elif moving == 'down':
        # check if square to right is filled
        if f"{current_x + 1},{current_y}" in coordinates:
            current_y -= 1
        else:
            moving = 'right'
            current_x += 1
    # sums the values of all the neighboring keys that exist (or adds 0 for keys that don't exist)
    current_square_value = sum(coordinates.get(key, 0) for key in [
        f"{current_x -1},{current_y -1}",
        f"{current_x},{current_y -1}",
        f"{current_x +1},{current_y -1}",
        f"{current_x -1},{current_y}",
        f"{current_x +1},{current_y}",
        f"{current_x -1},{current_y +1}",
        f"{current_x},{current_y +1}",
        f"{current_x +1},{current_y +1}"
    ])
    coordinates[f"{current_x},{current_y}"] = current_square_value

print(current_square_value)