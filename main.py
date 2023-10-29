from turtle import *
from math import *

colors_list = ['red', 'blue', 'aquamarine', 'green', 'gold', 'purple']  # list of colors

def get_color_choice():  # function to get a color
    print('Avaluable color:')
    for color_menu in range(len(colors_list)):
        print(colors_list[color_menu])

    right_color = False
    user_color = str(input('Please, choose the color: '))
    while right_color is False:
        if user_color not in colors_list:
            print('"' + user_color + '"', 'is wrong name of color, try again: ', end='')
            user_color = str(input())
        else:
            right_color = True
    return user_color

def get_num_hexagons():  # function to get a number of hexagons
    right_num_hex = False
    user_num_hex = int(input('Please, choose the number of hexagons: '))
    while right_num_hex is False:
        try:
            if user_num_hex < 4 or user_num_hex > 20:
                print('Number of hexagons must more than 3 and less then 20, try again: ', end='')
                user_num_hex = int(input())
            else:
                right_num_hex = True
        except ValueError:
            print('Number of hexagons must be a digit, try again: ', end='')
            user_num_hex = int(input())
    return user_num_hex
def draw_hexagon(x,y,side_len,border_color, fill_color):  # function to draw hexagon

    goto(x,y)
    pd()
    begin_fill()
    color(border_color, fill_color)
    lt(30)
    fd(side_len)
    lt(60)
    fd(side_len)
    lt(60)
    fd(side_len)
    lt(60)
    fd(side_len)
    lt(60)
    fd(side_len)
    lt(60)
    fd(side_len)
    lt(30)
    end_fill()
    pu()
    goto(0,0)

fill_color1 = get_color_choice()  # get user input for fill color
fill_color2 = get_color_choice()  # get user input for fill color
num_hex = get_num_hexagons()  # get user input the number of hexagons

d_hex_len = 500//num_hex
side_len = d_hex_len / sqrt(3)


screen = Screen()
screen.setup(width=1.0, height=1.0) # set up Turtle graphics screen to cover all window


speed(0) # set the fastest speed


goto(0, 0)
pu()


for itr in range(num_hex - (num_hex//2)): # create left part part of the pattern
    if itr % 2 == 0:
        for itr2 in range(num_hex): # creating individual hexagons in each row
            if itr2 % 2 == 0:
                draw_hexagon(itr2 * d_hex_len,itr * side_len * 3,side_len,'black',fill_color1)
            else:
                draw_hexagon(itr2 * d_hex_len,itr * side_len * 3,side_len,'black',fill_color2)
    else:
        for itr2 in range(num_hex): # creating individual hexagons in each row
            if itr2 % 2 == 0:
                draw_hexagon(itr2 * d_hex_len,itr * side_len * 3,side_len,'black',fill_color2)
            else:
                draw_hexagon(itr2 * d_hex_len,itr * side_len * 3,side_len,'black',fill_color1)

for itr in range(num_hex//2): # create right part part of the pattern
    if itr % 2 == 0:
        for itr2 in range(num_hex): # creating individual hexagons in each row
            if itr2 % 2 == 0:
                draw_hexagon((itr2 * d_hex_len) + (d_hex_len / 2),(itr * side_len * 3) + (1.5 * side_len),side_len,'black',fill_color1)
            else:
                draw_hexagon((itr2 * d_hex_len) + (d_hex_len / 2),(itr * side_len * 3) + (1.5 * side_len),side_len,'black',fill_color2)
    else:
        for itr2 in range(num_hex): # creating individual hexagons in each row
            if itr2 % 2 == 0:
                draw_hexagon((itr2 * d_hex_len) + (d_hex_len / 2),(itr * side_len * 3) + (1.5 * side_len),side_len,'black',fill_color2)
            else:
                draw_hexagon((itr2 * d_hex_len) + (d_hex_len / 2),(itr * side_len * 3) + (1.5 * side_len),side_len,'black',fill_color1)

done()