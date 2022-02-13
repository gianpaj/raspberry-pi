from datetime import datetime
import time
import digitalio
import busio
import board
# from PIL import Image, ImageDraw, ImageFont
# from pilmoji import Pilmoji
from adafruit_epd.ssd1680 import Adafruit_SSD1680

from renderer import Renderer

# create the spi device and pins we will need
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
ecs = digitalio.DigitalInOut(board.CE0)
dc = digitalio.DigitalInOut(board.D22)
rst = digitalio.DigitalInOut(board.D27)
busy = digitalio.DigitalInOut(board.D17)


# Initialize the Display
display = Adafruit_SSD1680(122, 250,
                           spi,
                           cs_pin=ecs,
                           dc_pin=dc,
                           sramcs_pin=None,
                           rst_pin=rst,
                           busy_pin=busy,
                           )

display.rotation = 1

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

WHITE = (0xFF, 0xFF, 0xFF)
BLACK = (0x00, 0x00, 0x00)
RED = (0xFF, 0x00, 0x00)

# Next define some constants to allow easy resizing of shapes and colors
BORDER = 20
FONTSIZE = 24
BACKGROUND_COLOR = BLACK
FOREGROUND_COLOR = WHITE
TEXT_COLOR = BLACK

# image = Image.new("RGB", (display.width, display.height))

# # Get drawing object to draw on image
# draw = ImageDraw.Draw(image)

# # Draw a black filled box as the background
# draw.rectangle((0, 0, display.width - 1, display.height - 1),
#                fill=BACKGROUND_COLOR)

# # Draw a smaller inner foreground rectangle
# draw.rectangle(
#     (BORDER, BORDER, display.width - BORDER - 1, display.height - BORDER - 1),
#     fill=FOREGROUND_COLOR,
# )

# font = ImageFont.truetype(
#     "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE)


gfx = Renderer(display)

# Draw Some Text
# text = "Ciao mamma!"

# (font_width, font_height) = font.getsize(text)

# with Pilmoji(image) as pilmoji:
# draw.text(
#     (display.width // 2 - font_width // 2,
#         display.height // 2 - font_height // 2),
#     # (0,0),
#     text,
#     font=font,
#     fill=TEXT_COLOR,
# )

# display.image(image)
# display.display()

# gfx.update_time()

# Check for new/deleted events every 10 seconds
QUERY_DELAY = 10  # Time in seconds to delay between querying the Google Calendar API


def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


last_check = None
current_time = get_current_time()

while True:
    # last_event_id = current_event_id
    last_time = current_time

    if last_check is None or time.monotonic() >= last_check + QUERY_DELAY:
        # Call the Calendar API
        # now = datetime.utcnow().isoformat() + "Z"
        # calendar_ids = get_all_calendar_ids()
        # events = []
        # for calendar_id in calendar_ids:
        #     events += get_events(calendar_id)

        # Sort Events by Start Time
        # events = sorted(
        #     events, key=lambda k: k["start"].get("dateTime", k["start"].get("date"))
        # )
        last_check = time.monotonic()

        # Update the current time
        current_time = get_current_time()

        gfx.update_time()

    # if not events:
    #     current_event_id = None
    #     current_index = None
