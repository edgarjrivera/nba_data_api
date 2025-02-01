from flask import Blueprint

# Create a Blueprint for the app routes
api_bp = Blueprint('api', __name__)

# Import individual route files
from .games import *
from .players import *
from .teams import *
