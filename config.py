import os
import connexion
from flask_sqlalchemy import SQLAlchemy

AWS_USER = 'AKIA2BYS3MX7V3RNOD5W'
AWS_PASS = 'ZnVjayB5b3UgdmVyeSBtdWNoCg==U4QyBaxVyRZ9'

vuln_app = connexion.App(__name__, specification_dir='./openapi_specs')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(vuln_app.root_path, 'database/database.db')
vuln_app.app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
vuln_app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

vuln_app.app.config['SECRET_KEY'] = 'random'
# start the db
db = SQLAlchemy(vuln_app.app)

vuln_app.add_api('openapi3.yml')


