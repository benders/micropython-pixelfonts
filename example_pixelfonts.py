#!/usr/bin/env micropython
"""
Example usage of the pixelfont package.
"""

import time
from pixelfonts import Font3x5, Font4x7

try:
    # Try to import PixelKit for demonstration
    import PixelKit as kit
    has_pixelkit = True
except ImportError:
    # Mock PixelKit for demonstration if it's not available
    has_pixelkit = False
    
    class MockPixelKit:
        def __init__(self):
            self.display = [[' ' for _ in range(16)] for _ in range(8)]
            
        def set_pixel(self, x, y, color):
            if 0 <= x < 16 and 0 <= y < 8:
                self.display[y][x] = '█'  # Use a block character to represent a lit pixel
                
        def clear(self):
            self.display = [[' ' for _ in range(16)] for _ in range(8)]
            
        def render(self):
            print("\n" + "-" * 18)  # Display border
            for row in self.display:
                print("|" + ''.join(row) + "|")
            print("-" * 18)
    
    kit = MockPixelKit()

def demo_font3x5():
    """Demo the 3x5 font"""
    COLOR = (0x10, 0x10, 0x10)  # Color doesn't matter for mock display
    DISPLAY_WIDTH = 16
    DISPLAY_HEIGHT = 8
    
    font = Font3x5(DISPLAY_WIDTH, DISPLAY_HEIGHT, kit.set_pixel)
    
    kit.clear()
    font.text("3579", 0, 1, COLOR)  # Slight Y offset for better viewing
    kit.render()
    time.sleep(2)

def demo_font4x7():
    """Demo the 4x7 font"""
    COLOR = (0x10, 0x10, 0x10)  # Color doesn't matter for mock display
    DISPLAY_WIDTH = 16
    DISPLAY_HEIGHT = 8
    
    font = Font4x7(DISPLAY_WIDTH, DISPLAY_HEIGHT, kit.set_pixel)
    
    kit.clear()
    font.text("2468", 0, 0, COLOR)
    kit.render()
    time.sleep(2)

def demo_scrolling():
    """Demo scrolling text with the 3x5 font"""
    COLOR = (0x10, 0x10, 0x10)  # Color doesn't matter for mock display
    DISPLAY_WIDTH = 16
    DISPLAY_HEIGHT = 8
    SCROLL_TEXT = "0123456789"
    SCROLL_SPEED = 0.2  # seconds between updates
    
    font = Font4x7(DISPLAY_WIDTH, DISPLAY_HEIGHT, kit.set_pixel)
    
    # Calculate the total width of the text
    text_width = len(SCROLL_TEXT) * (font.WIDTH + 1) - 1
    
    try:
        # Do a brief scrolling demo (limited iterations for the example)
        position = DISPLAY_WIDTH
        for _ in range(40):  # Scroll for a limited number of frames
            kit.clear()
            font.text(SCROLL_TEXT, position, 1, COLOR)  # Slight Y offset for better viewing
            kit.render()
            position -= 1
            if position < -text_width:
                position = DISPLAY_WIDTH
            time.sleep(SCROLL_SPEED)
    except KeyboardInterrupt:
        print("Scrolling stopped")

if __name__ == "__main__":
    print("pixelfont Package Demo")
    print("======================")
    
    if not has_pixelkit:
        print("PixelKit not found, using text-based display simulation")
    
    print("\nDemo Font3x5:")
    demo_font3x5()
    
    print("\nDemo Font4x7:")
    demo_font4x7()
    
    print("\nDemo scrolling text (press Ctrl+C to stop):")
    demo_scrolling()
    
    print("\nDemo complete!")