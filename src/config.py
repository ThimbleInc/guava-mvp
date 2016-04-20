import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = False

class DevelopmentConfig(Config):
	DEBUG = True
	
class ProductionConfig(Config):
	DEBUG = False
