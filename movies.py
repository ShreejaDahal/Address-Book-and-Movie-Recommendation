import sqlite3


class AddressBook(object):
    def __init__(self, filename):
        self.dbfilename = filename
        self.db = sqlite3.connect(self.dbfilename)
        c = self.db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS movies (title TEXT PRIMARY KEY, genres TEXT, rating TEXT, "
                  "length INTEGER, studio TEXT, imdb_rating NUMERIC, year INTEGER)")
        self.db.commit()

    def view_all(self):
        c = self.db.cursor()
        c.execute('SELECT * FROM movies ORDER BY title')
        contact = c.fetchall()
        c.close()
        return contact

    def request_movie(self):
        title = input("Enter the movie title")
        genres = input("Enter the genres ")
        rating = input("Enter the rating")
        length = input("Enter the total duration of the movie in minutes")
        studio = input("Enter the studio name")
        imdb_rating = input("Enter the imdb rating")
        year = input("Enter the year")
        c = self.db.cursor()
        c.execute('INSERT INTO movies(title, genres, rating, length, studio, imdb_rating, year) VALUES (?,?,?,?,?,?,?)',
                  (title, genres, rating, length, studio, imdb_rating, year))
        self.db.commit()
        c.close()

    def delete_movie(self):
        user_input = input("Enter the movie name ")
        c = self.db.cursor()
        c.execute('DELETE FROM movies WHERE title=?', (user_input,))
        self.db.commit()
        c.close()

    def view_movie_by_name(self):
        user_input = input("Enter the movie's name")
        c = self.db.cursor()
        c.execute('SELECT * FROM movies WHERE title=? ORDER BY year DESC', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact

    def view_movie_by_genre(self):
        user_input = input("Enter the genre")
        c = self.db.cursor()
        c.execute('SELECT * FROM movies WHERE genres=? ORDER BY year DESC', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact

    def view_movie_by_studio(self):
        user_input = input("Enter the studio")
        c = self.db.cursor()
        c.execute('SELECT * FROM movies WHERE studio=? ORDER BY year DESC', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact

    def view_movie_by_year(self):
        user_input = input("Enter the movie year")
        c = self.db.cursor()
        c.execute('SELECT * FROM movies WHERE year=? ORDER BY imdb_rating DESC', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact

    def view_movie_by_rating(self):
        user_input = input("Enter the rating")
        c = self.db.cursor()
        c.execute('SELECT * FROM movies WHERE rating=? ORDER BY imdb_rating DESC', (user_input,))
        contact = c.fetchall()
        c.close()
        return contact


ab = AddressBook(filename='movies.db')

while True:
    user_answer = input("Enter 1 view all movies, 2 to view by title, 3 to view by genres, 4 to view by year,"
                        "5 to view by rating, 6 to view by studio name , 7 to request a movie, and 8 to delete a movie")
    if user_answer == "1":
        for row in ab.view_all():
            print(row)

    elif user_answer == "2":
        for row in ab.view_movie_by_name():
            print(row)

    elif user_answer == "3":
        for row in ab.view_movie_by_genre():
            print(row)

    elif user_answer == "4":
        for row in ab.view_movie_by_year():
            print(row)

    elif user_answer == "5":
        for row in ab.view_movie_by_rating():
            print(row)

    elif user_answer == "6":
        for row in ab.view_movie_by_studio():
            print(row)

    elif user_answer == "7":
        ab.request_movie()

    elif user_answer == "8":
        ab.delete_movie()

    else:
        print("Come back next time!")
        break
