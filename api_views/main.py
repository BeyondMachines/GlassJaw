from flask import Response
import sys
from models.user_model import *
from app import destructive
from api_views.users import error_message_helper


def populate_db():
    if destructive:
        db.drop_all()
        db.create_all()
        User.init_db_users()
        response_text = '{ "message": "Database populated." }'
        response = Response(response_text, 200, mimetype='application/json')
        return response
    else:
        return Response(error_message_helper("Destructive actions not allowed"), 401, mimetype="application/json")


def basic():
    response_text = '{ "message": "VAmPI the Vulnerable API", "Help": "VAmPI is a vulnerable on purpose API. It was ' \
                    'created in order to evaluate the efficiency of third party tools in identifying vulnerabilities ' \
                    'in APIs but it can also be used in learning/teaching purposes." } '
    response = Response(response_text, 200, mimetype='application/json')
    return response
