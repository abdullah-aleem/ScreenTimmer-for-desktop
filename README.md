# ScreenTimmer for Desktop

This project is a Python-based desktop application that records the time spent on each app on your desktop. It consists of a backend program that runs continuously in the background, tracking the active application, and a frontend GUI created using Tkinter that allows you to start and stop the tracking process and view the time spent on each app.

## Features

- Records the time spent on each application running on your desktop.
- Provides a user-friendly GUI for starting and stopping the tracking process.
- Displays the time spent on each app in a clear and organized manner.
- Works on Windows, macOS, and Linux operating systems.

## Prerequisites

- Python 3.7 or above installed on your system.
- The following Python packages need to be installed:
    - `psutil` - Used to retrieve running processes and their information.
    - `tkinter` - Used for creating the graphical user interface.

You can install the required packages using the following command:
pip install psutil pandas tkinter

## Usage

1. Clone the repository to your local machine:

git clone https://github.com/abdullah-aleem/ScreenTimmer-for-desktop.git

2. Change into the project directory:

3. Start the application by running the `main.py` script:
 python main.py
4. The application window will appear, showing a "Start" button and a table displaying the time spent on each app.

5. Click the "Start" button to begin tracking the time spent on each app. The program will start running in the background.

6. As you switch between different applications on your desktop, the backend program will record the time spent on each app.

7. To stop the tracking process, click the "Stop" button in the application window. The recorded data will be saved to a JSON file.

8. You can view the recorded data by examining the generated json file in the project directory.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/your-username/desktop-app-time-tracker). 

When contributing code, please ensure that you follow the existing code style and submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was inspired by the need to track time spent on different applications for productivity purposes. Special thanks to the contributors of the `psutil`, `pandas`, and `tkinter` libraries for providing the necessary tools to build this application.
