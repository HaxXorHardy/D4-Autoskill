import json
import time
import cv2
import numpy as np
import pyautogui
import keyboard
from colorama import init, Fore

init(autoreset=True)

def load_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def find_image_on_screen(image_path, threshold=0.5):
    screen = pyautogui.screenshot()
    screen_np = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(screen_np, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return len(loc[0]) > 0

def main():
    config = load_config("config.json")
    last_state = {match["image"]: False for match in config["matches"]}

    while True:
        for match in config["matches"]:
            if match.get("ignore", False):
                continue

            image_path = match["image"]
            key = match["key"]
            found = find_image_on_screen(image_path)

            if not last_state[image_path] and found:
                print(f"{Fore.GREEN}Casting Skill, Pressing Key {key}")
                keyboard.press(key)
                time.sleep(0.1)  # Add a small delay between press and release
                keyboard.release(key)
            else:
                print(f"{Fore.YELLOW}Waiting for cooldown.")

            last_state[image_path] = found

        time.sleep(0.1)


if __name__ == "__main__":
    main()
