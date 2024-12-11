import os

from dotenv import load_dotenv


load_dotenv()
id = os.getenv("ID")
password = os.getenv("PASSWORD")
login_url = os.getenv("LOGIN_URL")
note_url = os.getenv("NOTE_URL")
places_1 = [os.getenv(f"PLACE_1_{i}") for i in range(4)]