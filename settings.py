import os
from dotenv import load_dotenv


load_dotenv()

IP_ADDRESS = os.getenv('IP_ADDRESS')
PORT = os.getenv('PORT')
