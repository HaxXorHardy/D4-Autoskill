# Diablo IV AutoSkill

Diablo IV AutoSkill is a Python script that automatically presses keys based on image matches on the screen. 

It uses OpenCV for image recognition and the pyautogui and keyboard libraries for key presses.

## Requirements

- Python 3.7 or higher
- OpenCV
- pyautogui
- keyboard
- colorama
- numpy

## Installation

1. Install the required Python libraries:

```bash
pip install opencv-python-headless pyautogui keyboard colorama numpy
```

## Usage
- Add your images to the images/ directory and update the config.json file with the image file names, keys to press, and optionally the "ignore" flag.
- **Run the script:** python autoskill.py
- The script will continuously monitor the screen and press the corresponding key when an image match is found.
- To stop the script, press CTRL+C in the terminal.

## Customization
- To use different image file formats, update the image paths in the config.json file accordingly.
- To adjust the matching threshold, modify the threshold parameter in the find_image_on_screen function in the autoskill.py script.
- To adjust the key press duration, modify the time.sleep value between keyboard.press(key) and keyboard.release(key) in the main function in the autoskill.py script.
