import sqlite3
with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS posts(title TEXT, description TEXT)""")
   # c.execute('INSERT INTO posts VALUES("Helb", "Mama,I know this may find you in your sober relaxed moods, All through I have been knowing you as a respectable woman of great deeds, You have always been a good example ,a role model to  our girls, A rare breed of amazing pulchritude with brains. ")')
    #c.execute('INSERT INTO posts VALUES("Message TO Amina Mohamed", "I heard that you are soon arresting comrades with HELB default, Comrades of which life after campus has been nothing but a nightmare, Comrades who have been tarmacking in search of jobs, Comrades who have first class Hons degrees as a decoration, Comrades whom you deny jobs and employ,recycle old folks, Comrades who have turned into petty hustlers, This must be the biggest joke of the century.") ')
  #  c.execute('INSERT INTO posts VALUES("TRYING again", "Trying adding some other stuffs in Python")')
