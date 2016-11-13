from flask.app import Flask
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask_injector import FlaskInjector
from werkzeug.utils import redirect

from plugin.operator.core.injector_modules import GlobalFlask, OperatorList

app = Flask(__name__)

@app.route("/")
def index(title:str,operators:OperatorList):
    return render_template("index.html",operators=operators,title=title)

@app.route("/racunanje", methods=['GET', 'POST'])
def racunanje(title:str,operators:OperatorList):
    first=0
    second=0
    if(len(operators)==0):
        return redirect(url_for('index'))
    else:
        operator = operators[0].operator_identifier()
    try:
        first , converted_first = convert_to_int(request.form['first_number'])
        second , converted_second = convert_to_int(request.form['second_number'])
        operator=request.form['operator']
        if not converted_first or not converted_second:
            return render_template("racunanje.html", title=title, operators=operators, first=first, second=second,
                                   operator=operator)
        rezultat=None
        for o in operators:
            if o.operator_identifier() == operator:
                rezultat=o.operation(first,second)
        if(rezultat is None):
            return render_template("racunanje.html", title=title, operators=operators )
        else:
            return redirect(url_for('izracunato',rezultat=rezultat))
    except:
        return render_template("racunanje.html",title=title,operators=operators,first=first,second=second,operator=operator)


def convert_to_int(number,default=0):
    try:
        value=int(number)
        return value,True
    except:
        value=default
        return value, False

@app.route("/izracunato")
def izracunato(title:str):

    return render_template("izracunato.html",title=title,rezultat=request.args.get("rezultat"))

def main():
    FlaskInjector(app=app, modules=[GlobalFlask])
    app.run(debug=True)


if __name__ == "__main__":
    main()