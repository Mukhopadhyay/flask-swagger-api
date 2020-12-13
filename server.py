import warnings
warnings.filterwarnings('ignore')

import os
from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import routes
import configs as cfg

routes = routes.get_routes()

# SwaggerUI config
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    cfg.SERVER_SETTINGS.get('SWAGGER_URL'),
    cfg.SERVER_SETTINGS.get('SWAGGER_API_URL'),
    config={
        'app_name':'flask_swagger_api'
    },
    blueprint_name='dota_hero_api'
)

app = Flask(__name__)
# Registering the routes
app.register_blueprint(routes)
# Registering the swagger blueprint
app.register_blueprint(
    SWAGGER_BLUEPRINT,
    url_prefix=cfg.SERVER_SETTINGS.get('SWAGGER_URL')
)

# Driver code
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', cfg.SERVER_SETTINGS.get('PORT')))
    CORS = CORS(app)
    # Dev mode run
    app.run(port=PORT, debug=True)