import logging
import os

#create a logger string
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_folder = "logs"
log_file = "logs/running_log.log"

os.makedirs(log_folder, exist_ok=True)