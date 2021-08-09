from flask import Flask

from hotspot_helper.views import VIEWS


def create_app(name):
    app = Flask(name)
    app.register_blueprint(VIEWS)
    return app


def main():
    app = create_app(__name__)
    app.run('0.0.0.0', threaded=True, debug=True)


if __name__ == '__main__':
    main()
