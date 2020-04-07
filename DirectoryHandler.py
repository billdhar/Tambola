import os
import filecmp

def_path = './Ticket Text'
def_ticket_image_path = './Ticket Images'


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
    final_val = True
    for x in range(0, len(file_list)-1):
        for y in range(x+1, len(file_list)):
            file1 = dir_path + '/' + file_list[x]
            file2 = dir_path + '/' + file_list[y]
            val = filecmp.cmp(file1, file2)
            if print_outputs:
                print('Comparing: ' + file1 + "=" + file2 + " > ", str(val))
            if val:
                print(file1 + " matches " + file2)
                final_val = False
                break
        if val:
            break
    return final_val


def delete_previous_tickets():
    ticket_text_file_list = os.listdir(def_path)
    ticket_image_file_list = os.listdir(def_ticket_image_path)

    for file in ticket_text_file_list:
        os.remove(def_path + "/" + file)

    for file in ticket_image_file_list:
        os.remove(def_ticket_image_path + "/" + file)

    print("Previous Files Removed!")
