from flask.app import Flask

app = Flask(__name__)

import prodavnica.main_view
import prodavnica.prodavnica_view
import prodavnica.artikli_view
