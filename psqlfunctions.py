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
		print(record)
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