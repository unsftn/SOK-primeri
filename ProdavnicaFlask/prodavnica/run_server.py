from flask_injector import FlaskInjector

from prodavnica import app
from prodavnica.injector_modules import GlobalFlask


def main():
    FlaskInjector(app=app, modules=[GlobalFlask])
    app.run(debug=True)

if __name__ == '__main__':
    main()