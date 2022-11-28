from src.api.controllers.accept_controller import blueprint \
    as accept_blueprint
from flask_restx import Api
from src.api.controllers.accept_controller import acceptNamespace

api_extension = Api(
    accept_blueprint,
    title='BIDS API',
    version='1.0',
    description='BIDS API',
    doc='/swagger'
)

api_extension.add_namespace(acceptNamespace)