import warnings
warnings.filterwarnings('ignore')

import os
from flask import Flask
from flask_cors import CORS
from routes import routes
import configs as cfg

routes = routes.get_routes()

app = Flask(__name__)
# Registering the routes
app.register_blueprint(routes)

# Driver code
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', cfg.PORT))
    CORS = CORS(app)
    # Dev mode run
    app.run(port=PORT, debug=True)