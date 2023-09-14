coordinates = {'0,0':1,'1,0':2}
# order is always, right, up, left, down
moving = 'right'
next_square = 3
current_x = 1
current_y = 0
while next_square <= 368078:
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
    coordinates[f"{current_x},{current_y}"] = next_square
    next_square += 1

print(abs(current_x) + abs(current_y))