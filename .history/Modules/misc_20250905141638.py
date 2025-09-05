import sys
import os

# Zdefiniuj funkcję, która zwraca poprawną ścieżkę do zasobu
def resource_path(relative_path):
    """ Get the absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def calculate_path( path ):
    
    return resource_path( path )

print( calculate_path("Icons/24x24/Database-Tick-24x24.png") )


# Użyj funkcji w swoim kodzie do wczytania obrazka
# Pamiętaj, że ścieżka do pliku graficznego jest teraz względna do miejsca, w którym PyInstaller go umieścił, czyli "grafiki/ikony/menu_ikona.png"
# image_path = resource_path(os.path.join("grafiki", "ikony", "menu_ikona.png"))
