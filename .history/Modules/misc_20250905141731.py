import sys
import os

# Zdefiniuj funkcję, która zwraca poprawną ścieżkę do zasobu
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def calculate_path( path ):    
    return resource_path( path )
