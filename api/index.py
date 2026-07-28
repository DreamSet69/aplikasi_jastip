import sys
import os

# Menambahkan root directory ke dalam system path agar bisa import dari app.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
