import os
import filecmp

def_path = './Tickets'


def check_dir(dir_path=def_path):
    if os.path.exists(dir_path):
        return True
    else:
        return False


def create_dir(dir_path=def_path):
    os.mkdir(dir_path)


def init(dir_path=def_path):
    if not check_dir(dir_path):
        create_dir(dir_path)

def compare_all_tickets(dir_path=def_path, print_outputs=False):
    file_list = os.listdir(dir_path)
    val = False
    for x in range(0, len(file_list)-1):
        for y in range(x+1, len(file_list)):
            file1 = dir_path + '/' + file_list[x]
            file2 = dir_path + '/' + file_list[y]
            val = filecmp.cmp(file1, file2)
            if print_outputs:
                print('Comparing: ' + file1 + "=" + file2 + " > ", str(val))
            if val:
                print(file1 + " matches " + file2)
                break
        if val:
            break


compare_all_tickets()