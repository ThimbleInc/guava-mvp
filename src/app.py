from src import app
import config


cf = config.DevelopmentConfig()
app.run(debug=cf.DEBUG);
