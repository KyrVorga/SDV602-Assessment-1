# Shadowcrypt

This project is a text-based adventure game built using Python and PySimpleGUI. This was made as an assessment for my software development class while studying a bachelor of information technology.

The game is very simple and straightforward. It involves venturing around a map collecting items in order to defeat the final boss.

The game is complete and in its final state. Anyone who wants to work on it may fork and submit pull requests. This project uses the MIT license.

# Running the game

There are two possible ways to set up and run the game. The simplest is to download the .exe from the releases tab [here](https://github.com/KyrVorga/SDV602-Assessment-1/releases/tag/v1.0.0).

The second way to set up the project is to clone the repository and set up a virtual environment, which I will outline below.

# Installing the project
**Prerequisites:**
It is expected that you have both Git and Python installed before attempting this.

1. Clone the repository onto your machine.
2. Open your preferred terminal and navigate into the cloned repository.
3. Create a generic virtual environment: ```python -m venv venv```
4. Activate the venv:

   Unix: ```source venv/Scripts/activate```
   
   Windows: ```venv\Scripts\activate```
5. Install the projects dependencies: ```pip install -r requirements.txt```.
6. Run Shadowcrypt: ```python Shadowcrypt.py```

# Building an .exe with PyInstaller

For this I will provide the command that I used to produce an .exe.

1. Open a terminal in the project's root directory.

2. Install PyInstaller with PIP, this can be in the project venv or globally.

3. Create the executable with ```pyinstaller --add-data 'images/*;images' --onefile --windowed Shadowcrypt.py```

Once the above is completed you will find a build and dist directories. Inside dist you will find the Shadowcrypt.exe.