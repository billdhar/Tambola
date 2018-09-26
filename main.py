import os
import time

from CreateTicket import *
from CheckTicket import save_ticket


def create_tickets(n=1):
    x = 0
    while x < n:
        bin_arr = create_binary_array()
        int_arr = create_random_int_array()
        ticket = create_ticket(bin_arr, int_arr)
        str_ticket = convert_to_string(ticket)
        if save_ticket(str_ticket):
            print('Completed... ' + str(x) + '\r')
            x += 1
        else:
            print('Retrying...')
            time.sleep(0.05)
    print('Done!')

create_tickets(1000)