import eventlet

# eventlet.monkey_patch(all=False, socket=True)
eventlet.monkey_patch()

from znchat.app import create_app

__all__ = ["create_app"]

if __name__ == "__main__":
    app = create_app()
    socketio = app.extensions["socketio"]
    socketio.run(app, host="0.0.0.0", port=3141, debug=False)
