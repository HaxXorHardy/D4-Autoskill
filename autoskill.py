import cv2
import numpy as np
import pyautogui
import pyscreenshot as ImageGrab
import json
import time
import ctypes

TARGET_PID = 4388

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def find_image_on_screen(template, threshold=0.9):
    screenshot = ImageGrab.grab()
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc
    return None

def is_target_window_active():
    GetForegroundWindow = ctypes.windll.user32.GetForegroundWindow
    GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId

    hwnd = GetForegroundWindow()
    pid = ctypes.wintypes.DWORD()
    GetWindowThreadProcessId(hwnd, ctypes.pointer(pid))
    return pid.value == TARGET_PID

def main():
    config = load_config()

    while True:
        if not is_target_window_active():
            print("Target window is not active")
            time.sleep(1)
            continue

        match_found = False
        for match in config["matches"]:
            if not match["enabled"]:
                continue

            image = cv2.imread(match["image"], cv2.IMREAD_COLOR)
            if find_image_on_screen(image) is not None:
                match_found = True
                print(f"Match found for {match['image']}, pressing key {match['key']}")
                pyautogui.press(match["key"])

        if not match_found:
            print("No match found")

        time.sleep(0.1)

if __name__ == "__main__":
    main()
