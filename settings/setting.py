import os

from dotenv import load_dotenv


load_dotenv()
id = os.getenv("ID")
password = os.getenv("PASSWORD")
login_url = os.getenv("LOGIN_URL")
note_url = os.getenv("NOTE_URL")

courses = os.getenv("COURSES").split()
places = {k: os.getenv(f"PLACE_{i}").split() for i, k in enumerate(os.getenv("PLACES").split())}