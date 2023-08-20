pyinstaller --add-data 'images/forest.png;images' --add-data 'images/forest_circle.png;images' --add-data 'images/frog.png;images' --onefile --windowed Shadowcrypt.py
pyinstaller --add-data 'images/*;images' --onefile --windowed Shadowcrypt.py
