# tests/conftest.py
import os
import sys

# añade la carpeta padre de tests (la raíz del proyecto) al inicio de sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)