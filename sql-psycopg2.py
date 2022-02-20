import psycopg2

# connect tp "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# Qeury 2 - select only the "Name" column from the "Artist" table
cursor.execute('SELECT "Name" FROM "Artist"')

# Qeury 3 - select only the "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Qeury 4 - select only the "ArtistId" #51 from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Qeury 5 - select only the "Album" #51 from the "Artist" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Qeury 6 - select only the "Track" #51 from the "Composer" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ['Queen'])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection 
connection.close()

# print results
for result in results:
    print(result)