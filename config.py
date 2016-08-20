# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
DB_PROTO    = 'mysql://'
DB_USER     = 'root'
DB_PWD      = '0000'
DB_SERVER   = 'localhost'
DB_NAME     = 'drawml'
DB_URI = DB_PROTO + DB_USER + ':' + DB_PWD + '@' + DB_SERVER + '/' + DB_NAME
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Google auth
GOOGLE_LOGIN_CLIENT_ID = "166774559697-1gchdfdv27lu9imof4dutsrhilpv7anm.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "GoAPQxXJhFc-jkHHjaT6gaFS"

OAUTH_CREDENTIALS={
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
}