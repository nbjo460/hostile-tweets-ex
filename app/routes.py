import fastapi
from manager import Manager

class Routes:
    app = fastapi.FastAPI()

    @app.get("/")
    def root(self):
        return {}
    @app.get("/load")
    def load_db(self):
        return Manager().get_data()
