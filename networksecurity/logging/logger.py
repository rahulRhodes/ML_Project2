import logging
import os
from  datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)



# For BasicConfig
# Sets the log file or output
# If you pass filename=..., logs go into that file.
# If you don’t pass a file, logs are printed to the console (stdout).
# Sets the log format
# The format=... string defines how each log line looks.

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)
