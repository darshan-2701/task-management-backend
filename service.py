from flask import Flask
from flask_cors import CORS

from controllers import task_controller

app = Flask(__name__)
cors_api = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(task_controller.task_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
