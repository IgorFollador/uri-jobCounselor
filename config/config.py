class Config:
    DEBUG = True
    #                                       //user:password@localhost/db_name
    SQLALCHEMY_DATABASE_URI = 'postgresql://...'
    SQLALCHEMY_TRACK_MODIFICATIONS = False