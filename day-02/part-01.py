checksum = 0
# the current working directory for visual studio is the project root
with open('day-02/input', 'r') as file:
    for line in file:
        numbers_list = [int(x) for x in line.split()]
        checksum += max(numbers_list) - min(numbers_list)

print(checksum)