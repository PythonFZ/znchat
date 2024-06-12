from celery import Celery, Task
from flask import Flask
from flask_socketio import SocketIO

from znchat.main import main_blueprint, init_socketio_events


def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY={
            "broker_url": "redis://localhost",
            "result_backend": "redis://localhost",
            "task_ignore_result": True,
        },
    )
    app.config.from_prefixed_env()

    # Initialize SocketIO
    socketio = SocketIO(app, message_queue=app.config["CELERY"]["broker_url"])

    # Initialize Celery
    celery_init_app(app)

    # Register routes and socketio events
    app.register_blueprint(main_blueprint)
    init_socketio_events(socketio)

    # Add socketio to app extensions for easy access
    app.extensions["socketio"] = socketio

    return app
