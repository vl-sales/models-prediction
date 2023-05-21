from src.app import create_app
import os
import logging
from waitress import serve
logging.basicConfig(level=logging.DEBUG)

app = create_app()

if __name__ == '__main__':
    port = os.getenv('PORT') if os.getenv('PORT') else "8000"
    logging.debug("Starting SERVER on port: " + port)
    serve(app, host="0.0.0.0", port=port)