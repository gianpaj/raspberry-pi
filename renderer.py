from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from adafruit_epd.epd import Adafruit_EPD

DejaVuSans = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DejaVuSans_Bold = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

small_font = ImageFont.truetype(DejaVuSans_Bold, 16)
medium_font = ImageFont.truetype(DejaVuSans, 20)
large_font = ImageFont.truetype(DejaVuSans_Bold, 24)

# RGB Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Renderer:
    """
    renders the graphics on the e-ink display
    """

    def __init__(self, display, *, am_pm=True, celsius=True):
        self.am_pm = am_pm
        self.celsius = celsius

        self.small_font = small_font
        self.medium_font = medium_font
        self.large_font = large_font

        self.display = display

        self._weather_icon = None
        self._city_name = None
        self._main_text = None
        self._temperature = None
        self._description = None
        self._time_text = None

    def update_time(self):
        now = datetime.now()
        self._time_text = now.strftime(
            "%I:%M:%S %p").lstrip("0").replace(" 0", " ")
        self.update_display()

    def update_display(self):
        self.display.fill(Adafruit_EPD.WHITE)
        image = Image.new("RGB", (self.display.width,
                          self.display.height), color=WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the time
        (font_width, font_height) = medium_font.getsize(self._time_text)
        draw.text(
            (5, font_height * 2 - 5),
            self._time_text,
            font=self.medium_font,
            fill=BLACK,
        )
        self.display.image(image)
        self.display.display()
