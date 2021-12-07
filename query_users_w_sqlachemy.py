import sqlalchemy as db
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3)

# Connect to db
engine = db.create_engine("sqlite:///movies.db")
connection = engine.connect()

metadata = db.MetaData()

users = db.Table("Users", metadata, autoload=True, autoload_with=engine)

query = db.select([users])
query_emails = db.select([users.columns.Email])

result_proxy = connection.execute(query_emails)
result_set = result_proxy.fetchall()

pp.pprint(result_set)
