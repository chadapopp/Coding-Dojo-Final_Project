from flask_app import app
from flask_app.controllers import index_controller
from flask_app.controllers import auth_controller
from flask_app.controllers import listing_controller
from flask_app.controllers import booking_controller



if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True, port=5005)
