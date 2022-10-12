#!/usr/bin/python3

def create_corners(width):
    return 2*("#"+width*"-")+"#"+"\n"

def create_central(width):
    return 2*("|"+width*" ")+"|"+"\n"

def create_grid(squares, width, height):
    return squares*(create_corners(width)+height*create_central(width))+create_corners(width)

print(create_grid(5, 8, 1))