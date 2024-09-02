ENVIRONMENT='production'

DATABASE_FILE=''
if ENVIRONMENT == 'production':
    DATABASE_FILE='database.csv'
else:
    DATABASE_FILE='test_database.csv'