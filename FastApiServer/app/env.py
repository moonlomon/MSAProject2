import pymysql
from sqlalchemy import create_engine

USERNAME = "mydb"
PASSWORD = "rootroot"
HOSTNAME = "mydb.cuaqdrne6onj.ap-northeast-2.rds.amazonaws.com" # "localhost"
DATABASE = "mydb"
PORT = 3306
CHARSET = "utf8mb4"
DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}"
engine = create_engine(DB_URL, encoding="utf-8", echo=True)

conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)