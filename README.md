# Real estate agency website

The site is under development, so only the page with a list of apartments and the admin panel for filling the database are available.

## Launch

- Download the code
- Install dependencies with the command `pip install -r requirements.txt`
- Create a database file and apply all migrations at once with the command `python3 manage.py migrate`
- Start the server with the command `python3 manage.py runserver`

## Environment variables

Some of the project settings are taken from environment variables. To define them, create a `.env` file next to `manage.py` and write the data there in the following format: `VARIABLE=value`.

There are 3 variables available:
- `DEBUG` - debug mode. Set to True to see debugging information in case of an error.
- `SECRET_KEY` — secret key of the project
- `ALLOWED_HOSTS` - see [Django documentation](https://docs.djangoproject.com/en/5.1/ref/settings/#allowed-hosts).
- `DATABASE` - one-line address to the database, for example: `sqlite:///db.sqlite3`. More information in [documentation](https://github.com/jacobian/dj-database-url)

     This allows you to easily switch between databases: PostgreSQL, MySQL, SQLite - it doesn’t matter, you just need to enter the desired address.

## Project goals

The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).