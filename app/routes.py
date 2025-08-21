import fastapi
from manager import Manager

class Routes:
    app = fastapi.FastAPI()

    @app.get("/")
    def root(self):
        return {}
    @app.get("/load")
    def load_db(self):
        """
        For load the data.
        :return:
        """
        return Manager().get_data()
