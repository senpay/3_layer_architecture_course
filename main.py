from flask import Flask, jsonify, request
from business.exceptions import InvalidUserException, Unauthorized, UserNotFoundException

from business.user_service import UserService
from presentation.user_controller import UserController

app = Flask(__name__)
user_service = UserService()
user_controller = UserController(user_service)

@app.route("/")
def hello_world():
    return "I am OK!"

@app.route("/user", methods = ['POST'])
def user():
    incoming_data = request.get_json(force=True)
    try:
        user_data = user_controller.create_user(incoming_data)
    except InvalidUserException:
        return jsonify({"message": "Invalid user data"}), 400
    return jsonify(user_data)

# Now updated to enforce authentication
@app.route("/user/<user_id>")
def get_user(user_id):
    try:
        authorization_header = request.headers.get('Authorization')
        user_data = user_controller.get_user(user_id,
                                             authorization_header)
    except UserNotFoundException:
        return jsonify({"message": "User not found", "user_id": user_id}), 404
    except Unauthorized as exc:
        return jsonify({"message": str(exc)}), 403
    return jsonify(user_data)


@app.route("/authenticate", methods = ['POST'])
def authenticate():
    try:
        incoming_data = request.get_json(force=True)
        user_data = user_controller.authenticate(incoming_data)
    except UserNotFoundException:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user_data)
    


if __name__ == "__main__":
    app.run(debug=True)