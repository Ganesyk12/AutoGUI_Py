# PyAutoGUI

<p align="center">
<img  src="https://www.python.org/static/community_logos/python-logo.png"  alt="Python Logo"  width="250">
</p>

PyAutoGUI is a Python library that allows you to automate interactions with your computer's graphical user interface (GUI). With PyAutoGUI, you can program actions such as moving the mouse, clicking buttons, typing text, and more, making it useful for automating routine tasks that typically require manual interaction with applications.
> _See <a href="https://pyautogui.readthedocs.io/en/latest/">Documentation_
</a>

## Key Features

1. **Mouse Control**:
   - **Moving the Mouse**: You can move the mouse cursor to a specific position on the screen.
   - **Clicking**: PyAutoGUI supports various types of clicks (left click, right click, double click).
   - **Dragging and Dropping**: You can move the mouse while holding down a button to drag and drop objects.

2. **Keyboard Control**:
   - **Typing Text**: You can automate typing text into any application.
   - **Pressing Keys**: You can simulate key presses or key combinations (e.g., Ctrl+C).

3. **Taking Screenshots**:
   - **Screenshot**: PyAutoGUI can take screenshots of the entire screen or a specific area.
   - **Image Matching**: You can search for a small image within a screenshot to find the location of specific UI elements.

4. **Timing Control**:
   - **Delays**: You can add time delays between actions to simulate more realistic human interactions.
 
 
## Required Libraries

|	Library		|	Version	|
|---------------|-----------|
| PyAutoGUI 	|	0.9.54	| 

## Example Usage

- ### Moving and Clicking the Mouse
```python
import pyautogui

# Move the mouse to coordinates (100, 100)
pyautogui.moveTo(100, 100, duration=1)  # Move in 1 second

# Left click at the current position
pyautogui.click()

```
## Thanks For Supporting


> Author : <a href="https://github.com/Ganesyk12">Ganes Yudha Kusuma</a>
> _Copyright : @2024_