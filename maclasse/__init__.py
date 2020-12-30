from databases import Database
from sanic import Sanic
from sanic_restful_api import Api

from maclasse.routes import AjoutEleve

app = Sanic(__name__)
app.update_config("config.py")
api = Api(app)
app.db = Database(app.config.DB_URL)


def setup_database():
    @app.listener("after_server_start")
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener("after_server_stop")
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()


api.add_resource(AjoutEleve, "/")
