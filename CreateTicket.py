import random
import numpy as np
import time

ticket_index = 0


def create_binary_array():
    array_created = False
    while not array_created:
        binary_array = []
        a = 0
        while a < 9:
            array = np.random.choice([0, 1], size=3)
            # print(array)
            ones = 0
            for x in array:
                if x == 1:
                    ones += 1
            if ones == 2:
                binary_array.append([array[0], array[1], array[2]])
                a += 1
        a = 0
        num = random.sample(range(0, 9), 3)
        while a < 3:
            direction = random.choice([0, 1])
            if direction == 1:
                for z in range(0, 3):
                    if binary_array[num[a]][z] == 1:
                        binary_array[num[a]][z] = 0
                        break
            else:
                for z in range(2, -1, -1):
                    if binary_array[num[a]][z] == 1:
                        binary_array[num[a]][z] = 0
                        break
            a += 1

        row_count = [0, 0, 0]
        for row in binary_array:
            for ind in range(len(row)):
                row_count[ind] = row_count[ind] + row[ind]

        if (row_count[0] == row_count[1]) and (row_count[1] == row_count[2]) and (row_count[0] == 5):
            array_created = True
    return binary_array


def create_random_int_array():
    num_array = list()
    num_array.append(sorted(random.sample(range(1, 10), 2)))
    for x in range(1, 9):
        num_array.append(sorted(random.sample(range(10*x, 10*(x+1)), 2)))
        time.sleep(0.005)
    return num_array


def create_ticket(bin_array=create_binary_array(), int_array=create_random_int_array()):
    temp_ticket = []
    for x in range(len(bin_array)):
        temp_array = []
        int_ind = 0
        for y in range(len(bin_array[x])):
            if bin_array[x][y] == 1:
                temp_array.append(str(int_array[x][int_ind]))
                int_ind += 1
            else:
                temp_array.append('x')

        temp_ticket.append(temp_array)
    return temp_ticket


def console_print_ticket(temp_ticket):
    for x in range(0, 3):
        for y in range(0, 9):
            print(temp_ticket[y][x], end='\t', flush=True)
        print()


def convert_to_string(temp_ticket):
    ticket = ''
    for x in range(0, 3):
        for y in range(0, 9):
            ticket += str(temp_ticket[y][x]) + ' '
        if x != 2:
            ticket += ': '
    return ticket
