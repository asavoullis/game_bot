import pyautogui
import time
import keyboard
import win32api
import win32con


# https://www.youtube.com/watch?v=wCho_BdpdyY

def click(coordinates):
    x, y = coordinates
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print(f"Mouse clicked at position {x}, {y}")

def mouse_click(coordinates):
    x, y = coordinates
    win32api.SetCursorPos((x, y))
    pyautogui.mouseDown()
    time.sleep(0.1)  # Wait for 0.1 seconds
    pyautogui.mouseUp()
    print(f"Mouse clicked at position {x}, {y}")

def key_press(key, coordinates):
    x, y = coordinates
    win32api.SetCursorPos((x, y))
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)
    print(f"{key}, pressed at position {x}, {y}")

def if_color_at_pointer(RGB_COLOR, coordinates):
    x, y = coordinates
    win32api.SetCursorPos((x, y))
    pixel_color = pyautogui.pixel(x, y)

    # Check if each channel (R, G, B) matches the specified color
    if pixel_color != RGB_COLOR:
        print(f"No RGB_COLOR match at {x}, {y}, RGB_COLOR is {pixel_color} (expected {RGB_COLOR})")
        
    else:
        print(f"RGB_COLOR match at {x}, {y}, RGB_COLOR is {pixel_color}")

def check_browser_zoom():
    if pyautogui.locateAllOnScreen('../images/zoom.jpg', confidence=0.8):
        return "Browser Zoom is Correct"
    else:
        return "Error: Browser Zoom is Incorrect"

if __name__ == "__main__":
    first_run = True
    while not keyboard.is_pressed('q'):
        if first_run:
            if check_browser_zoom():
                pass
            else:
                break
        else:
            pass

        # Check for Scientist T3 if available
        coordinates = (1861, 820)
        target_color = (0, 245, 0)
        if_color_at_pointer(target_color, coordinates)
        mouse_click(coordinates)





        # pyautogui.keyDown('1')
    



""" getting coordinates
import pyautogui
pyautogui.displayMousePosition()
"""
