import os
from dotenv import load_dotenv

load_dotenv(override=True)
USERNAME=os.getenv('username')
PASSWORD=os.getenv('password')
PORT=os.getenv('port')