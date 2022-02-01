# import digitalio
# import busio
# import board
from PIL import Image, ImageDraw, ImageFont, ImageOps
from types import SimpleNamespace
# from adafruit_epd.ssd1680 import Adafruit_SSD1680

# create the spi device and pins we will need
# spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# ecs = digitalio.DigitalInOut(board.CE0)
# dc = digitalio.DigitalInOut(board.D22)
# srcs = None
# rst = digitalio.DigitalInOut(board.D27)
# busy = digitalio.DigitalInOut(board.D17)
# display = Adafruit_SSD1680(122, 250,
#                            spi,
#                            cs_pin=ecs,
#                            dc_pin=dc,
#                            sramcs_pin=srcs,
#                            rst_pin=rst,
#                            busy_pin=busy,
#                            )

# display.rotation = 1

# image = Image.open("blinka.png")

# # Scale the image to the smaller screen dimension
# image_ratio = image.width / image.height
# screen_ratio = display.width / display.height
# if screen_ratio < image_ratio:
#     scaled_width = image.width * display.height // image.height
#     scaled_height = display.height
# else:
#     scaled_width = display.width
#     scaled_height = image.height * display.width // image.width
# image = image.resize((scaled_width, scaled_height), Image.BICUBIC)

# # Crop and center the image
# x = scaled_width // 2 - display.width // 2
# y = scaled_height // 2 - display.height // 2
# image = image.crop((x, y, x + display.width, y +
#                    display.height)).convert("RGB")

# # Convert to Monochrome and Add dithering
# image = image.convert("1").convert("L")

# # Display image.
# display.image(image)
# display.display()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Next define some constants to allow easy resizing of shapes and colors
BORDER = 20
FONTSIZE = 24
BACKGROUND_COLOR = BLACK
FOREGROUND_COLOR = WHITE
TEXT_COLOR = BLACK


display = {
    "width": 122,
    "height": 250,
}
display = SimpleNamespace(**display)

image = Image.new("RGB", (display.width, display.height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box as the background
draw.rectangle((0, 0, display.width - 1, display.height - 1),
               fill=BACKGROUND_COLOR)

# Draw a smaller inner foreground rectangle
draw.rectangle(
    (BORDER, BORDER, display.width - BORDER - 1, display.height - BORDER - 1),
    fill=FOREGROUND_COLOR,
)

# font = ImageFont.truetype(
#     "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)
# mac
# font = ImageFont.truetype(
#     "~/Library/Fonts/FiraCode-Medium.ttf", FONTSIZE)

f = ImageFont.load_default()

# Draw Some Text
text = "Ciao mamma!"

(font_width, font_height) = f.getsize(text)

# with Pilmoji(image) as pilmoji:
draw.text(
    (display.width // 2 - font_width // 2,
        display.height // 2 - font_height // 2),
    # (0,0),
    text,
    font=f,
    fill=TEXT_COLOR,
)
# (font_width, font_height) = f.getsize(text)

# txt = Image.new('L', (display.width, display.height))
# d = ImageDraw.Draw(txt)

# # display the text in the middle
# d.text(((display.width / 2) - (font_width / 2),
#         (display.height / 2) - (font_height / 2)),
#        text, font=f, fill=127)

# # rotate the text
# txt = txt.rotate(90, expand=1)

# image.paste(ImageOps.colorize(w, (0, 0, 0), (255, 255, 84)), (0, 0),  w)

# # drawing text size
# draw.text((5, 5), text, font = font, align ="left")

# mac
image.show()

# display.image(image)
# display.display()
