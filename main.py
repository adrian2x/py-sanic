import os
from sanic import Sanic
from orjson import dumps, loads

from api.tasks import tasks

# example using a custom json serializer
app = Sanic(__name__, dumps=dumps, loads=loads)

# Config settings can be added to the app like so
app.config.SECRET = "my_custom_secret"
app.config.DB_NAME = 'appdb'
app.config['DB_USER'] = 'appuser'

db_settings = {
    'DB_HOST': 'localhost',
    'DB_NAME': 'appdb',
    'DB_USER': 'appuser'
}
app.config.update(db_settings)

# Add any application-wide data or objects
# app.ctx.db = Database()

# Register blueprints here
app.blueprint(tasks, version=1)

if __name__ == "__main__":
    PORT = os.environ.get("PORT")
    port = int(PORT or 8000)
    app.run(host="0.0.0.0", port=port, auto_reload=PORT is None)
