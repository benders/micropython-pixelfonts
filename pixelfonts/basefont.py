#!/usr/bin/env python3
"""
BaseFont class for bitmap fonts.
This is the parent class for all bitmap font implementations.
"""

class BaseFont:
    """Base class for bitmap fonts"""
    
    WIDTH = 0  # Width will be defined in subclasses
    HEIGHT = 0  # Height will be defined in subclasses
    FONT = {}   # Font dictionary will be defined in subclasses
    
    def __init__(self, region_width, region_height, pixel_func):
        """
        Initialize a bitmap font renderer.
        
        Args:
            region_width (int): Width of the display region in pixels
            region_height (int): Height of the display region in pixels
            pixel_func (function): Function to call for drawing pixels (x, y, *args, **kwargs)
        """
        self.region_width = region_width
        self.region_height = region_height
        self.pixel_func = pixel_func
    
    def _safe_pixel(self, x, y, *args, **kwargs):
        """
        Draw a pixel only if it's within the display region.
        
        Args:
            x (int): X coordinate
            y (int): Y coordinate
            *args: Additional arguments to pass to pixel_func
            **kwargs: Additional keyword arguments to pass to pixel_func
        """
        if 0 <= x < self.region_width and 0 <= y < self.region_height:
            self.pixel_func(x, y, *args, **kwargs)
    
    def draw_char(self, char, x_offset, y_offset, *args, **kwargs):
        """
        Draw a character at the specified position.
        
        Args:
            char (str): The character to draw
            x_offset (int): X position to start drawing
            y_offset (int): Y position to start drawing
            *args: Additional arguments to pass to pixel_func
            **kwargs: Additional keyword arguments to pass to pixel_func
            
        Raises:
            ValueError: If the character is not in the font
        """
        if char not in self.FONT:
            raise ValueError(f"Character '{char}' not found in font.")
        
        # Skip drawing if character is completely outside the display region
        if x_offset + self.WIDTH < 0 or y_offset + self.HEIGHT < 0:
            return
        elif x_offset >= self.region_width or y_offset >= self.region_height:
            return
        
        for y, row in enumerate(self.FONT[char]):
            for x, col in enumerate(row):
                if col == '#':
                    self._safe_pixel(x + x_offset, y + y_offset, *args, **kwargs)
    
    def text(self, string, x_offset, y_offset, *args, **kwargs):
        """
        Draw a string of text at the specified position.
        
        Args:
            string (str): The text to draw
            x_offset (int): X position to start drawing
            y_offset (int): Y position to start drawing
            *args: Additional arguments to pass to pixel_func
            **kwargs: Additional keyword arguments to pass to pixel_func
        """
        for i, char in enumerate(string):
            self.draw_char(char, x_offset + i * (self.WIDTH + 1), y_offset, *args, **kwargs)