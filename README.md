# FlyingMouse
An implementation of hand-motion detection to control mouse cursors like a weird person

# For people with a life
## Installation
1. Download the latest release
2. Unzip the file
3. Run the handmouse.exe file
4. Use it maybe?

## Known Issues
1. The app cannot be manually close. Please open task manager and close it yourself manually
2. Everyone's hands are different, some people's hand might not work, we are trying to make this application accessible to people with different abilities. #diversity #blessed #love #nohate

## What happens if shit happens?
You have a few options:
1. Snapchat: gabrielma0220
2. Open an issue on the issue page of this website (you need a github account. So you lazy people won't be bothered)
3. If you know me irl, you should have my contacts already or, just ask me irl. 
4. jUsT goOgLe It BrO

# For Nerds Only
## Installation
Installing is straight forward and can easily be built into an executable file built SPECIFICALLY for your own computer.
1. On terminal, run ``` pip install -r requirements.txt```
2. For directly debugging, run handmouse.py 
3. For built version, run this command in your terminal ```python setup.py build```
## Calibration
Hands may not detect properly on first time start. Put both hands in front of your computer and slowly turn both hands until a green frame appears. Note: Prolonged use of the application may reduce accuracy and calibrate when appropiate

## Variables
This mouse uses a threshold variable to control the sensitivity to flickering ratio, which more sensitivity means more flickering, and vise-versa. This is used to smoothen the values. Without such value the computer may not be able to handle high framerate processing and flicke(lowered fps and lag) Keep in mind that this is meant to be tuned by the user and the exe version will be set to laptop default of 6.

## Issues and Pull requests
1. When creating an issue please read all other opened issues. They may help you as you will most likely get an answer more quickly. response time to issues usually take more than a month
2. Pull requests are more than welcome as long they are constructive and clearly described
=======
# Calibration
Hands may not detect properly on first time start. Put both hands in front of your computer and slowly turn both hands until a green frame appears. Note: Prolonged use of the application may reduce accuracy and calibrate when appropiate
# Packaging
This program can be packaged into an exe version. Due to how broken mediapipe can be during packaging, please use handmouse.spec spec file to run pyinstaller such that it can run properly

```pyinstaller --onefile --windowed handmouse.spec```