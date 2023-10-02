class Config:
    DEBUG = True
    TESTING = True
    
    CONNECTORCARD = "https://tlacorp.webhook.office.com/webhookb2/68b12b28-cd0e-424a-905c-124e14e37b9b@0527d0d1-ef38-4748-909a-2d97379c33b2/IncomingWebhook/c844e52f0a5d43f8bbe7c14c40b6ae78/cc4ea250-1e8f-4111-a521-d926c707c306"

    #Configuracion de base de datos
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://kaxper:miloja@localhost/tlakms"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True