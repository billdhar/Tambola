from CreateTicket import *
from CheckTicket import save_ticket
from DirectoryHandler import compare_all_tickets, delete_previous_tickets
from PIL import Image, ImageDraw, ImageFont

import os

ticket_text_path = "Ticket Text"
template_path = "Template/Tambola Template.png"
ticket_image_path = "Ticket Images"
ticket_tracker_path = "Ticket Tracker.txt"

VERBOSE = True

# Required number of tickets
NUMBER_OF_TICKETS = 25


def create_tickets(n=1):

    x = 0
    while x < n:
        bin_arr = create_binary_array()
        int_arr = create_random_int_array()
        ticket = create_ticket(bin_arr, int_arr)
        str_ticket = convert_to_string(ticket)
        if save_ticket(str_ticket):
            if VERBOSE:
                print('Created... ' + str(x) + '\r')
            x += 1
        else:
            print('Retrying...')
            time.sleep(0.05)


def convert_tickets():
    files = os.listdir(ticket_text_path)

    for file in files:
        file_name = file.title().split(".")[0]

        table_origin_x = 85
        table_origin_y = 150
        table_width = 1600
        table_height = 450
        table_line_thickness = 7

        img_template = Image.open(template_path)

        img = ImageDraw.Draw(img_template)
        shape = [(table_origin_x, table_origin_y), (table_origin_x + table_width, table_origin_y + table_height)]
        img.rectangle(shape, outline="black", width=table_line_thickness)

        line_start_y = table_origin_y + table_height/3
        shape_line = [(table_origin_x, line_start_y), (table_origin_x + table_width, line_start_y)]
        img.line(shape_line, fill="black", width=table_line_thickness)

        line_start_y = table_origin_y + (table_height*2)/3
        shape_line = [(table_origin_x, line_start_y), (table_origin_x + table_width, line_start_y)]
        img.line(shape_line, fill="black", width=table_line_thickness)

        col_num = 9
        for ind in range(1, col_num):
            line_start_x = table_origin_x + table_width*ind/col_num
            shape_line = [(line_start_x, table_origin_y), (line_start_x, table_origin_y + table_height)]
            img.line(shape_line, fill="black", width=table_line_thickness)

        file_data = open(ticket_text_path + "/" + file).read().replace("Tambola Ticket:\n", '').split(':')
        for ind in range(len(file_data)):
            file_data[ind] = file_data[ind].strip().split(' ')

        top_text_margin = 70
        left_text_margin = 90
        text_start_x = table_origin_x
        text_start_y = table_origin_y
        font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 75)
        for row in range(len(file_data)):
            text_y = text_start_y + (row*table_height/len(file_data)) + top_text_margin
            for col in range(len(file_data[row])):
                if file_data[row][col] != 'x':
                    text = file_data[row][col]
                    text_width, text_height = img.textsize(text, font=font)
                    text_x = text_start_x + (col*table_width/len(file_data[row])) + left_text_margin - (text_width/2)
                    img.text((text_x, text_y - (text_height/2)), text, fill="black", font=font, align="left")

        img_template.save(ticket_image_path + "/" + file_name + ".png")

        if VERBOSE:
            print("Created... ", file_name)


def add_footer(file_path, email_address):

    table_origin_x = 85
    table_origin_y = 150
    table_width = 1600
    table_height = 450

    footer_offset_x = 300
    footer_offset_y = 25

    img_final = Image.open(file_path)
    img = ImageDraw.Draw(img_final)
    font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)

    text_width, text_height = img.textsize(email_address, font=font)
    footer_x = table_origin_x + table_width - footer_offset_x - (text_width/2)
    footer_y = table_origin_y + table_height + footer_offset_y
    img.text((footer_x, footer_y), email_address, fill="black", font=font, align="right")
    img_final.save(file_path)


create_tickets()
val = compare_all_tickets(ticket_text_path)
if val:
    convert_tickets()

print("Done!")
