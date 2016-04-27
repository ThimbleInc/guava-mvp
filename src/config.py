import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	SECRET_KEY = 'hello_its_me'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'guava.db')
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True
	
class ProductionConfig(Config):
	DEBUG = False
