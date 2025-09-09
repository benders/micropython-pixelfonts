# pixelfont

## Usage

```python
from pixelfonts import Font3x5, Font4x7

# Create a font renderer with your display dimensions and pixel function
font = Font3x5(display_width=16, display_height=8, pixel_func=set_pixel)

# Draw text at a specific position
font.text("123", x_offset=0, y_offset=0, color=(255, 255, 255))

# Draw a single character
font.draw_char("5", x_offset=10, y_offset=2, color=(255, 0, 0))
```

### Integration with Display Libraries

pixelfont works with any display library that provides a pixel-setting function. The pixel function should accept x and y coordinates followed by any additional parameters (like color).

```python
# Example with a generic display library
def set_my_pixel(x, y, color):
    my_display.pixel(x, y, color)

font = Font4x7(128, 64, set_my_pixel)
font.text("0123", 10, 10, (255, 255, 255))
```

## Available Fonts

- **Font3x5**: A compact 3x5 pixel font, for very small displays
- **Font4x7**: A more readable 4x7 pixel font

## Creating Custom Fonts

You can create your own custom fonts by subclassing `BaseFont`:

```python
from pixelfont import BaseFont

class MyCustomFont(BaseFont):
    WIDTH = 5
    HEIGHT = 8
    FONT = {
        "A": [
            "  #  ",
            " # # ",
            "#   #",
            "#####",
            "#   #",
            "#   #",
            "#   #",
            "     "
        ],
        # Add more characters...
    }
```
