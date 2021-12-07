import sqlalchemy as db
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

# Connect to db
engine = db.create_engine("sqlite:///movies.db")
connection = engine.connect()

metadata = db.MetaData()


movies = db.Table("Movies", metadata, autoload=True, autoload_with=engine)

# Insert a new entry
query_obj = movies.insert().values(Title="Psycho", Director="Alfred Hitchcock", Year=1960)
connection.execute(query_obj)

query = db.select([movies])
query_by_director = db.select([movies]).where(movies.columns.Director == "Julito Chulito")

result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

result_proxy2 = connection.execute(query_by_director)
result_set2 = result_proxy2.fetchall()

print(result_set[0])
pp.pprint(result_set)

pp.pprint(result_set2)
