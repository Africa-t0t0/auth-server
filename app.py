from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from utils import handlers
from utils import database_config
from models import db, User

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_object(database_config.Config)
db.init_app(app=app)
jwt = JWTManager(app)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="pbkdf2:sha256")
    new_user = User(username=data["username"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Invalid Credentials"}), 401

    # create jwt token and return it
    access_token = create_access_token(identity=user.username)
    return jsonify({"access_token": access_token}), 200


# dummy endpoint for testing
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    cleaned_dd = handlers.handle_server_configuration()

    debug = cleaned_dd["debug"]
    port = cleaned_dd["port"]

    with app.app_context():
        db.create_all()

    app.run(debug=debug, port=port)
