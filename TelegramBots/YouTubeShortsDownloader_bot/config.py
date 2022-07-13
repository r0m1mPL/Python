from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent

API_TOKEN = os.getenv("API_TOKEN", '')
