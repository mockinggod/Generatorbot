import psycopg2

def addprefix(serverinfo, guildid, prefix):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		postgres_insert_query = """ INSERT INTO prefixes (ID, prefix) VALUES (%s,%s)"""
		record_to_insert = (guildid, prefix)
		cursor.execute(postgres_insert_query, record_to_insert)

		connection.commit()
		count = cursor.rowcount
		print (count, "Record inserted successfully into prefix table")

	except (Exception, psycopg2.Error) as error :
		if(connection):
			print("Failed to insert record into prefix table", error)

	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			
def updateprefix(serverinfo, guildid, prefix):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		# Update single record now
		sql_update_query = """Update prefixes set prefix = %s where ID = %s"""
		cursor.execute(sql_update_query, (prefix, guildid))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record Updated successfully ")


	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			
def readprefixes(serverinfo):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		sql_select_query = """select * from prefixes"""
		cursor.execute(sql_select_query)
		record = cursor.fetchall()
		return(record)

	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

			
def removeprefix(serverinfo, guildid):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		# Update single record now
		sql_delete_query = """Delete from prefixes where ID = %s"""
		cursor.execute(sql_delete_query, (guildid, ))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record deleted successfully ")

	except (Exception, psycopg2.Error) as error:
		print("Error in Delete operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

			
def addrace(serverinfo, userid, genre, race):
	try:
		connection = psycopg2.connect(serverinfo)
		

		cursor = connection.cursor()

		postgres_insert_query = """ INSERT INTO races (ID, genre, racename, gender, weight, names, surnames, maxsettlement, occupation1, occupation2, occupation3, occupation4, occupation5, occupation6, occupation7, occupation8, occupation9, occupation10, occupation11) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		record_to_insert = (userid, genre, race[0], race[1], race[2], race[3], race[4], race[5], race[6][0], race[6][1], race[6][2], race[6][3], race[6][4], race[6][5], race[6][6], race[6][7], race[6][8], race[6][9], race[6][10])
		
		cursor.execute(postgres_insert_query, record_to_insert)

		connection.commit()
		count = cursor.rowcount
		print (count, "Record inserted successfully into races table")

	except (Exception, psycopg2.Error) as error :
		if(connection):
			print("Failed to insert record into races table", error)

	finally:
		#closing database connection.
		if(connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			
			
def readraces(serverinfo, userid, genre):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()
		
		if genre == 'all':
			sql_select_query = """select * from races where ID = %s"""
			record_to_select = ([userid])
		else:
			sql_select_query = """select * from races where ID = %s and genre = %s"""
			record_to_select = (userid, genre)
		cursor.execute(sql_select_query, record_to_select)
		record = cursor.fetchall()
		count = cursor.rowcount
		return(count, record)

	except (Exception, psycopg2.Error) as error:
		print("Error in update operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")

			
def removerace(serverinfo, userid, genre, racename):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		# Update single record now
		sql_delete_query = """Delete from races where ID = %s and genre = %s and racename = %s"""
		cursor.execute(sql_delete_query, (userid, genre, racename))
		count = cursor.rowcount
		connection.commit()
		
		print(count, "Record deleted successfully ")
		
		return(count)

	except (Exception, psycopg2.Error) as error:
		print("Error in Delete operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")
			
def removeracegenre(serverinfo, userid, genre):
	try:
		connection = psycopg2.connect(serverinfo)

		cursor = connection.cursor()

		# Update single record now
		sql_delete_query = """Delete from races where ID = %s and genre = %s"""
		cursor.execute(sql_delete_query, (userid, genre))
		connection.commit()
		count = cursor.rowcount
		print(count, "Record deleted successfully ")
		
		return(count)

	except (Exception, psycopg2.Error) as error:
		print("Error in Delete operation", error)

	finally:
		# closing database connection.
		if (connection):
			cursor.close()
			connection.close()
			print("PostgreSQL connection is closed")