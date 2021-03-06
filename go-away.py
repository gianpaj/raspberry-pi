import digitalio
import busio
import board
from adafruit_epd.epd import Adafruit_EPD
from adafruit_epd.ssd1680 import Adafruit_SSD1680

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)
srcs = None

display = Adafruit_SSD1680(122, 250, spi, cs_pin=ecs, dc_pin=dc, sramcs_pin=srcs,
                           rst_pin=rst, busy_pin=busy)

# display.fill(Adafruit_EPD.WHITE)

# display.fill_rect(0, 0, 50, 60, Adafruit_EPD.BLACK)
# display.hline(80, 30, 60, Adafruit_EPD.BLACK)
# display.vline(80, 30, 60, Adafruit_EPD.BLACK)

# display.display()

# up_button = digitalio.DigitalInOut(board.D5)
# up_button.switch_to_input()
# down_button = digitalio.DigitalInOut(board.D6)
# down_button.switch_to_input()

# if not up_button.value:
#     print("Top left button is pressed")

# if not down_button.value:
#     print("Botton left button is pressed")


# clear the buffer
print("Clear buffer")
display.fill(Adafruit_EPD.WHITE)
display.pixel(10, 100, Adafruit_EPD.BLACK)

print("Draw Rectangles")
display.fill_rect(5, 5, 10, 10, Adafruit_EPD.RED)
display.rect(0, 0, 20, 30, Adafruit_EPD.BLACK)

print("Draw lines")
display.line(0, 0, display.width-1, display.height-1, Adafruit_EPD.BLACK)
display.line(0, display.height-1, display.width-1, 0, Adafruit_EPD.RED)

print("Draw text")
display.text('hello world', 25, 10, Adafruit_EPD.BLACK)
display.display()
