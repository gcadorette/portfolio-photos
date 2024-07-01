import os
from dotenv import load_dotenv

load_dotenv()

def getenv(varname):
    return os.getenv(varname)