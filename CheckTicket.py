import os

def_path = './Tickets'

def save_ticket(temp_ticket, dir_path = def_path):
    tickets = get_ticket_list(dir_path)
    match = False
    for ticket in tickets:
        file = open(dir_path + '/' + ticket, 'r')
        if temp_ticket in file.readlines()[1]:
            file.close()
            match = True
            print('Duplicate')
            break
    if not match:
        index = len(tickets) + 1
        file_name = 'Ticket ' + str(index) + '.txt'
        files = os.listdir(dir_path)
        for ticket in files:
            if file_name in ticket:
                print('Found: ' + file_name)
                index += 1
                file_name = 'Ticket ' + str(index) + '.txt'
        file = open(dir_path + '/' + file_name, 'w')
        file.write('Tambola Ticket:\n')
        file.write(temp_ticket)
        file.close()
        return True


def get_ticket_list(dir_path=def_path):
    tickets = []
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    files = os.listdir(dir_path)
    for file in files:
        if '.txt' in file:
            temp_file = open(dir_path + '/' + file, 'r')
            if 'Tambola Ticket:' in temp_file.readline():
                tickets.append(file)
            temp_file.close()
    return tickets


