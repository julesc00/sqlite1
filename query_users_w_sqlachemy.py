import sqlalchemy as db
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=3)

# Create or connect to db
engine = db.create_engine("sqlite:///users2.db")
connection = engine.connect()

metadata = db.MetaData()

# Create users table
users_table = db.Table(
    "Users",
    metadata,
    db.Column("users_id", db.Integer, primary_key=True),
    db.Column("first_name", db.Text),
    db.Column("last_name", db.Text),
    db.Column("email", db.Text)
)
metadata.create_all(engine)

# Insert entries.
# insertion_query = users_table.insert().values([
#     {"first_name": "Cari", "last_name": "Briones", "email": "cari@chulis.mx"},
#     {"first_name": "Franzche", "last_name": "Briones", "email": "punky@chulis.mx"},
#     {"first_name": "Brigitte", "last_name": "Briones", "email": "gigitte@chulis.mx"},
#     {"first_name": "Michele", "last_name": "Briones", "email": "chenis@chulis.mx"},
#     {"first_name": "Jemima", "last_name": "Briones", "email": "jemi@chulis.mx"}
# ])

users = db.Table("Users", metadata, autoload=True, autoload_with=engine)

query = db.select([users])
query_emails = db.select([users.columns.email])

result_proxy = connection.execute(query_emails)
result_set = result_proxy.fetchall()

pp.pprint(result_set)
