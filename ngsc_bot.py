import time
import win32api
import win32con
import pyautogui
import keyboard

# https://www.youtube.com/watch?v=wCho_BdpdyY

class MouseController:
    """
    A class for controlling mouse actions.

    Attributes:
        None 

    Methods:
        click(coordinates): Simulates a mouse click at the specified coordinates.
        mouse_click(coordinates): Simulates a mouse click using pyautogui.
        key_press(key, coordinates): Simulates a key press at the specified coordinates.
        if_color_at_pointer(RGB_COLOR, coordinates): Checks if the pixel color at the given coordinates matches the expected color.
        check_browser_zoom(): Checks if the browser zoom level is approximately 50%.
    """

    def __init__(self):
        # no initialization logic needed yet
        pass  

    def click(self, coordinates):
        """
        Simulates a mouse click at the specified coordinates.

        Args:
            coordinates (tuple): (x, y) position of the click.

        Returns:
            None
        """
        x, y = coordinates
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        print(f"Mouse clicked at position {x}, {y}")

    def mouse_click(self, coordinates):
        """
        Simulates a mouse click using pyautogui.

        Args:
            coordinates (tuple): (x, y) position of the click.

        Returns:
            None
        """
        x, y = coordinates
        win32api.SetCursorPos((x, y))
        pyautogui.mouseDown()
        time.sleep(0.1)  # Wait for 0.1 seconds
        pyautogui.mouseUp()
        print(f"Mouse clicked at position {x}, {y}")

    def key_press(self, key, coordinates):
        """
        Simulates a key press at the specified coordinates.

        Args:
            key (str): Key to press (e.g., 'a', 'ctrl', 'shift').
            coordinates (tuple): (x, y) position for the key press.

        Returns:
            None
        """
        x, y = coordinates
        win32api.SetCursorPos((x, y))
        pyautogui.keyDown(key)
        time.sleep(0.1)
        pyautogui.keyUp(key)
        print(f"{key}, pressed at position {x}, {y}")

    def if_color_at_pointer(self, RGB_COLOR, coordinates):
        """
        Checks if the pixel color at the given coordinates matches the expected color.

        Args:
            RGB_COLOR (tuple): Expected RGB color (e.g., (255, 0, 0) for red).
            coordinates (tuple): (x, y) position to check.

        Returns:
            None
        """
        x, y = coordinates
        win32api.SetCursorPos((x, y))
        pixel_color = pyautogui.pixel(x, y)

        if pixel_color != RGB_COLOR:
            print(f"No RGB_COLOR match at {x}, {y}, RGB_COLOR is {pixel_color} (expected {RGB_COLOR})")
        else:
            print(f"RGB_COLOR match at {x}, {y}, RGB_COLOR is {pixel_color}")

    def check_browser_zoom(self):
        """
        Checks if the browser zoom level is approximately 50%.

        Returns:
            bool: True if zoom is approximately 50%, False otherwise.
        """
        if pyautogui.locateAllOnScreen('../images/zoom.jpg', confidence=0.8):
            return True
        else:
            return False

if __name__ == "__main__":
    mouse_controller = MouseController()
    
    while not keyboard.is_pressed('q'):
        if not mouse_controller.check_browser_zoom():
            continue

        # Check for Scientist T3 if available
        scientist_coordinates = (1861, 820)
        scientist_color = (0, 245, 0)
        mouse_controller.if_color_at_pointer(scientist_color, scientist_coordinates)
        mouse_controller.mouse_click(scientist_coordinates)





""" getting coordinates
import pyautogui
pyautogui.displayMousePosition()

pyautogui.keyDown('1')
"""
