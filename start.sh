export SECRET_KEY=phoenix
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://april:2222@localhost/pitch'
# python3 manage.py db init
# python3 manage.py db migrate -m "Deployment Migration"
# python3 manage.py db upgrade
# python3.9 manage.py server