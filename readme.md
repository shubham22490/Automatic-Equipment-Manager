# Machine Controller Application

## Introduction

The Machine Controller Application is a Python-based program designed to interface with a Raspberry Pi for machine control and monitoring. This application utilizes the Tkinter GUI library for the user interface and includes functionality for communication with external devices via serial communication. The code also establishes a secure connection to a MySQL database through SSH tunneling for data storage and retrieval.

## Features

- **Database Connectivity:** The application connects to a MySQL database using SSH tunneling for secure communication. The database is used to store timestamped records of user actions and machine states.

- **Serial Communication:** Communication with an external device, presumably a Raspberry Pi, is established through a serial connection. The application can send and receive data to control and monitor the connected machine.

- **Graphical User Interface (GUI):** The Tkinter library is employed to create a graphical user interface for users to interact with the application. The GUI provides an intuitive platform for controlling the machine and viewing its status.

- **Real-time Data Display:** The application retrieves real-time data from the connected device and displays it in the GUI. This can include information such as temperature, status, and other relevant parameters.

## Components

### 1. **DB Class (Database Handling)**
   - Manages the connection to the MySQL database through SSH tunneling.
   - Provides methods for checking the database connection status and inserting data into the database.

### 2. **Com Class (Communication with Raspberry Pi)**
   - Handles communication with an external device (presumably a Raspberry Pi) through a serial connection.
   - Includes methods for sending and receiving data to and from the connected device.

### 3. **App Class (Graphical User Interface)**
   - Utilizes Tkinter to create a windowed application with a specific theme (default is 'minty').
   - Implements features such as window sizing, positioning, and an icon.
   - Integrates components for database handling and communication with the Raspberry Pi.

### 4. **Main Application Logic**
   - The application logic includes functionalities such as data processing, user input handling, and updating the GUI in real-time based on received data.

## Dependencies

- **Tkinter:** GUI library for creating the graphical user interface.
- **ttkbootstrap:** Theme library for enhancing the appearance of Tkinter widgets.
- **pytz:** Library for dealing with time zones.
- **serial:** Library for serial communication.
- **pymysql:** MySQL database connector.
- **sshtunnel:** Library for creating and managing SSH tunnels.
- **socket:** Provides access to socket operations.
- **datetime:** Module for working with dates and times.

## Usage

1. **Install Dependencies:**
   - Ensure all required libraries are installed using `pip install -r requirements.txt`.

2. **Run the Application:**
   - Execute the script using `python main.py`.
   - The application window will appear, providing controls for machine operations and displaying real-time data.

3. **Interact with the GUI:**
   - Use the GUI controls to send commands to the connected machine.
   - Monitor the real-time data displayed on the GUI for machine status.

## Notes

- Ensure that the correct serial port is specified in the `Com` class constructor.
- Modify the database and SSH connection details in the `DB` class according to your setup.

## Disclaimer

This application is designed as a starting point and may need customization based on specific machine requirements and hardware configurations. Ensure that you have the necessary permissions and credentials for database access and SSH tunneling.

**Note:** The provided code snippet may not include the complete code. Consider obtaining the full source code for the complete application.