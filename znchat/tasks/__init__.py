from celery import shared_task
from flask import current_app


@shared_task
def hello(sid):
    print(f"Hello, to! {sid}")
    current_app.extensions["socketio"].emit("log", {"data": "Hello, World!"}, to=sid)
