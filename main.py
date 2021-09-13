import os
import app

app = app.create_app(os.getenv('FLASK_CONFIG') or 'development')