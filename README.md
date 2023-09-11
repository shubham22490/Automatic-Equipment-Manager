### Automatic-Equipment-Manager

## Overview
The Machine Controller Application is a graphical user interface (GUI) program built using the Tkinter library for Python. This application allows users to control various machine components, such as a DC Trainer Kit, a Digital Storage Oscilloscope (DSO), and a DC Supply. Users can turn these components on or off and submit their choices to control the machine.

## Features
- User-friendly GUI with a Minty theme.
- Personalized welcome message with the current user's name.
- Control interface for three machine components: DC Trainer Kit, DSO, and DC Supply.
- Radio buttons for each component to select between ON and OFF states.
- Submit button to send the selected component states to the machine.
- Icon representing the application in the window title bar.

## Installation
1. Make sure you have Python installed on your system.
2. Install the required libraries using pip:
   ```
   pip install tkinter ttkbootstrap
   ```
3. Download the application's source code.
4. Ensure that you have the 'square.ico' file in the same directory as the source code, or update the `window.iconbitmap()` line with the correct path to your icon file.
5. Run the application by executing the Python script:
   ```
   python machine_controller.py
   ```

## Usage
1. Launch the Machine Controller Application.
2. The application will display a welcome message with your username.
3. Use the radio buttons to select the desired state (ON or OFF) for each machine component: DC Trainer Kit, DSO, and DC Supply.
4. Click the "SUBMIT" button to send the selected component states to control the machine.

## Notes
- The application uses the `com.sendData()` function to send control commands to the machine. However, this function is currently commented out in the code (`# com.sendData([kit_value.get(), dso_value.get(), supply_value.get()])`). You should uncomment this line and ensure that the `Com` class and related functions are correctly implemented to interface with the machine.

## License
This Machine Controller Application is released under the [MIT License](LICENSE).

## Author
[Your Name]

## Contact Information
If you have any questions or need assistance with this application, please contact [your email address].

**Note:** Make sure to replace `[Your Name]` and `[your email address]` with your actual name and contact information in the README file. Additionally, include any relevant information about your machine control system and how to set up the communication between the application and the machine if needed.
