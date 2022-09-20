from config import BOT_USERNAME, OWNER
from db_helper import DBHelper

db = DBHelper()
titles = db.get_tables()
