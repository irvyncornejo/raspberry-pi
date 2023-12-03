import time
import neopixel
from umachine import Pin
import random


from gpiopico import  Joystick
from message import jam_message, game_name
import tm1637
from machine import Pin

tm = tm1637.TM1637(clk=Pin(1), dio=Pin(0))

joystick_2 = Joystick(26, 27, 22)
joystick_1 = Joystick(4, 28, 22)
pin = Pin(15, Pin.OUT)
pixel = neopixel.NeoPixel(pin, 256)


color_null = (0, 0, 0)
point_color = (20, 0, 0)
point_color_two = (30, 0, 10)
paddle_color_one = (0, 30, 2)
base_matrix = [color_null]*255
matrix = [[(0, 0, 0)]*16]*16



def delete():
    for n, color in enumerate(base_matrix):
        pixel[n] = (0, 0, 0)
    pixel.write()

def move_point(paddle_o, paddle_t, matrix, point_one, point_two, score_a, score_b):
    try:
        matrix = [row[:] for row in matrix]

        for number_row, row in enumerate(matrix):
            if number_row in paddle_o:
                matrix[0][number_row] = paddle_color_one
            if number_row in paddle_t:
                matrix[15][number_row] = point_color

            matrix[point_one][point_two] = point_color_two

            if number_row != 0 and number_row % 2 != 0:
                row.reverse()

        matrix = [j for i in matrix for j in i]

        for n, elem in enumerate(matrix):
            pixel[n] = elem
        pixel.write()
        
        if not point_two in paddle_o and point_one == 0:
            score_a += 1
            return score_a, score_b

        if not point_two in paddle_t and point_one >= 14:
            score_b += 1
            return score_a, score_b

        return score_a, score_b


    except IndexError:
        print('Error')
        delete()

def move_paddles(paddle, value_operation)->list:
    if paddle[-1] == 14:
        return [ pixel + 1 for pixel in paddle]

    if paddle[-1] == 1:
        return [ pixel - 1 for pixel in paddle]

    elif (paddle[-1] + value_operation) > 15  or (paddle[0] + value_operation) < 0:
        return paddle
    return [ pixel + value_operation for pixel in paddle]

def define_bounces(point, last_bounces):
    if point == 15:
        last_bounces = 'up'
        point -= 1
        return point, last_bounces

    if point == 0:
        last_bounces = 'down'
        point += 1
        return point, last_bounces

    else:
        if last_bounces == 'up':
            point -= 1
        else:
            point += 1
        return point, last_bounces

def move_po(point_a_position, point_b_position,last_direction, last_bounces):
    point_b_position, last_bounces = define_bounces(point_b_position, last_bounces)
    if last_direction == 'left':
        if point_a_position < 14:
            point_a_position += increment
            return point_a_position, point_b_position,last_direction, last_bounces
        else:
            point_a_position -= increment
            last_direction = 'r'
            return point_a_position, point_b_position,last_direction,last_bounces

    else:
        if point_a_position > 1:
            point_a_position -= increment
            return point_a_position, point_b_position,last_direction, last_bounces
        else:
            point_a_position += increment
            last_direction = 'left'
            return point_a_position, point_b_position,last_direction, last_bounces

def write_message(matrix):
    def hex_to_rgb(value):
        _value = value.strip().replace('#', '')
        _rgb = len(_value)
        if _rgb != 6:
            raise ValueError(f'The hex color #{value} is not valid')
        return tuple(int(_value[i:i+_rgb//3], 16) for i in range(0, _rgb, _rgb//3))
    
    matrix = [row[:] for row in matrix]
    for number_row, row in enumerate(matrix):
        if number_row != 0 and number_row % 2 != 0:
            row.reverse()
    matrix = [j for i in matrix for j in i]

    for n, elem in enumerate(matrix):
        pixel[n] = hex_to_rgb(elem)
    pixel.write()
        
    


paddle_init = [ 6, 7, 8, 9, 10]
point_a = 2
point_b = 8
last_position_paddle_one = []
last_position_paddle_two = []
point_a_position = point_a
point_b_position = point_b
last_direction='left'
last_bounces = ''
increment = 2
levels = [0.1, 0.05, 0.03, 0.01]
game = False
score_a = 0
score_b = 0

time.sleep(5)
while True:
    tm.numbers(score_a, score_b)
    while not game:
        write_message(jam_message)
        time.sleep(2)
        write_message(game_name)
        time.sleep(2)
        game = True

    vertical_1, horizontal_1 = joystick_1.get_values()
    vertical_2, horizontal_2 = joystick_2.get_values()
    
    last_position_paddle_one = paddle_init if last_position_paddle_one == [] else last_position_paddle_one
    last_position_paddle_two = paddle_init if last_position_paddle_two == [] else last_position_paddle_two

    if horizontal_2 > 2.2:
        last_movement = 'down'
        last_position_paddle_one=move_paddles(last_position_paddle_one, increment)

    if horizontal_2 < 1.2:
        last_movement = 'up'
        last_position_paddle_one=move_paddles(last_position_paddle_one, -increment)

    if horizontal_1 > 2.0:
        last_movement = 'up'
        last_position_paddle_two=move_paddles(last_position_paddle_two, increment)
        

    if horizontal_1 < 1.5:
        last_movement = 'down'
        last_position_paddle_two=move_paddles(last_position_paddle_two, -increment)
        
    else:
        pass

    point_a_position, point_b_position, last_direction, last_bounces = move_po(point_a_position, point_b_position,last_direction, last_bounces)
    score_a , score_b=move_point(last_position_paddle_one, last_position_paddle_two, matrix, point_a_position, point_b_position, score_a, score_b)
    time.sleep(0.05)
