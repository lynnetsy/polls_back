from flask import jsonify
from ms import app
from ms.controllers import PollController


url_prefix = app.config.get('URL_PREFIX')

@app.route(f"{url_prefix}", methods=["POST"])
def add():
    return PollController().add()


@app.route(f"{url_prefix}/about")
def about():
    return jsonify({
        "data": {
            "name": app.config.get('APP_NAME'),
            "version": app.config.get('APP_VERSION'),
        },
        "code": 200
    }), 200
