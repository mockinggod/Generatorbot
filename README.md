Thank you for your interest in Generatorbot.

This is a discord bot developed to help GMs prepare and run there rpg session by creating randomly generated content. Currently available: Names,, NPCs, Inns, Settlements and more. For now there is only fantasy content.
The philosophy behind this generator is inspired by the tables found in the Forbidden Land rpg.

When an item is generated on a server some of the info will be sent to the same channel, and whoever sends the command might receive a private message with more information such as secrets and details.

The tables are kept in .txt format so that the (even more) laymen can edit them easily

Dependencies:

 * NumPy
 * apscheduler
 * async-timeout
 * discord
 * os
 * psycopg2-binary
 * titlecase

To run your own version you will need to add three files to the repository:
 * Token.txt with your bots discord token number
 * discordid.txt with your discord id
 * serverinfo.txt with the content you would place in psycopg2.connect() for example "user=postgres password=cool host=127.0.0.1 port=5432 dbname=test 
 
You can also place these values as environmental variables: TOKEN, DISCORDID and DATABASE_URL respectively.
 
Current version 0.3.3
 
This is an amateur project, if you have questions or feedback my reddit username is u/mockinggod.
