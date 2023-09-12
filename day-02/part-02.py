checksum = 0
# the current working directory for visual studio is the project root
with open('day-02/input', 'r') as file:
    for line in file:
        numbers_list = [int(x) for x in line.split()]
        for i in range(len(numbers_list)):
            for ii in range(len(numbers_list)):
                if i != ii and numbers_list[i] % numbers_list[ii] == 0:
                    checksum += int(numbers_list[i] / numbers_list[ii])

# TODO: break out of loops as soon as a evenly divisible pair is found for faster performance
print(checksum)