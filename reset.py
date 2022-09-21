import time
from datetime import datetime

from db_helper import DBHelper

db = DBHelper()


def reset():
    db.del_all_users_name()


while True:
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    if hour == 0 and minute == 0:
        reset()
        time.sleep(60)
    time.sleep(1)
