from dash import Dash
from layout import layout
from callbacks import get_callbacks

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)

app.layout = layout

get_callbacks(app)

if __name__ == '__main__':
   app.server.run(debug=True, threaded=True)
