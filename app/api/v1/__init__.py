from flask import Blueprint
from app.api.v1.endpoints.convert import convert_ada_file

# Create v1 API blueprint
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

# Register routes
api_v1.add_url_rule('/convert', 'convert', convert_ada_file, methods=['POST'])