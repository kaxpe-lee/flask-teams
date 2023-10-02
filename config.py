class Config:
    DEBUG = True
    TESTING = True
    
    
    #Configuracion de base de datos
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://kaxper:miloja@localhost/tlakms"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    
    DEBUG = True
    TESTING = True