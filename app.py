from flask import Flask
from framework.Router import Router

import config

def create_app():
    #Start the app..
    app = Flask(__name__, static_url_path='/static', 
                        static_folder=config.STATIC_DIR,
                        template_folder=config.VIEWS_DIR)

    #Confing start...
    app.config.from_object(config)

    #Database connection
    from framework import Database
    Database.init_app(app)

    Router.run(app)

    app.debug = True

    return app

if __name__ == '__main__':
    create_app().run()
