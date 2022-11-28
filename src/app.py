from flask import Flask
from flask_restx import Api
from src.api.controllers.accept_controller import blueprint \
    as accept_blueprint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(accept_blueprint)

if __name__ == "__main__":
    app.run()