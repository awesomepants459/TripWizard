import os

#configs
MAIN_DIR        = os.path.dirname(os.path.realpath(__file__))+"/"

APP_DIR         = MAIN_DIR+"application/"

VIEWS_DIR       = APP_DIR+"views/"

CONTROLLER_DIR  = APP_DIR+"controllers/"

MODEL_DIR       = APP_DIR+"models/"

STATIC_DIR      = APP_DIR+"static"

DATABASE_NAME   = 'data.db'

#change in "production"
SECRET_KEY="dev"

