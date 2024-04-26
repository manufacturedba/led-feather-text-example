import board
import busio as io
import adafruit_ht16k33.matrix
from adafruit_bitmap_font import bitmap_font
from displayio import Bitmap

i2c = io.I2C(board.SCL, board.SDA)

matrix = adafruit_ht16k33.matrix.Matrix16x8(i2c)

font = bitmap_font.load_font("tom-thumb.bdf", Bitmap)

def print_char(matrix, char, x, y):
    glyph = font.get_glyph(ord(char))
    for i in range(glyph.width):
        for j in range(glyph.height):
            pos = glyph.height - j
            if glyph.bitmap[i, j] == 1:
                matrix[x + i, y + pos] = 1

def print_string(matrix, string, x, y):
    for i, char in enumerate(string):
        print_char(matrix, char, x + i * 4, y)

while True:
    matrix.fill(0)
    print_string(matrix, "Hello world", 0, 0)