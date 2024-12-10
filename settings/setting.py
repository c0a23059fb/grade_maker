import os

from dotenv import load_dotenv


load_dotenv()
id = os.getenv("ID")
password = os.getenv("PASSWORD")
login_url = os.getenv("LOGIN_URL")
note_url = os.getenv("NOTE_URL")
xpaths = [os.getenv(i) for i in ["ABSENCE_XPATH", "MOTIVATION_XPATH", "UNDERSTAND_XPATH", "MANNER_XPATH"]]
